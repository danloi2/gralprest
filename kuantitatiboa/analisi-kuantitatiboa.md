---
title: Analisi Kuantitatiboa
subtitle: Zenbakiekin Jolasean
subject: Analisi Kuantitatiboa
# epigraph: No funciona
# abstract: Resumen corto
# summary: Texto facilitado
# dedication: Abcabc
# acknowledgments: Jesús Valverde
# keypoints: Metodología, Investigación Educativa, Trabajo Fin de Máster, Programa. 
site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
downloads:
  - file: ../assets/data/01-datuak.xlsx
    title: adibide-datuak analizatzeko
  - file: ../assets/pdf/2020-galindo.pdf
    title: Estadística para no estadísticos (Galindo, 2020)
---

# Analisi kuantitatiboa

> [!WARNING] Atal kuantitatiboaren helburua
> *Hezkuntzako zenbakizko datu sinpleak analizatzea Jamovi erabiliz*.

## 1.- Zer da analisi kuantitatiboa? (10 min)

**Zertarako erabiltzen den estatistika ikerketan?**.

Laburbilduz:

**Estatistika bi adar nagusitan banatzen da:**

> [!NOTE] Estatistika deskribatzailea
> → Datuak **laburbiltzeko eta deskribatzeko** erabiltzen da.
    
Adibidea:  
Ikastetxe bateko ikasleen azterketako notak aztertzea:

- batezbestekoa
- mediana
- moda
- histogramak
    
> [!NOTE] Estatistika inferentziala
> → **Lagin batetik populazioari buruzko ondorioak ateratzeko** erabiltzen da.


Adibidea:  
30 ikasleren notak erabiliz ikastetxe osoaren batezbestekoa estimatzea.

💡 Ideia nagusia:

- Deskribatzailea → **zer gertatu den azaldu**
    
- Inferentziala → **ondorioak atera**

Info: [[estatistika-motak]]
## 2.- Aldagai motak (15 min)

Ikasleek estatistikan **aldagai motak identifikatzen ikasi behar dute**.

### 2.1.- Datu motaren arabera

#### 2.1.1.- Kategorikoak

> [!NOTE] Kategorikoak
> Balioak kategoriak dira.

> [!NOTE] Nominalak
> - ordenarik ez
> - adib: ikasgaia

> [!NOTE] Ordinalak
> - ordena dago baina distantzia ez  
> - adib: gogobetetze maila
    
#### 2.1.2.- Zenbakizkoak

> [!NOTE] Zenbakizkoak
> Balio kuantitatiboak.

> [!NOTE] Diskretuak
> - zenbaki osoak
> - adib: ikasle kopurua

> [!NOTE] Jarraituak
> - edozein balio hartu dezake
> - adib: azterketa-denbora
    
### 2.2.- Funtzioaren arabera

#### 2.2.1.- Menpeko aldagaia

> [!NOTE] Menpeko aldagaia
> Aztertzen den emaitza.
> Adib: azterketako nota
    
#### 2.2.2.- Independentea

> [!NOTE]
> Eragina izan dezakeen faktorea.
> 
> Adib:  ikasketa-metodoa
   
#### 2.2.3.- Koaldagaia

> [!NOTE] Koaldagaia
> Eragina kontrolatzeko erabiltzen den aldagaia.
> 
> Adib: aurreko ezagutzak
  
#### 2.2.4.- Mediatzailea

> [!NOTE] Aldagai Mediatzailea
> Independenteak menpekoan duen eragina **bitartekaritzen du**.
> 
> Adib: ikasketa-estrategiak

#### 2.2.5.- Moderatzailea

> [!NOTE] Aldagai Moderatzailea
> Aldagaien arteko erlazioa **indartu edo ahuldu** dezake.
> 
> Adib: motibazioa

Info: ![[aldagaiak.svg]]
## 3.- Softwarea: SPSS vs JAMOVI (10 min)

Gomendioa: **JAMOVI erabiltzea**.

| Softwarea | Ezaugarriak                                                   |
| --------- | ------------------------------------------------------------- |
| SPSS      | Tradizionala baina ordainpekoa                                |
| JAMOVI    | Doakoa, intuitiboa eta automatikoki eguneratzen ditu emaitzak |
### 3.1.- Deskargatu eta Konfiguratu

 https://www.jamovi.org/
 Hiru puntuak; Hizkuntza
### 3.2.- Aldagaiak izendatzeko urrezko arauak

**1. Beti letra batekin hasi**

