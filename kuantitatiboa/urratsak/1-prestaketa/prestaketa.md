---
title: 1. Datuen Prestaketa
subtitle: Datuak garbitzen eta txukuntzen
subject: Analisi Kuantitatiboa
---

Edozein analisi estatistiko sakon egin aurretik, gure datu-multzoa prestatzea eta garbitzea ezinbestekoa da. Askotan, urrats hau ikerketaren garapenean pauso garrantzitsuenetako bat izan ohi da, datu garbi batzuk gabe emaitza faltsuak edota erroreak lortuko genituzke eta.

## Zer da datuen prestaketa?

Datuak txukuntzean oinarritzen den lehen fasea da. Fitxategia Excel (`.csv`), SPSS (`.sav`) edota Jamovi (`.omv`) formatuan egon, arreta berezia jarri behar diogu aldagaien konfigurazioari:

1. **Aldagai motak zehaztu**: Ziurtatu aldagai nominalak (adib. Generoa) edo jarraituak (adib. Nota) zuzen definituta daudela zure softwarean. Honela, softwareak azterketa desberdin egokiak aplikatuko dizkio bakoitzari.
2. **Missing data (datu faltak)**: Batzuetan partaideek ez dute galdera bat erantzuten. Zure softwareari (adibidez Jamovi-ri) hutsune horiek iragazkia erabiliz aurkitzeko edota errore barik irakurtzeko ezarpenak konfiguratu behar dituzu.
3. **Kategorien kodeak (balioak)** eta dummy aldagaiak: Aldagai kategorikoetan (adib. 1 = Emakumea, 2 = Gizona), ezinbestekoa da balio edo label-ak ondo definitzea, gero sortzen diren taulak eta grafikak behar bezala interpretatu ahal izateko. Gainera, kasu batzuetan—bereziki erregresioak edo analisi inferentzial aurreratuak egiteko—aldagai kategorikoak dummy aldagai bihurtu behar dira, hau da, 0 eta 1 balioak hartzen dituzten aldagai bitarretan. Esaterako, "Ikastetxe mota" (Publikoa/Pribatua/Itundua) aldagaitik "Ikastetxe_Publikoa" bezalako aldagai bat sor daiteke (0 = Ez, 1 = Bai), prestaketa fasean softwareko Compute edo Transform funtzioak erabiliz, jatorrizko datuak galdu gabe.

> [!TIP] Zure datuak irekitzeko orduan
> Jamovi edo SPSS erabiltzerakoan, beti berraztertu aldagaien *Data Setup* interfazea grafiko bat sortu baino lehen! Datuak ondo sailkatuz gero, beste dena automatikoa izango da.

Behin datuak prest edukita, bigarren pausura joan gaitezke: datuen argazki finko bat egitera (analisia deskribatzailea).
