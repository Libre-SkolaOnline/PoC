# PoC - Škola Online

Proof of Concept pro API Škola Online. Umožňuje přístup k rozvrhům, úkolům, znamkám, zprávám a informacím o uživateli.

## Instalace

Vyžaduje Python 3.6+

```
pip install requests
```

## Spuštění

```
python runner.py
```

Program spustí interaktivní menu, ze kterého si vyberete modul:

- rozvrh.py - Zobrazení rozvrhu
- ukoly.py - Výpis úkolů
- znamky.py - Zobrazení známek
- zpravy.py - Čtení zpráv
- userinfo.py - Informace o uživateli

Při prvním spuštění budete požádáni o přihlášení do Škola Online.

## Moduly

- `auth.py` - Autentizace a správa tokenů
- `rozvrh.py` - Práce s rozvrhami
- `ukoly.py` - Práce s úkoly
- `znamky.py` - Práce se znamkami
- `zpravy.py` - Čtení zpráv
- `userinfo.py` - Informace o uživateli