Aldagai baten izena **inoiz ez da zenbaki batekin hasi behar**.

❌ Okerra  
`1adina`  
`2024_notak`

✅ Zuzena  
`adina`  
`nota_finala`

**Zergatik?**  
Programa estatistiko askok zenbaki batekin hasten diren izenak **balio matematiko edo errore gisa interpreta ditzakete**.

**2. Espaziorik EZ erabili**

Aldagaien izenetan **ezin dira espazioak erabili**.

❌ Okerra

`ikasle adina`  
`nota media`  
`ikasketa orduak`

✅ Zuzena

`ikasle_adina`  
`nota_media`  
`ikasketa_orduak`

💡 **Irtenbidea:**  
Erabili **beheko gidoia (_)** hitzak bereizteko.

**3. Ez erabili karaktere berezirik**

Karaktere bereziek arazoak sor ditzakete programa estatistikoetan.

❌ Okerra

`nota%`  
`urteañ`  
`motibazioa?`  
`nota-finala`

✅ Zuzena

`nota`  
`urtea`  
`motibazioa`  
`nota_finala`

Saihestu bereziki:

- `ñ`
    
- azentuak (`á é í ó ú`)
    
- ikurrak (`% ? ! / -`)

**4. Aurrizkiak (prefijoak) erabiltzea**

Praktika oso gomendagarria da **aurrizkiak erabiltzea**, aldagaien mota identifikatzeko.

Horrela, datu-basea **asko errazago interpretatzen da**.

 * **Datu demografikoak**

Aurrizkia: `dem_`

Adibideak:

`dem_adina` → ikaslearen adina  
`dem_sexua` → ikaslearen sexua  
`dem_herrialdea` → jatorrizko herrialdea  
`dem_maila` → ikasketa maila edo ikasturtea

* **Datu akademikoak**

Aurrizkia: `akad_`

Adibideak:

`akad_matematika_nota`  
`akad_euskara_nota`  
`akad_batezbestekoa`  
`akad_ikasketa_orduak`

* **balorazio edo eskala aldagaiak**

Aurrizkia: `val_`

Normalean **Likert eskalak** erabiltzen dira (1–5 edo 1–7).

Adibideak:

`val_motibazioa`  
`val_interesa`  
`val_gogobetetasuna`

Adibidez eskala:

| Balioa | Esanahia  |
| ------ | --------- |
| 1      | Oso baxua |
| 2      | Baxua     |
| 3      | Ertaina   |
| 4      | Altua     |
| 5      | Oso altua |

* **Interbentzio aurreko eta ondorengo neurketak**

Aurrizkiak:

`pre_` → interbentzioaren aurretik  
`post_` → interbentzioaren ondoren

Adibideak:

`pre_matematika_nota`  
`post_matematika_nota`

`pre_motibazioa`  
`post_motibazioa`

Horrela azter daiteke **programa edo metodologia batek eragina izan duen ala ez**.

**5.  Adibide osoa: Hezkuntza ikerketa batean erabil daitezkeen aldagaiak**

> [!NOTE] Adibidea
> Imajinatu ikerketa bat non aztertu nahi den ikasketa-metodo berri batek ikasleen errendimendua eta motibazioa hobetzen duen ala ez

-

*  **Aldagai demografikoak**

| Aldagaia       | Deskribapena          | Mota        |
| -------------- | --------------------- | ----------- |
| dem_sexua      | ikaslearen sexua      | nominala    |
| dem_adina      | ikaslearen adina      | zenbakizkoa |
| dem_herrialdea | jatorrizko herrialdea | nominala    |
| dem_maila      | ikasturtea            | ordinala    |

* **Aldagai akademikoak**

| Aldagaia             | Deskribapena                 | Mota        |
| -------------------- | ---------------------------- | ----------- |
| akad_ikasketa_orduak | astean ikasten dituen orduak | zenbakizkoa |
| akad_matematika_nota | matematikako nota            | zenbakizkoa |
| akad_euskara_nota    | euskarako nota               | zenbakizkoa |
| akad_batezbestekoa   | batez besteko nota           | zenbakizkoa |

* **Eskala psikopedagogikoak**

Likert eskala (1-5):

| Balioa | Esanahia    |
| ------ | ----------- |
| 1      | Oso desados |
| 2      | Desados     |
| 3      | Neutrala    |
| 4      | Ados        |
| 5      | Oso ados    |

Aldagaiak:

`val_motibazioa`  
`val_interesa`  
`val_autoefikazia`

* **Interbentzio aurretik eta ondoren**

