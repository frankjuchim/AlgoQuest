"""Ersetzt den Begriff „Kata“ durch „Warm-up“ in Texten, docx/pptx-XML, txt/json/md.
Artikel vor dem freistehenden Wort (die Kata → das Warm-up) werden mit angepasst, auch über Run-Grenzen hinweg."""
import re, sys, zipfile, os, io, json

SKIP = re.compile(r'[Kk]atalog|Kataster|[Kk]atastroph|katakomb', re.I)

def wort(t):
    t = re.sub(r'\bkata_(w|\*)', r'warmup_\1', t)
    t = re.sub(r'\bKATAS\b', 'WARM-UPS', t)
    t = re.sub(r'KATA(?=[-\s:.,)]|$)', 'WARM-UP', t)
    t = re.sub(r'(?<![A-Za-zÄÖÜäöüß])Katas\b', 'Warm-ups', t)
    t = re.sub(r'Kata(?!log|ster|stroph|komb)(?=[^a-zäöüß]|$)', 'Warm-up', t)
    return t

# Artikel (feminin → neutrum), nur wenn danach das freistehende Wort folgt (nicht „Warm-up-Karte“ o. Ä.)
ART = [(r'\bdie', 'das'), (r'\bDie', 'Das'), (r'\beine', 'ein'), (r'\bEine', 'Ein'), (r'\bjede', 'jedes'), (r'\bJede', 'Jedes'),
       (r'\bdiese', 'dieses'), (r'\bDiese', 'Dieses'), (r'\bdeine', 'dein'), (r'\bDeine', 'Dein'), (r'\beure', 'euer'),
       (r'\bEure', 'Euer'), (r'\bkeine', 'kein'), (r'\bwelche', 'welches'), (r'\bWelche', 'Welches'), (r'\bzur', 'zum'),
       (r'\bZur', 'Zum'), (r'\beiner', 'einem'), (r'\bheutige', 'heutige'), (r'\bnächste', 'nächste'), (r'\berste', 'erste')]
STANDALONE = re.compile(r'^((?:Papier-|Blitz-|Zähl-)?Warm-up)(?!-)(?!s)')

def artikel_fix(prefix, rest):
    """prefix endet ggf. mit Artikel + Leerzeichen; rest beginnt mit dem Wort."""
    if not STANDALONE.match(rest):
        return prefix
    for a, b in ART:
        m = re.search(a + r'(\s+)$', prefix)
        if m:
            return prefix[:m.start()] + b + m.group(1)
    m = re.search(r'\bder(\s+)$', prefix)   # „der Kata“ (Genitiv/Dativ) → markieren für Handprüfung
    if m:
        PRUEF.append(prefix[-30:] + '|' + rest[:30])
    return prefix

PRUEF = []

def fix_text(t):
    t = wort(t)
    out = []; i = 0
    for m in re.finditer(r'(?:Papier-|Blitz-|Zähl-)?Warm-up', t):
        pre = t[i:m.start()]
        joined = ''.join(out) + pre
        joined = artikel_fix(joined, t[m.start():])
        out = [joined]; i = m.start()
    out.append(t[i:])
    return ''.join(out)

def fix_xml(xml, tag):
    """tag: 'w:t' oder 'a:t'. Bearbeitet Absätze (w:p / a:p) knotenweise mit Artikelkorrektur über Knotengrenzen."""
    para = 'w:p' if tag == 'w:t' else 'a:p'
    node_re = re.compile(r'(<' + tag + r'(?:\s[^>]*)?>)(.*?)(</' + tag + '>)', re.S)
    def do_para(pm):
        p = pm.group(0)
        nodes = list(node_re.finditer(p))
        if not nodes or not re.search(r'[Kk]ata|KATA', p):
            return p
        texts = [wort(n.group(2)) for n in nodes]
        # Artikel innerhalb und über Knoten hinweg
        for k in range(len(texts)):
            t = texts[k]
            starts = [m.start() for m in re.finditer(r'(?:Papier-|Blitz-|Zähl-)?Warm-up', t)]
            for s in reversed(starts):
                pre = t[:s]
                if pre.strip():
                    t = artikel_fix(pre, t[s:]) + t[s:]
                else:
                    j = k - 1
                    while j >= 0 and texts[j] == '':
                        j -= 1
                    if j >= 0:
                        texts[j] = artikel_fix(texts[j] + pre, t[s:])
                        if pre:
                            texts[j] = texts[j][:len(texts[j]) - len(pre)]
            texts[k] = t
        res = []; last = 0
        for n, t in zip(nodes, texts):
            res.append(p[last:n.start()]); res.append(n.group(1) + t + n.group(3)); last = n.end()
        res.append(p[last:])
        return ''.join(res)
    return re.sub(r'<' + para + r'[ >].*?</' + para + '>', do_para, xml, flags=re.S)

def fix_office(path):
    zin = zipfile.ZipFile(path)
    changed = False
    buf = io.BytesIO(); zout = zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        d = zin.read(it.filename)
        if it.filename.endswith('.xml'):
            s = d.decode('utf8')
            if re.search(r'[Kk]ata|KATA', s):
                tag = 'a:t' if it.filename.startswith('ppt/') else 'w:t'
                s2 = fix_xml(s, tag)
                if tag == 'w:t':
                    s2 = s2  # docProps etc. bleiben
                if s2 != s:
                    changed = True; d = s2.encode('utf8')
        zout.writestr(it, d)
    zout.close(); zin.close()
    if changed:
        open(path, 'wb').write(buf.getvalue())
    return changed

if __name__ == '__main__':
    for f in sys.argv[1:]:
        if f.endswith(('.docx', '.pptx')):
            if fix_office(f): print('geändert', f)
        else:
            t = open(f, encoding='utf-8').read(); t2 = fix_text(t)
            if t2 != t: open(f, 'w', encoding='utf-8').write(t2); print('geändert', f)
    if PRUEF:
        print('HANDPRUEFUNG („der …“):'); [print('  ', x) for x in PRUEF]
