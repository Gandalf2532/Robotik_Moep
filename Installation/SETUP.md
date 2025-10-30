# Installation
## Abhängigkeiten und Dinge, die installiert werden müssen:
- [git](https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe)
- [Visual Studio Code](https://code.visualstudio.com/docs/?dv=win64user)
- [Dev Container Erweiterung für Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
Bei allen gilt: Downloaden (also auf die Links klicken) und dann ausführen. Wenn etwas in den Path soll, gerne akzeptieren (vor allem git)
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