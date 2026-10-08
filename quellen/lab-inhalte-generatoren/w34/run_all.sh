#!/bin/bash
# Baut welt3.json/welt4.json neu (Java-Laeufe), validiert §3–§5 und prueft, dass jeder Code-Block kompiliert wurde
set -e
cd "$(dirname "$0")"
python3 build_w3.py
python3 build_w4.py
python3 validate.py ../content/welt3.json ../content/welt4.json
python3 codecheck.py
