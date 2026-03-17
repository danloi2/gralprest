---
title: Nire aldagaia normaltasunaren irizpideak betetzen ditu?
subtitle: Banaketaren forma eta normaltasunaren azterketa
subject: Analisi Deskribatzailea
site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
---


## **Banaketaren forma**

**Definizioa:** Datuen banaketa “forma” aztertzea, asimetria eta kurtosia kontuan hartuta.

- Asimetria: ±2 balio normala
    
- Kurtosia: ±2 balio normala
    

**Praktika gida:**

- Analyses → Descriptives → Plots → check **Skewness, Kurtosis**
    
- Ikusi `akad_ikasketa_orduak` datuak normala diren
    

> [!NOTE]
> Banaketaren formari dagokionez, `akad_ikasketa_orduak` aldagaiak normaltasun-irizpideak betetzen dituela frogatzen da. **Asimetria-indizea -0.016 da** (E.E. = 0.221), eta horrek aldagaiak simetria ia perfektua duela adierazten du, batez bestekoaren inguruan orekatuta baitago. Bestalde, **kurtosi-balioa -0.710 da** (E.E. = 0.438); balio negatibo honek banaketa platikurtiko arin bat iradokitzen duen arren (kanpaina normal estandarra baino zertxobait zapalagoa), adierazlea onartutako tarteen barruan dago. Estatistikoki, bi indizeak **±1.96 tartearen barruan** egoteak (konfiantza-maila altuarekin) banaketa normalaren hipotesia babesten du. Datu hauek, lehen ikusitako histograma eta Q-Q plot-arekin batera, laginaren izaera parametrikoa berresten dute.

## **Normaltasunaren azterketa**

> [!NOTE] Normalaltasuna
> Parametrikoak erabili aurretik datuak normalak direla ziurtatzea.
> 
> - Histogramak + Normal Curve
>     
> - Test estatistikoak: Shapiro-Wilk (n<50) edo Kolmogorov-Smirnov (n>50)

    

Hipotesiak:

- H₀ → datuak normalak dira
    
- H₁ → datuak ez dira normalak
    

Interpretazioa:

- p > 0.05 → normalitatea → **proba parametrikoak erabil daitezke**
    
- p < 0.05 → ez normalak → **proba ez-parametrikoak gomendagarria**
    

**Praktika gida:**

- Analyses → Descriptives 
- `pre_matematika_nota`, `post_matematika_nota` eta `aka_ikasketa_orduak`

> [!NOTE]
> Datuen analisi deskriptiboak eta normaltasun-testek (`Shapiro-Wilk`) erakusten dute aztertutako hiru aldagaiak banaketa normalaren barruan kokatzen direla. Zehazki, `pre_matematika_nota` ($p = .454$), `post_matematika_nota` ($p = .769$) eta `akad_ikasketa_orduak` ($p = .204$) aldagaietan lortutako p-balioak 0.05eko esangurantz-mailatik gora daude, banaketa parametrikoa berretsiz.
