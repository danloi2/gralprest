---
title: Zertan datza analisi kuantitatiboa?
subtitle: Deskribatzailea eta Inferentziala
subject: Analisi Kuantitatiboa

site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
---

**Estatistika** da analisi kuantitatiboaren ardatz nagusia; analisi hau **errealitatea ikertzeko tresna** bat da, **datu zenbakigarriak** neurtu, prozesatu eta inferentziak egitean oinarritzen dena. 

## Populazioa eta Lagina

Estatistikan errealitatea ulertzeko bi kontzeptu ulertu behar dira: 

::: {glossary}

**Populazioa**  
: Ikerketa batean aztertzen den **multzo osoa edo kolektiboa** da. Adibidez, ikastetxe bateko **ikasle guztiak** populazioa dira, zure ikerketan guztien datuak kontuan hartzen bagenu bezala.

**Lagina**  
: {term}`Populazioa`ren **zati ordezkari bat** da, datuak bildu eta **ondorioak ateratzeko** erabiltzen dena.  

:::

:::{tip} Adibide {term}`lagina` (GRAL): 30 Ikasleren Notak
Ikastetxe bateko 30 ikasleren notak {term}`lagina` dira, ikastetxe osoaren emaitzak estimatzeko.
:::

:::{important} Ideia nagusia
{term}`Populazioa`ren eta {term}`Lagina`ren arteko erlazioa:
- {term}`Populazioa` → **guztia**, zuzeneko informazio guztia  
- {term}`Lagina` → **zati bat**, praktiko eta aztertzeko erraza, ondorioak ateratzeko erabiltzen dena
:::

## Analisi Kuantitatiboaren Urratsak

Analisi kuantitatibo on bat egiteko, estatistika bi adarretan banatzen da prozesu ordenatu bat jarraituz. GRAL baterako, hauek dira pauso nagusiak:

### 1. Urratsa: Datuen Prestaketa
Datuak softwarean (Jamovi, SPSS) sartu aurretik, ondo antolatu behar dira. Aldagaiak definitzea, falta diren datuak (missing values) kudeatzea eta formatua (adibidez `.csv` edo `.sav`) egokia dela ziurtatzea da lehen pausoa.

### 2. Urratsa: Analisi Deskribatzailea

Lehen fase estatistikoa beti da lortutako datuak arakatu eta deskribatzea (nola banatzen diren, balio atipikorik badagoen...). 

::: {glossary}

**Estatistika deskribatzailea**
: Datuak **laburbiltzeko, deskribatzeko eta modu ulergarrian aurkezteko** erabiltzen da. Datu-multzoak bildu, sailkatu eta irudikatzeaz arduratzen da, haien ezaugarri nagusiak aztertzeko (batezbestekoa, mediana, moda edo histogramak). Bere helburu nagusia lortutako datuen "argazki" bat eskaintzea da, **laginetik haratago orokortzeko asmorik gabe**.

:::

:::{tip} Adibide Deskribatzailea (GRAL): Ikasgelako motibazio-maila
* **Testuingurua:** Galdesorta bat pasatu diezu zure gelako 25 ikasleei.
* **Analisi deskribatzailea:** Kalkulatu duzu batezbestekoa (6,5) eta barra-diagrama bat egin duzu.
* **Emaitza:** "Nire gelako ikasleen % 60ak 7tik gorako motibazioa du".
:::

### 3. Urratsa: Aurrebaldintzak eta Banaketen Analisia

Inferentzietara pasa aurretik (hau da, proba estatistiko sendoak egin aurretik), datuek irizpide batzuk betetzen dituztela ziurtatu behar da. Garrantzitsuenak **normaltasuna** (Shapiro-Wilk) eta **bariantzen homogeneotasuna** (Levene) dira. Homozedastikotasunik ez badago, proba ez-parametrikoak edota parametro zuzenduak (Welch) erabili beharko dira.

### 4. Urratsa: Analisi Inferentziala

Behin datuak ezagututa, hurrengo urratsa hipotesiak ebaluatzeko eta emaitzak populazio osora estrapolatzeko erabiltzen da.

::: {glossary}

**Estatistika Inferentziala**  
: Lagin baten datuetatik abiatuta populazio osoari buruzko ondorioak ateratzen dituen adarra da. Helburua **laginaren informazioa orokortzea**, parametroak estimatzea eta hipotesiak probatzea da.

:::

:::{tip} Adibide Inferentziala (GRAL): Gamifikazioaren eragina ikasgelan
* **Testuingurua:** Metodologia tradizionala gela batean eta gamifikazioa beste batean aplikatu duzu.
* **Analisi inferentziala:** *T-test* bat aplikatzen duzu bi taldeen arteko aldea esanguratsua den ikusteko.
* **Emaitza:** "Gamifikazioarekin lortutako hobekuntza ez da kasualitatea izan; beraz, metodo hau LHko edozein ikasgelatan aplikatuta emaitza hobeak lortuko liratekeela ondorioztatzen da".
:::

---

## Dataset-a (Praktikatzeko Materialari Sarbidea)

Ondorengo fitxategiak erabiliko ditugu adibide gisa analisi kuantitatiboa ikasteko. Zuzenean deskargatu ditzakezu ordenagailura zure software estatistiko gogokoenean irekitzeko:

- 📊 {download}`Dataset Kuantitatiboa (CSV formatuan - Excel edo antzekoetarako) <../assets/data/kuantitatiboa/dataset-kuantitatiboa.csv>`
- 📊 {download}`Dataset Kuantitatiboa (SAV formatuan - SPSS edo Jamovirako) <../assets/data/kuantitatiboa/dataset-kuantitatiboa-kappa.sav>`
