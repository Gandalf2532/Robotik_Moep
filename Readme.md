# Pybricks Code für unsere Roboter

Das hier ist unser Repository, um unsere FLL Projekte zu sichern und Backups herzustellen.

> [!IMPORTANT]
> Tutorial ist noch nicht fertig. Visual Studio Code und die Pybricks packages müssen anders vorbereitet werden. Langsam wird es.
> Finger weg von .devcontainer, .vscode und requirements.txt !!!

# Tutorial zu Python, Pybricks und der Installation der Abhängigkeiten, sowie eine kleine übersicht über git

## Inhaltsverzeichnis
- [Installation](#installation)
- [Python](#python-grundlagen)
- [Pybricks](#pybricks-grundlagen)
- [git](#simple-git-Befehle)

## Installation

### Abhängigkeiten und Dinge, die installiert werden müssen:
> [!NOTE]
> Dafür einfach install.bat ausführen. Die kann man online einfach so downloaden (über GitHub.com).

- [git](https://git-scm.com/install)
- [Visual Studio Code] (Desktophttps://code.visualstudio.com/docs/?dv=win64user)

Bei allen gilt: downloaden und dann ausführen. Wenn etwas in den Path soll, gerne akzeptieren (vor allem git)

### Klonen des Repositorys auf das Gerät
In cmd diese 3 Befehle ausführen
```bash
cd %userprofile%/Documents

mkdir GitHub && cd ./GitHub

git clone https://github.com/MOEP-Robotik/Robotik_Moep.git

git config --global user.name $user && git config --global user.email $email
```
Dabei wird ein neuer Ordner GitHub im Ordner Dokumente erstellt. In diesem wird das Repository geklont. Dort wird auch gearbeitet. Nach dem Öffnen des geklonten Ordners in Visual Studio Code das Terminal öffnen (Standard Tastenkombination ist: STRG + ö) und `pip install -r requirements.txt` ausführen.
> [!IMPORTANT]
> $user durch unseren Nutzernamen ersetzen
> $email durch unsere Email ersetzen. Beim ersten Commit wird dann eine Aufforderung gestellt, sich anzumelden. @Gandalf2532 hat das Passwort. 
 

## Pybricks
### Auf dem Spike Prime Hub (im Normalfall bereits geschehen)
Tutorial auf https://code.pybricks.com/ folgen
## Python Grundlagen
Eine gute "Grundlage" bilden die Python-Docs unter python.org

## Pybricks Grundlagen
Findet man auch online

## simple git Befehle
> [!TIP]
> Die Befehle müssen **nicht** gelernt werden, sofern die Visual Studio Code Erweiterung für GitHub verwendet wird

**git ...**
- ...**help**
- ...add
- ...push
- ...commit

- ...pull