| Aldagaia             | Deskribapena                    |
| -------------------- | ------------------------------- |
| pre_matematika_nota  | programaren aurreko nota        |
| post_matematika_nota | programaren ondorengo nota      |
| pre_motibazioa       | motibazioa programaren aurretik |
| post_motibazioa      | motibazioa programaren ondoren  |

## 4.- **Aldagai bakarreko estatistika deskribatzailea (20 min)**

> **Helburua:** Datu multzo bat **laburbiltzea eta deskribatzea**.

### 4.1.- **Maiztasun taulak**

> [!NOTE] Maiztasun taulak
> Aldagai kategorikoen balioak zenbat aldiz agertzen diren erakusten duten taulak.
> 
> - Adib: `dem_sexua`, `pref_irakasgaia`, `metodoa`
>     
> - Parametroak: maiztasuna, portzentajea
>     
> - Jamovi: **Análisis** → Exploración → Frecuencias**

**Praktika gida:**

1. Hautatu `dem_sexua`
    
2. Markatu **Tablas de frecuencias**
    
3. Aztertu, zein generok nagusi den

| Frequencias de dem_sexua |           |             |               |
| ------------------------ | --------- | ----------- | ------------- |
| dem_sexua                | Recuentos | % del Total | % Acumulativo |
| E                        | 50.0      | 41.7%       | 41.7%         |
| M                        | 70.0      | 58.3%       | 100.0%        |

> [!NOTE]
> Ikerketa honetan 120 ikaslek parte hartu dute, eta ez dago balio galdurik. Ikasleen artean, mutilak % 58,3 dira, eta neskak % 41,7.

### 4.2.- **Grafikoak**

> [!NOTE]
> Datuen banaketa eta erlazioak ikusizko moduan azaltzeko tresnak.
> 
> - Histogramak: `akad_ikasketa_orduak`, `pre_matematika_nota`, `post_matematika_nota`
>     
> - Barra-diagramak: `dem_sexua`, `metodoa`
>     
> - Grafiko zirkularrak: `pref_irakasgaia`

    

**Praktika gida:**

1. Hautatu `akad_ikasketa_orduak`
    
2. Sortu **Histograma + Normaltasuna + Q-Q**
    
3. Aztertu banaketa: simetrikoa ala ez
    

> [!NOTE]
> Asteko ikasteko orduak (akad_ikasketa_orduak) aldagaia aztertzean, datuek banaketa gutxi gorabehera normalari jarraitzen diotela ikusten da. Histogramak egitura kanpatua eta nahiko simetrikoa erakusten du, astean 6-10 orduko ikasle-kontzentrazio handienarekin. Joera hori sendo berresten da Q-Q plot grafikoan, non puntu gehienak (hondakin estandarizatuak) zuzenean erreferentziako lerro diagonalaren gainean kokatzen diren. Muturretan (banaketa-kolak) desbideratze txiki batzuk ikusten badira ere, batez ere beheko mugan, ez dirudi normaltasun-kasua baztertzeko bezain esanguratsuak direnik, eta horrek iradokitzen du lagin hori egokia dela proba estatistiko parametrikoak egiteko.

### 4.3.- **Joera zentrala**

> [!NOTE] Joera Zentrala
> Datuen “zentroa” edo ohiko balioa adierazten duen neurri estatistikoa.
> 
> - Batezbestekoa: datu guztiak batuta banaketa kopurura zatituta
>     
> - Mediana: datu erdiko balioa
>     
> - Moda: gehien agertzen den balioa
>     
> - Adib: `akad_ikasketa_orduak` → batezbestekoa = 6 ordu, mediana = 5 ordu, moda = 4 ordu
  
**Praktika gida:**

- Análisis → Exploración → Descriptivas
    
- Hautatu `post_matematika_nota`
    
- Markatu **Media, Mediana, Moda**

> [!NOTE]
> Interbentzioaren ondoren, post_matematika_oharra aldagaiak banaketa oso orekatua erakusten du. Batezbestekoaren (70.9) eta medianaren (70.6) arteko hurbiltasunak datuen simetria handia iradokitzen du, emaitzak alboratu ditzaketen ezohiko balioak (outlierrak) alde batera utzita. Era berean, moda (74.2) erdiko joera baino zertxobait gorago dago, eta horrek adierazten du errendimendu ohikoena nabarmenaren tartean kokatzen dela, eta laginaren gehiengoa ($N = 120$) lorpen akademiko positiboko maila batean sendotzen dela.

