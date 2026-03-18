---
title: 3. Zeintzuk dira analisi parametrikoak egiteko aurrebaldintzak?
subtitle: Normaltasuna, Formak eta Homozedastizitatea
subject: Analisi Kuantitatiboa
site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
---


## **1. Banaketaren forma**

**Definizioa:** Datuen banaketa “forma” aztertzea, asimetria eta kurtosia kontuan hartuta.

- Asimetria: ±2 balio normala

- Kurtosia: ±2 balio normala


**Praktika gida:**

- Analyses → Descriptives → Plots → check **Skewness, Kurtosis**

- Ikusi `akad_ikasketa_orduak` datuak normala diren


> [!NOTE]
> Banaketaren formari dagokionez, `akad_ikasketa_orduak` aldagaiak normaltasun-irizpideak betetzen dituela frogatzen da. **Asimetria-indizea -0.016 da** (E.E. = 0.221), eta horrek aldagaiak simetria ia perfektua duela adierazten du, batez bestekoaren inguruan orekatuta baitago. Bestalde, **kurtosi-balioa -0.710 da** (E.E. = 0.438); balio negatibo honek banaketa platikurtiko arin bat iradokitzen duen arren (kanpaina normal estandarra baino zertxobait zapalagoa), adierazlea onartutako tarteen barruan dago. Estatistikoki, bi indizeak **±1.96 tartearen barruan** egoteak (konfiantza-maila altuarekin) banaketa normalaren hipotesia babesten du. Datu hauek, lehen ikusitako histograma eta Q-Q plot-arekin batera, laginaren izaera parametrikoa berresten dute.


## **2. Normaltasunaren azterketa**

> [!NOTE] Normaltasuna
> Parametrikoak erabili aurretik datuak normalak direla ziurtatzea.
>
> - Histogramak + Normal Curve
>
> - Test estatistikoak: Shapiro-Wilk (n<50) edo Kolmogorov-Smirnov (n>50)



Hipotesiak:

- H₀ → datuak normalak dira

- H₁ → datuak ez dira normalak


Interpretazioa:

- p > 0.05 → normalitatea → **proba parametrikoak erabili ditzakegu**

- p < 0.05 → ez normalak → **proba ez-parametrikoak erabiltzea gomendagarria da**


**Praktika gida:**

- Analyses → Descriptives
- `pre_matematika_nota`, `post_matematika_nota` eta `aka_ikasketa_orduak`

> [!NOTE]
> Datuen analisi deskriptiboak eta normaltasun-testek (`Shapiro-Wilk`) erakusten dute aztertutako hiru aldagaiak banaketa normalaren barruan kokatzen direla. Zehazki, `pre_matematika_nota` ($p = .454$), `post_matematika_nota` ($p = .769$) eta `akad_ikasketa_orduak` ($p = .204$) aldagaietan lortutako p-balioak 0.05eko esangurantz-mailatik gora daude, banaketa parametrikoa berretsiz.


## **3. Bariantzen Homogeneotasuna (Levene Testa)**

Beste aurrebaldintza garrantzitsu bat (bereziki taldeak konparatzen direnean, adibidez T-test edo ANOVA batean) **bariantzen homogeneotasuna** da.

Parametrikoak berme osoz erabiltzeko, taldeen arteko bariantzak (sakabanaketak) antzekoak izan behar dira. Honi **Homozedastizitatea** deitzen zaio. Bariantzak oso desberdinak badira, ordea, **Heterozedastizitatea** dugu, eta kasu horietan ezin dira proba estatistiko estandarrak (Student-en T, adibidez) bere horretan aplikatu, egokitzapen matematikoak egin gabe (adibidez, Welch-en T kontrastea erabiliz).

**Levene-ren Testa** da hau egiaztatzeko probarik erabiliena eta ezagunena.

Hipotesiak:
- H₀ → Bariantzak berdinak dira (Homozedastizitatea badago)
- H₁ → Bariantzak ezberdinak dira (Heterozedastizitatea daukagu)

Interpretazioa:
- p > 0.05 → Homozedastikoak → **Proba parametriko estandarrak erabili ditzakezu** (Bariantzak berdinak direla onartzen duzu).
- p < 0.05 → Heterozedastikoak → **Welch zuzenketa edo proba ez-parametrikoak erabili behar dituzu** (Normalean jamovik, `Assumption Checks` atalaz gain, `Welch's` laukitxoan klikatzeko aukera ematen dizu datuak berdintzeko).

**Praktika gida:**
- T-test edo ANOVA bat egitean Jamovin, beti markatu datuen *Assumption Checks* atalean dagoen **Homogeneity tests**.
