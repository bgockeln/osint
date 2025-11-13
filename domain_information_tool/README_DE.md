# Domain Information Lookup Tool

Ein weiteres einfaches ``Python-Skript``, das verschiedene Informationen
über eine angegebene Domain sammelt.

Es unterstützt derzeit:

- **WHOIS-Daten** – Ruft Registrar-, Erstellungs- und Ablaufdaten, Nameserver sowie E-Mail-Kontaktinformationen ab.
- **DNS-Auflösung** – Löst eine Domain zu ihren IP-Adressen und Aliasen auf.
- **IP-Geolokalisierung** – Nutzt ip-api.com, um Geostandort-, ISP- und Organisationsdaten abzurufen.
- **Server-Fingerprints** – Untersucht HTTP-Header auf Informationen über Server-Software und verwendete Technologien.
- **Shodan-Hostberichte** – Fragt die Shodan-API nach offenen Diensten, Ports und potenziellen Schwachstellen ab (erfordert einen API-Schlüssel).

## Shodan-API-Informationen

Für diese Funktion wird ein **Shodan-API-Schlüssel** benötigt.
Leider wurde dieser Teil etwas zu komplex für mich, und da ich nicht blind Inhalte von ChatGPT übernehme,
bleibt der Abschnitt zu den Shodan-Hostberichten derzeit etwas unzuverlässig und experimentell.

## Screenshots

![Example 1](imgs/pic1.PNG)

![Example 2](imgs/pic2.PNG)

![Example 1](imgs/pic3.PNG)

![Example 2](imgs/pic4.PNG)

![Example 2](imgs/pic5.PNG)
