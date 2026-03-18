---
title: Zein da bi aldagai kuantitatiboen arteko erlazioa?
subtitle: Adostasun neurriak, Korrelazioa eta erregresioa
subject: Analisi Inferentziala
site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
---

## **Adostasun neurriak**

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


## **Korrelazioa**

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

## Erregresioa

> [!NOTE] Erregresioa
> Aldagai batek (**menpeko aldagaia**) beste aldagai batek edo aldagai batzuek (**independenteko aldagaiak**) duten **eragina eta erlazioa** aztertzeko estatistika teknika d
> 
> - Dependent: `post_matematika_nota`
>     
> - Predictor: `akad_ikasketa_orduak`
>     
> - Menua: Analyses → Regression → Linear Regression
