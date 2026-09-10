# Backup_System

Ein Backup-Werkzeug für **Linux**, geschrieben in Python, mit grafischer Oberfläche (PyQt6).
Gemeinschaftsprojekt von [@DocKoRn](https://github.com/DocKoRn) und
[@bloldi](https://github.com/bloldi).

## Zielsystem

**Linux, Python ≥ 3.12.** Windows und macOS sind nicht vorgesehen – das Werkzeug greift auf
Dateirechte, Einhängepunkte und `systemd` zu.

Entwickelt und geprüft wird auf zwei Distributionen gleichzeitig:

| Distribution | Basis | wer |
|---|---|---|
| CachyOS | Arch | @DocKoRn |
| Ubuntu 24.04 LTS | Debian | @bloldi |

Das ist Absicht, kein Zufall: Was auf beiden läuft, läuft mit hoher Wahrscheinlichkeit auch
auf anderen Distributionen. Die Unterschiede zwischen Arch und Debian sind uns dabei schon
mehrfach begegnet, deshalb gelten für den ganzen Code drei Regeln:

- **Immer `python3` aufrufen**, nie `python` – unter Ubuntu gibt es den Befehl `python` nicht.
- **PyQt6 wird per `pip` in ein venv installiert** (`requirements.txt`), nicht als Paket der
  Distribution. Sonst hat jeder eine andere Version.
- **`from __future__ import annotations`** steht in jeder Kern-Datei, damit moderne
  Typangaben auch unter Python 3.12 funktionieren.

Wo sich die Einrichtung unterscheidet (Paketnamen, Pfade), wird sie **getrennt nach
Distribution** beschrieben – keine `pacman`-Befehle in einer Anleitung, die auch für Ubuntu
gelten soll.

## Stand

Das Projekt ist in der Bauphase; im Repository liegt noch kein Programmcode. Der Bauplan
(Fassung 3, Stand 01.09.2026) beschreibt Klassen, Datenhaltung und acht Bauphasen und liegt
bisher außerhalb des Repositories.

## Mitarbeiten

`main` ist geschützt: kein direkter Push, keine Historie umschreiben, Änderungen laufen über
einen Pull Request.

**Nie echte Daten ins Repository** – keine IP-Adressen, keine Schlüssel, keine Pfade aus dem
Privatleben. Testdaten sind erfunden.
