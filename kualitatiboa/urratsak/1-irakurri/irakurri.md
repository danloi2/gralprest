---
title: "1. Irakurri"
subtitle: Datu guztiak osorik irakurri ulertzeko
subject: Analisi Kualitatiboa
---

Analisi kualitatiboa hasi aurretik, datuak **irakurri eta prestatu** egin behar dira. Hau da prozesuko lehen fasea: datuak ezagutzea, antolatzea eta tresnan sartzea.

```{admonition} Garrantzitsua
:class: important
Prestaketako fasea ez da "ekintza tekniko bat" — analisiaren parte da. Lehen irakurketan jada ideiak identifikatzen hasten zara.
```

---

## 1. Lehen irakurketa

Lehen pausua datuak osorik irakurtzea da, koderik esleitu gabe.

**Helburua:**

- Testua osorik ulertzea
- Ideia nagusiak eta errepikapenak antzematea
- Lehen inpresioak jasotzea oharren bidez

```{admonition} Aholkua
:class: tip
Irakurtzen ari zarela, idatz itzazu zure lehen erreakzioak paper batean. Kodifikazioan lagungarriak izango dira.
```

---

## 2. Transkripzioa (beharrezkoa bada)

Audio edo bideoak erabili badituzu, testu bihurtu behar dituzu analizatu aurretik.

:::{glossary}

Transkripzioa
: Audio edo bideo batean esandakoak testu idatzi bihurtzeko prozesua, analisi kualitatiboan erabiltzeko.

:::

**Transkripzioa egiteko aukerak:**

| Modua | Tresna | Ezaugarriak |
|:---|:---|:---|
| Eskuzkoa | Edozein testu-editore | Zehatza, motela |
| Semi-automatikoa | [oTranscribe](https://otranscribe.com/) | Doakoa, nabigatzailean |
| Automatikoa | [Whisper (OpenAI)](https://openai.com/research/whisper) | Doakoa (Python), oso zehatza |
| Automatikoa | [Turboscribe](https://turboscribe.ai/es/) | AI bidezkoa, oso azkarra |
| Automatikoa | [Clipchamp (Microsoft)](https://clipchamp.com/es/) | Doakoa, bideoetatik azpitituluak/testua ateratzeko |

```{admonition} Gure dataset-ean
:class: note
Ikastaro honetako dataset-a dagoeneko transkribatuta dago. Zuzenean hurrengo fasera pasa zaitezke.
```

---

## 3. Datuen antolaketa: Fitxategien izenak

Behin testuak prest daudenean, ezinbestekoa da **nomenklatura-arau** koherenteak erabiltzea. Horrela, QualCoder-ek fitxategiak automaitkoki ordenatuko ditu eta errazagoa izango da iturriak identifikatzea.

### Kebab-case eta datak

Gure proiektuan **kebab-case** formatua erabiliko dugu:

- Dena letra xehez (**minuskulaz**).
- Hitzak gidoi baten bidez bereizita (`-`). Ez erabili espaziorik, tilderik edo hizki berezirik (ñ, ?, !).
- **Data hasieran** jarri: fitxategiak kronologikoki ordenatzeko (adib: `2026-03-23-`).

**Gomendatutako egitura:** `URTEA-HILA-EGUNA-mota-id.md`

| Atala | Adibidea | Deskribapena |
| :--- | :--- | :--- |
| **Data** | `2026-03-23` | Urtea-Hila-Eguna, orden kronologikoa mantentzeko. |
| **Mota** | `elkarrizketa` | `elkarrizketa`, `egunkaria` edo `documentua`. |
| **Id** | `ir01` | Parte-hartzailearen edo saioaren kodea (Irakaslea 1). |

### Gure dataset-eko adibideak

Ikastaro honetako dataset-ak ia osorik jarraitzen du konbentzio hau:

- ✅ `2026-elkarrizketa-ir01.md`
- ✅ `20260105-egunkaria-ikerlaria.md` (YYYYMMDD formatuan)
- ✅ `2026-documentua-programazioa-didaktikoa-matematika-lh6.md`

---

## Laburpena: prestaketa fasea

```{admonition} Prestaketa: faseen laburpena
:class: note
1. 📖 **Irakurri** materialak osorik
2. 🎙️ **Transkribatu** audioak (beharrezkoa bada)
3. 🗂️ **Antolatu** fitxategiak izen argiarekin
4. ▶️ Prest: **kodifikaziorako** (2. urratsa)
```
