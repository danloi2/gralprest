---
title: Zer deskribatu daiteke aldagai bakar batekin?
subtitle: Maiztasuna, joera zentrala eta dispertsioa
subject: Analisi Deskribatzailea
site:
  hide_outline: false
  hide_toc: false
  hide_title_block: false
---


> **Helburua:** Datu multzo bat **laburbiltzea eta deskribatzea**.

## **Maiztasun taulak**

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

## **Grafikoak**

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

## **Joera zentrala**

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

## **Dispertsioa**

**Definizioa:** Datuen banaketa edo bariazio neurtzen du.

- Minimoa, maximoa, desbideratze tipikoa, bariantza  
    💡 Praktika: Desbideratze tipikoa handia bada, batezbestekoak **ez du fidagarritasun handirik**
    

**Praktika gida:**

- Analyses → Descriptives
    
- Hautatu `post_matematika_nota`
    
- Markatu **SD, Variance, Minimum, Maximum, Hedadura**
    

> [!NOTE]
> Aldakortasunari dagokionez, `post_matematika_nota` aldagaiak 10.9ko desbideratze tipikoa eta 119ko varianza erakusten ditu. Datu hauek adierazten dute ikasleen arteko aldeak moderatuak direla eta lagina nahiko kohesionatuta dagoela, nahiz eta banakako diferentziak egon. Laginaren hedadura edo rangoa 52.6 puntukoa da (46.3tik 98.9ra), eta horrek erakusten du ebaluazio-tresnak gaitasuna izan duela errendimendu desberdinak atzemateko, inolako datu galdu gabe ($N=120$).