### 4.4.- **Dispertsioa**

**Definizioa:** Datuen banaketa edo bariazio neurtzen du.

- Minimoa, maximoa, desbideratze tipikoa, bariantza  
    💡 Praktika: Desbideratze tipikoa handia bada, batezbestekoak **ez du fidagarritasun handirik**
    

**Praktika gida:**

- Analyses → Descriptives
    
- Hautatu `post_matematika_nota`
    
- Markatu **SD, Variance, Minimum, Maximum, Hedadura**
    

> [!NOTE]
> Aldakortasunari dagokionez, `post_matematika_nota` aldagaiak 10.9ko desbideratze tipikoa eta 119ko varianza erakusten ditu. Datu hauek adierazten dute ikasleen arteko aldeak moderatuak direla eta lagina nahiko kohesionatuta dagoela, nahiz eta banakako diferentziak egon. Laginaren hedadura edo rangoa 52.6 puntukoa da (46.3tik 98.9ra), eta horrek erakusten du ebaluazio-tresnak gaitasuna izan duela errendimendu desberdinak atzemateko, inolako datu galdu gabe ($N=120$).

### 4.5.- **Banaketaren forma**

**Definizioa:** Datuen banaketa “forma” aztertzea, asimetria eta kurtosia kontuan hartuta.

- Asimetria: ±2 balio normala
    
- Kurtosia: ±2 balio normala
    

**Praktika gida:**

- Analyses → Descriptives → Plots → check **Skewness, Kurtosis**
    
- Ikusi `akad_ikasketa_orduak` datuak normala diren
    

> [!NOTE]
> Banaketaren formari dagokionez, `akad_ikasketa_orduak` aldagaiak normaltasun-irizpideak betetzen dituela frogatzen da. **Asimetria-indizea -0.016 da** (E.E. = 0.221), eta horrek aldagaiak simetria ia perfektua duela adierazten du, batez bestekoaren inguruan orekatuta baitago. Bestalde, **kurtosi-balioa -0.710 da** (E.E. = 0.438); balio negatibo honek banaketa platikurtiko arin bat iradokitzen duen arren (kanpaina normal estandarra baino zertxobait zapalagoa), adierazlea onartutako tarteen barruan dago. Estatistikoki, bi indizeak **±1.96 tartearen barruan** egoteak (konfiantza-maila altuarekin) banaketa normalaren hipotesia babesten du. Datu hauek, lehen ikusitako histograma eta Q-Q plot-arekin batera, laginaren izaera parametrikoa berresten dute.

### 4.6.- **Normaltasunaren azterketa (10 min)**

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
> 

## 5.- **Bi aldagairen arteko analisia (20 min)**

### 5.1.- Aldagai kategorikoak

#### 5.1.1.- Taula gurutzatuak

> [!NOTE] Taula gurutzatuak
> **Bi aldagai kualitatiboren** (kategorialen) arteko erlazioa aztertzeko
> - Adib: `dem_sexua` × `pref_irakasgaia`
>     
> - Menua: **Analyses → Frequencies → Contingency Tables**
>     

#### 5.1.2.- Chi-karratua

> [!NOTE]
> **Bi aldagai kategorikoen arteko erlazioa edo dependentzia** aztertzeko estatistika probetako bat da
> Hipotesiak:
> 
> - H₀ → ez dago erlaziorik
>     
> - H₁ → erlazioa dago
>     

> [!NOTE]
> Sexuaren eta irakasgai gogokoenaren arteko lotura aztertzeko kontingentzia-taula eta Pearson-en Chi-karratu testa erabili dira. Deskribapen-mailan, emakumeek Zientziak (%14.2) eta gizonek Historia (%16.7) maiztasun handiagoz aukeratu dituzten arren, analisi estatistikoak erakusten du desberdintasun horiek ez direla esanguratsuak ($χ^2 = 1.87$; $df = 3$; **$p = .600$**). Ondorioz, onartu egiten da independentzia-hipotesia: aztertutako laginean, ikaslearen sexuak ez du eraginik irakasgai baten edo bestearen aldeko lehentasunean."


### 5.2.- Adostasun neurriak

> [!NOTE] Cohen Kappa
> Bi edo gehiagoren **ebaluazioen, neurketen edo kategoriaren balioen arteko adostasuna neurtzen duten teknika estatistikoak** dira
> **Jamovi praktikan:**
> 
> - Analyses → Reliability → Cohen’s Kappa
>     
> - Hautatu `epaile1_irakasgaia` eta `epaile2_irakasgaia`
>     
> - Emaitzak: **Kappa balioa** eta interpretazioa

