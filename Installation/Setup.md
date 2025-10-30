# Installation
## git
### Installer:
- https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe
## Klonen des Repositorys auf das Gerät
In cmd diese 3 Befehle ausführen
```bash
cd %userprofile%/Documents

mkdir GitHub && cd ./GitHub

git clone https://github.com/MOEP-Robotik/Robotik_Moep.git
```
Dabei wird ein neuer Ordner GitHub im Ordner Dokumente erstellt. In diesem wird das Repository geklont. Dort wird auch gearbeitet.
In den Unterordner FLL2025_26 sollte ein Ordner .vscode sein. Es existiert darin ein .devcontainer. Nach dem Öffnen des geklonten Ordners in Visual Studio Code sollte unten rechts eine Meldung kommen, ob der Ordner als DevContainer geöffnet werden soll. Dort auf "Reopen" o.ä. klicken. Beim ersten öffnen dauert es etwas länger als danach.
## Pybricks
### Auf dem Spike Prime Hub (im Normalfall bereits geschehen)
Tutorial auf https://code.pybricks.com/ folgen