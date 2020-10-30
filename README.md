# Initialisierung
Installation leere Datenbank demo leer.zip im Portal odoo.mintsys.ch 
Import res.users.xls
Import product.template.xls
Import mrp.bom
Import mrp.workcenter.xls
Installation App "Kontakte"
Import res.partner
Arbeitsplan für *Oberrohr" und *Rahmen unbeschichtet* erstellen
Mengen für die Bestandteile des Rahmens anpassen
Lieferanten für die Produkte für den Rahmen hinterlegen
Diese Inhalte finden sich in der Datenbank demo 1.zip
**In den XLSX-Dateien dürfen keine Werte 0 enthalten. z.B. Abteilung mit Wert 0**


# Demo Fahrrad

Beschreibung zum Demo-Datensatz.

# Verkauf

Produkt: Fahrrad
Dienstleistung: Entwicklung - 150.00/CHF

# Fertigung

Es steht ein Produkt Fahrrad zur Produktion bereit.

Die Komponente Sattelstütze wird beim Lieferanten eingekauft.

# Kontakt

Lieferant: BWB-Betschart AG

Kunde: Veloplus

# Einkauf

Die Komponente Sattelstütze kann beim Lieferanten beschafft werden.

# Projekt

Aus dem Entwicklungsprojekt kann ein Verkausauftrag erstellt werden.

Das Entwicklungsprojekt ist mit einer Kostenstelle verknüpft.

# Benutzer / User
*Dateiname: res.users.xls*
Folgende Benutzer sind Admin:
- Administrator 
- Christian Huber

Jeder Benutzer ist auch als Personal erfasst

# Personal
*Dateiname: hr.employee.xlsx*
Folgendes Personal mit diesen Rollen sind erfasst:
- **Peter Wernermann CEO (Rolle Verkauf und Projekte)**

*Abteilung Administration:*
- **Hildegard Rufener (Rolle Finanzen und Verkäufe)**
- Jens Stolte (Rolle Web-Administrator)
- Martina Schlegel (Rolle Finanzen)
- Peter Wernermann CEO (Rolle Verkauf und Projekte)
- Yvonne Halter-Brunner (Rolle Finanzen, Personal)

*Abteilung Projekte:*
- **Christian Huber (Rolle Projekte/Produktion, Leiter Produktion)**
- Theo Altermatt (Rolle HR und Projekte)
- Hans Durrer (Rolle Projekte/Produktion)
- Franziska Schmid (Rolle Projekte/Produktion)

*Abteilung Sales:*
- **Inge Riis (Rolle Verauf, Leiterin Verkauf)**
- Hans Meier (Rolle Verkauf)
- Thomas Lauener (Rolle Verkauf)

*Benutzer Mint System*
- Kurt Gisler (Rolle Administrator)
- Janik von Rotz (Rolle Administrator)
- Marco Roeleven (Rolle Administrator)
- admint (Rolle Administrator)

## Personal, import der Adressen je Mitarbeiter
*Dateiname: hr.adress_home.xlsx* 


# Erfassen der Mitarbeiter, muss bei Verwendung des App Anwesenheitszeiten zwingend Benutzer sein




# Anwesenheitszeiten
*Unter Einstellungen den Wert bei An-/Abmeldung mit PIN auf True setzen* 


# Abwesenheitszeiten
*Dateiname: hr.leave.type.xlsx*

Vor dem Import der Feriensaldos müssen unter Konfiguration > die Abwesenheitstypen erfasst sein:
- Bezahlter Urlaub /Ferien
- Krankheit
- Ausgleichstage
- Unbezahlte Ferien
- Militär
- Zivilschutz
- Mutterschaftsurlaub
- Vaterschaftsurlaub

Die Genehmigung der Abwesenheit erfolgt immer durch den Teamleiter.