| Kappa     | Adostasuna          |
| --------- | ------------------- |
| <0        | Ez dago adostasunik |
| 0-0.20    | Adostasun txikia    |
| 0.21-0.40 | Adostasun baxua     |
| 0.41-0.60 | Moderatua           |
| 0.61-0.80 | Ona                 |
| 0.81-1    | Oso ona             |



### 5.3.- **Korrelazioa eta erregresioa (15 min)**

#### 5.3.1.- Korrelazioa

> [!NOTE] Korrelazioa
> 
> Bi **aldagai kuantitatiboen arteko erlazioa** neurtzen duen estatistika tresna da
> - Bi aldagaien arteko erlazioa: `akad_ikasketa_orduak` ↔ `post_matematika_nota`
>     
> - Parametrikoa: Pearson (normalak eta interval eskala)
>     
> - Ez-parametrikoa: Spearman (ez normalak edo ordinalak)
>     
> 
> Balioak:
> 
> - -1 → erlazio negatiboa
>     
> - 0 → erlaziorik ez
>     
> - 1 → erlazio positiboa

Hona hemen **taula praktiko bat**, zeinekin ikusi daitekeen **zein korrelazio-mota erabili** aldagai mota eta banaketaren arabera:

| Aldagai mota          | Banaketa  | Korrelazio gomendatua                | Oharrak                                                  |
| --------------------- | --------- | ------------------------------------ | -------------------------------------------------------- |
| Jarraibide / continua | Normal    | **Pearson**                          | Bi aldagaien arteko erlazio lineala neurtzen du          |
| Jarraibide / continua | Ez normal | **Spearman**                         | Bi aldagaien arteko erlazio monotonikoa neurtzen du      |
| Ordinala              | Edozein   | **Spearman**                         | Eskala ordinaletan erlazio monotonikoa aztertzeko egokia |
| Nominal / bi balio    | Edozein   | **Phi / Cramer’s V**                 | Bi aldagai kategorikoen arteko erlazio indarra neurtzeko |
| Nominal / >2 balio    | Edozein   | **Cramer’s V**                       | Bi aldagai kategorikoen arteko erlazio indarra neurtzeko |
| Ordinal + Jarraitua   | Normal    | **Pearson** (baldin erlazio lineala) | Alternatiba: Spearman, ez-lineala bada                   |
| Ordinal + Jarraitua   | Ez normal | **Spearman**                         | Erlazio monotonikoa neurtzen du                          |

- Menua: Analyses → Regression → Matriz de Correlación

- `pre_matematika_nota`, `post_matematika_nota` eta `aka_ikasketa_orduak`


> [!NOTE]
> Pearson-en korrelazio-koefizientea kalkulatu da tratamenduaren aurretik eta ondoren matematikako errendimendu akademikoaren egonkortasuna aztertzeko. Emaitzek **korrelazio positibo oso sendoa eta estatistikoki esanguratsua** erakusten dute (**$r = .91$; $p < .001$**). Elkartze-indize altu honek iradokitzen du hasierako fasean lortutako emaitzak amaierako faseko arrakastaren iragarle (_predictor_) oso fidagarriak direla; izan ere, ikasleek taldearen barruan duten erlatibozko posizioari modu koherentean eutsi diote (**$R^2 = .83$**).

#### 5.3.2.- Erregresioa

> [!NOTE] Erregresioa
> Aldagai batek (**menpeko aldagaia**) beste aldagai batek edo aldagai batzuek (**independenteko aldagaiak**) duten **eragina eta erlazioa** aztertzeko estatistika teknika d
> 
> - Dependent: `post_matematika_nota`
>     
> - Predictor: `akad_ikasketa_orduak`
>     
> - Menua: Analyses → Regression → Linear Regression
>     

## 6.- Estatistika inferentziala (15 min)

> [!NOTE]
> Helburua:
> 
> **Lagin batetik populazioari buruzko ondorioak ateratzea.**
> 
> Tresnak:
> 
> - konfiantza-tarteak
>     
> - hipotesi-kontrasteak

    
### 6.1.- Konfiantza-tartea

Populazio parametroa egongo den **balio tartea**.

Adib:

batezbestekoa = 78  
CI95% = **73.52 – 82.48**

Interpretazioa:

%95eko konfiantzarekin, populazioaren batezbestekoa tarte horretan dago.



