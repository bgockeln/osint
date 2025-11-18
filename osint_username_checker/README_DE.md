# OSINT Username Checker
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-work--in--progress-yellow)

Dieses Projekt ist ein **einfacher Username-Checker**, der Einsteigern(mir) praktische Erfahrung mit grundlegenden OSINT-Techniken (Open Source Intelligence) vermittelt.

Das Skript funktioniert, indem es eine **HTTP-Anfrage** an den Server der ausgewählten Webseite sendet und die Antwort überprüft, um festzustellen, ob ein Benutzername existiert.

Derzeit unterstützte Seiten:

- **GitHub:** `https://github.com/<username>`
- **Instagram:** `https://instagram.com/<username>`  
- **TikTok:** `https://www.tiktok.com/@<username>`  
- **X/Twitter:** `https://www.x.com/<username>`  

*(Instagram und X/Twitter wurden getestet, können jedoch **falsche Positivmeldungen** erzeugen und sind daher nicht vollständig zuverlässig.)*

## Funktionsweise
1. Der Benutzer gibt einen Benutzernamen ein.  
2. Das Skript erstellt die URL für die ausgewählte Webseite.  
3. Das Skript sendet eine Anfrage an den Server.  
4. Das Skript prüft den **HTTP-Statuscode** (200 = existiert, 404 = nicht gefunden usw.) und, in einigen Fällen, einige Schlüsselwörter im Seiteninhalt, um eine bestmögliche Einschätzung zu treffen.

## Einschränkungen
- Es können nur **öffentliche Profile** zuverlässig erkannt werden.  
- Instagram und X/Twitter können aufgrund von JavaScript-generierten Inhalten oder Login-Seiten falsche Ergebnisse liefern.  

![Beispiel 1](imgs/pic1.PNG)

![Beispiel 2](imgs/pic2.PNG)
