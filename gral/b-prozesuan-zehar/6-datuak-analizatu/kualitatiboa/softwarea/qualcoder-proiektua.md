---
title: "QualCoder erabiltzen: Proiektuaren fluxua"
subtitle: Pausoz pausoko gida praktikoa
subject: QualCoder
---

## QualCoder erabiltzen: Proiektuaren fluxua

Analisi kualitatiboa egiteko, QualCoder-en proiektu berri bat sortuko dugu eta dataset-eko fitxategiak sartuko dugu.

```{admonition} Beharrezkoa: dataset-a deskargatu
:class: important
Hasi aurretik, {download}`Dataset osoa <../../assets/data/kualitatiboa/dataset-kualitatiboa.md>` deskargatu edo banakako fitxategiak. Beherago dituzue eskaerak:

- {download}`Elkarrizketa 1 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir01.md>` · {download}`Elkarrizketa 2 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir02.md>` · {download}`Elkarrizketa 3 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir03.md>`
- {download}`Gelako egunkaria <../../assets/data/kualitatiboa/20260105-egunkaria-ikerlaria.md>`
- {download}`Programazio didaktikoa <../../assets/data/kualitatiboa/2026-documentua-programazioa-didaktikoa-matematika-lh6.md>`
```

---

## 1. Proiektua sortu

1. Joan `Project` > `New Project`.
2. Aukeratu karpeta bat eta jarri izena, adib: `gral-analisia.qd`.

## 2. Project Memo (Proiektuaren oharra)

Fitxategiak sartu aurretik, komeni da ikerketaren helburu orokorra bat ezartzea. Bereziki IA erabili behar baduzu, garrantzitsua da tresnari "testuingurua" ematea **Project Memo** erabiliz.

1. Joan `Project` → `Project Memo`
2. Idatzi zure ikerketaren laburpen laburra (1-2 esaldi).

```{admonition} Adibidea
:class: tip
*"Ikerketa honek metodologia aktiboen eragina aztertzen du ikasleen parte-hartzean Lehen eta Haur Hezkuntzan. Hiru elkarrizketa, gelako egunkari bat eta programazio didaktiko bat aztertuko ditugu."*
```

## 3. Fitxategiak inportatu

1. Joan `Files and Cases` > `Manage files`.
2. Sakatu 📄+ eta hautatu deskargatutako fitxategiak.
3. Eman izen garbi eta koherenteak fitxategiei (ikus {ref}` nomenklatura-arauak<3-datuen-antolaketa-fitxategien-izenak>`):
`2026-elkarrizketa-ir01`, `20260105-egunkaria-ikerlaria`, `2026-documentua-programazioa`.

## 4. Kodeak sortu

1. Joan `Codes` > `Manage codes`.
2. Sakatu ➕ eta idatzi lehen kodeak, adib: `motibazioa`, `parte-hartzea`, `talde-lana`.

```{admonition} Aholkua
:class: tip
Kode bakoitzari kolore ezberdina jar diezaiozu, analisian errazago aurkitzeko.
```

## 5. Testua kodifikatu

1. Joan `Coding` > `Code text`.
2. Aukeratu fitxategi bat ezkerreko zerrendan.
3. Hautatu testu zati esanguratsua saguarekin.
4. Klik egin kodearen izena eskuineko zerrendan.

## 6. Kategoriak antolatu

Kode asko sortu ondoren, arrastatu kode bat beste baten gainera zuhaitz-egitura sortzeko.

## 7. Txostenak atera

1. Joan `Reports` > `Coding reports`.
2. Hautatu kodeak eta sakatu "Run".
3. Esportatu behar baduzu: `.html` edo `.csv`.

> [!IMPORTANT] Segurtasun kopia
> QualCoder-ek datuak automatikoki gordetzen ditu, baina komeni da proiektuaren karpetaren kopia bat egitea noizean behin.
