---
title: Zerekin egin ditzakezu analisi kualitatiboak?
subtitle: QualCoder, doakoa eta erraza
subject: Analisi Kualitatiboa
---

Hemen daukazue **QualCoder** doako softwarea erabiliz aurreko dataset-a nola aztertu ikasteko gida zehatza.

> [!NOTE] Zer da QualCoder?
> Datu kualitatiboak (testuak, irudiak, audioak eta bideoak) aztertzeko kode irekiko tresna bat da.

### Nola instalatu QualCoder

1. [QualCoder Webgune](https://qualcoder.wordpress.com/) offizialetik Programa deskargatu.
2. Instalatu aurkitutako jarraibideen bidez.
3. Ireki eta proiektu berri bat sortu.

> [!WARNING] Arazoak badituzu
> Kodifikazioa Word edo Excelen ere egin dezakezu kolore eta taulen bidez asmakizun teknikoak eragotziaz. Sorfwarea laguntza bat da, ez helburua.

---

## Pausoz pauso: QualCoder Proiektua

### 1. Proiektu berria sortu

1. Ireki QualCoder.
2. Sakatu `Project` > `New Project`.
3. Aukeratu karpeta bat zure ordenagailuan eta ipini izen bat (adibidez, `TFG_Kualitatiboa.qd`).
4. Proiektua irekita egongo da eta prest datuak sartzeko.

### 2. Fitxategiak inportatu

Orain, deskargatu dituzun fitxategiak QualCoder-en sartu behar dituzu. (Oraindik ez badituzu, hemen daukazue saioan erabiltzeko materiala deskargatzeko aukera: {download}`Elk1 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir01.md>`, {download}`Elk2 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir02.md>`, {download}`Elk3 <../../assets/data/kualitatiboa/2026-elkarrizketa-ir03.md>`, {download}`Egunkaria <../../assets/data/kualitatiboa/20260105-egunkaria-ikerlaria.md>`, {download}`Programazioa <../../assets/data/kualitatiboa/2026-documentua-programazioa-didaktikoa-matematika-lh6.md>`).

1. Joan `Files and Cases` > `Manage files` atalera.
2. Sakatu goiko eskuinaldean dagoen 📄+ (Gehitu fitxategia) botoia.
3. Aukeratu deskargatu dituzun `.md` edo `.txt` fitxategiak eta inportatu.
4. Fitxategi bakoitzari izen garbi bat jar diezaiokezu, adibidez: `Elkarrizketa_1`, `Egunkaria_1`, etab.

### 3. Kodeak sortu

Fitxategiak aztertzen hasi baino lehen, edo irakurtzen ari garen bitartean, **kodeak (etiketak)** sortu ditzakegu.

1. Joan `Codes` > `Manage codes` atalera.
2. Sakatu bertan dagoen ➕ (Gehitu kodea) botoia.
3. Idatzi zure kodeak, adibidez: `motibazioa`, `talde_lana`, `zailtasunak`, `metodologia_aktiboa`
4. Kode bakoitzari **kolore ezberdin bat** esleitu diezaiokezu, askoz bisualagoa izateko.

### 4. Datuak kodifikatu (Testuak markatu)

Hau da pausorik garrantzitsuena. Irakurri testua eta aplikatu sortu dituzun kodeak.

1. Joan `Coding` > `Code text` atalera.
2. Aukeratu fitxategi bat ezkerreko zerrendan (adib.: `2026-elkarrizketa-ir01`).
3. Hautatu testu zati garrantzitsu bat saguarekin (adib.: _"Ikusi dut ikasleek taldean lan egiten dutenean gehiago parte hartzen dutela"_).
4. Eskubialdean, zure kodeen zerrendan, klik egin egokiena den kodean.
5. Ikusiko duzu testu zati hori kodearen kolorearekin markatuta geratzen dela eta eskuineko marjinean kodearen izena agertzen dela.

### 5. Kategoriak (Zuhaitza) sortu

Kode asko dituzunean, taldekatu egin behar dituzu.

1. Behin kode guztiak sortuta daudela, `Manage Codes` atalean berean, zuhaitz egitura bat sor dezakezu.
2. Kode bat beste baten barruan (azpikode gisa) sartzeko, besterik gabe, **arrastatu kode bat bestearen gainean** saguarekin.
3. Adibidez, kategoria bat sor dezakezu eta barruan hainbat kode sartu.

### 6. Emaitzak atera eta esportatu

Dena kodifikatuta dagoenean, zein ondoriora heldu garen ikusi behar da.

1. Joan `Reports` > `Coding reports` atalera.
2. Aukeratu ikusi nahi dituzun kodeak edo fitxategiak (normalean denak aukeratzen dira amaierako txostenerako).
3. Sakatu bilaketa botoia (Kargatu/Run).
4. Zure kode guztien laburpena agertuko da, dagokien testu-zatiekin. Hauek TFGan zuzenean erabili ditzakezun zitak dira.
5. Posible da taula hau **Esportatzea** (.csv edo .html formatuan) emaitzen atala idazten hasteko.

> [!IMPORTANT] Azken gomendioa
> QualCoder-ek datu-base batean (SQLite) funtzionatzen du, beraz aldaketak automatikoki gordetzen dira. Hala ere, komeni da noizean behin `.qd` karpetaren edo fitxategiaren **segurtasun kopia** bat egitea.
