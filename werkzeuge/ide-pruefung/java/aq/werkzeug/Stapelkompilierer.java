package aq.werkzeug;

import javax.tools.*;
import java.io.*;
import java.nio.file.*;
import java.util.*;

/**
 * Kompiliert viele kleine Übersetzungseinheiten schnell im selben Prozess.
 * Aufbau: <wurzel>/<block>/<kandidat>/*.java. Je Block werden die Kandidaten in alphabetischer Reihenfolge
 * kompiliert, bis einer fehlerfrei ist. Ausgabe je Block:
 *   BLOCK <block> ok <kandidat>
 *   BLOCK <block> fehler <anzahl Fehler> <Zeile>: <Meldung>   (Kandidat mit den wenigsten Fehlern)
 * Aufruf: java aq.werkzeug.Stapelkompilierer <klassenpfad> <wurzel>
 */
public final class Stapelkompilierer {
    public static void main(String[] args) throws IOException {
        JavaCompiler javac = ToolProvider.getSystemJavaCompiler();
        Path wurzel = Paths.get(args[1]);
        Path aus = Files.createTempDirectory("stapel-");
        List<Path> bloecke;
        try (var s = Files.list(wurzel)) { bloecke = s.filter(Files::isDirectory).sorted().toList(); }
        for (Path block : bloecke) {
            List<Path> kandidaten;
            try (var s = Files.list(block)) { kandidaten = s.filter(Files::isDirectory).sorted().toList(); }
            String bester = null;
            int besteAnzahl = Integer.MAX_VALUE;
            String ok = null;
            for (Path k : kandidaten) {
                List<File> quellen = new ArrayList<>();
                try (var s = Files.list(k)) { s.filter(p -> p.toString().endsWith(".java")).sorted().forEach(p -> quellen.add(p.toFile())); }
                DiagnosticCollector<JavaFileObject> diag = new DiagnosticCollector<>();
                try (StandardJavaFileManager fm = javac.getStandardFileManager(diag, Locale.ROOT, java.nio.charset.StandardCharsets.UTF_8)) {
                    List<String> opt = List.of("-cp", args[0], "-d", aus.toString(), "-proc:none", "-nowarn", "-Xlint:none", "-encoding", "UTF-8");
                    boolean erfolg = javac.getTask(null, fm, diag, opt, null, fm.getJavaFileObjectsFromFiles(quellen)).call();
                    if (erfolg) { ok = k.getFileName().toString(); break; }
                    List<Diagnostic<? extends JavaFileObject>> fehler = diag.getDiagnostics().stream()
                        .filter(d -> d.getKind() == Diagnostic.Kind.ERROR).toList();
                    if (!fehler.isEmpty() && fehler.size() < besteAnzahl) {
                        besteAnzahl = fehler.size();
                        Diagnostic<? extends JavaFileObject> d = fehler.get(0);
                        String datei = d.getSource() == null ? "?" : Paths.get(d.getSource().toUri()).getFileName().toString();
                        bester = k.getFileName() + "/" + datei + ":" + d.getLineNumber() + ": " + d.getMessage(Locale.ROOT).split("\n")[0];
                    }
                }
            }
            if (ok != null) System.out.println("BLOCK " + block.getFileName() + " ok " + ok);
            else System.out.println("BLOCK " + block.getFileName() + " fehler " + besteAnzahl + " " + bester);
        }
    }
}