> [!NOTE]
> Puntuazioen azterketa konparatiboak errendimendu akademikoaren hobekuntza nabarmena erakusten du esku-hartzearen ondoren. Batez besteko aritmetikoa pre-testeko **65.7tik (95% konfiantza-tartea [63.9, 67.5])** post-testeko **70.9ra (95% konfiantza-tartea [68.9, 72.9])** igo da. Bi faseetako konfiantza-tarteek elkar ez ukitzeak froga sendoa ematen du lortutako hobekuntza estatistikoki esanguratsua dela baieztatzeko. Gainera, kalifikazioen barrutian desplazamendu positiboa antzeman da, batez ere gutxieneko balioan (46.3 post-testean eta 38.9 hasieran); horrek iradokitzen du erabilitako metodologiak eragin mesedegarria izan duela ikasle guztien errendimenduan, hasierako maila edozein izanda ere


### 6.2.- Hipotesi kontrastea (10 min)

Urratsak:

1️⃣ Hipotesiak formulatu

H₀ → ez dago efekturik  
H₁ → efektua dago

2️⃣ α ezarri

normalean **0.05**

3️⃣ Estatistikoa kalkulatu

4️⃣ p-balioa interpretatu

|p balioa|Interpretazioa|
|---|---|
|p < 0.05|esanguratsua|
|p < 0.01|oso esanguratsua|
|p < 0.001|oso oso esanguratsua|
### 6.3.- Talde konparazioak (5 min)

### 6.4.- Bi talde

#### 6.4.1.- Parametrikoak: T-Student

Bi talde konparatzeko.

- lagin independenteak
    
- lagin erlazionatuak
    
Bariantzen homogeneotasuna egiaztatzeko Levene-ren testa aplikatu da. Emaitzek erakusten dutenez, ez dago desberdintasun esanguratsurik taldeen arteko aldakortasunean, ez hasierako unean ($F(1, 118) = 3.00$; $p = .086$), ezta amaierakoan ere ($F(1, 118) = 1.11$; $p = .294$). P-balioak .05 atalasearen gainetik egoteak homozedastizitate-suposizioa berresten du, eta horrek t-test parametrikoaren erabilera egokitzat jotzea ahalbidetzen du

Laginketa independenteetarako t-testa aplikatu da sexuaren arabera matematikako puntuazioetan desberdintasunik dagoen egiaztatzeko. Emaitzek erakusten dute ez dagoela alde esanguratsurik gizonen eta emakumeen artean, ez pre-test fasean (**$t(118) = -0.018; p = .986; d = -0.003$**), ezta post-test fasean ere (**$t(118) = -0.656; p = .513; d = -0.121$**). Efektuaren tamaina oso baxua denez, ondoriozta daiteke sexua ez dela aldagai diskriminatzailea ikasleen errendimendu akademikoan, metodoa aplikatu aurretik zein ondoren.

#### 6.4.2.- Ez-parametrikoak: Mann-Whitney eta Wilcoxon

- Mann-Whitney
    
- Wilcoxon

### 6.5.- Talde edo gehiago

#### 6.5.1.- Parametrikoak: ANOVA

Se comprobaron los supuestos de normalidad y homogeneidad de varianzas antes de realizar el ANOVA. La prueba de Shapiro–Wilk indicó que los datos seguían una distribución normal (W = 0.992, p = .718). Asimismo, la prueba de Levene mostró que se cumplía el supuesto de homogeneidad de varianzas (F(7,112) = 0.843, p = .554)

Se realizó un ANOVA factorial para analizar el efecto de la asignatura preferida y el sexo sobre las horas de estudio académico. Los resultados mostraron que el modelo global no fue significativo, F(7,112) = 1.84, p = .086. Tampoco se encontró un efecto significativo del sexo, F(1,112) ≈ 0.00, p = .984. El efecto de la asignatura preferida estuvo cercano a la significación, F(3,112) = 2.51, p = .062, η² = .061. Asimismo, la interacción entre asignatura preferida y sexo no fue significativa, F(3,112) = 1.05, p = .375.

#### 6.5.2.- Ez-parametrilkoak: Kruskal-Wallis
## 7.- Amaiera (5 min)

Galindo, H. (2020). _Estadística para no estadísticos: Una guía básica sobre la metodología cuantitativa de trabajos académicos_. 3ciencias.

Mezu nagusia:

Analisi kuantitatiboan **3 gauza jakin behar dira**:

1️⃣ Aldagai mota  
2️⃣ Banaketa (normala ala ez)  
3️⃣ Galdera estatistikoa

