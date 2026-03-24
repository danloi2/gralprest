---
title: "QualCoder: Oinarrizko konfigurazioa"
subtitle: Ezarpenak eta pertsonalizazioa
subject: QualCoder
---

## Konfigurazio leihoa irekitzea

QualCoder-en ezarpen guztiak `Settings` (Konfigurazioa) leihoan daude. Hona heltzeko hiru modu daude:

- **ALT + S** tekla-lasterbidea
- `Project` menua → **Settings**
- `AI` menua → **Settings**

Dokumentazio ofiziala: [Configuraciones — QualCoder Doc](https://qualcoder-org.github.io/doc/es/2.2.-Settings/)

---

### Kodetzaile-izena (erabiltzaile-profila)

QualCoder-ek erabiltzaile-profila erabiltzen du kodeak nork egin dituen erregistratzeko.

```{admonition} Zergatik da garrantzitsua?
:class: note
GRAL batean bakarrik lan egiten baduzu, izen sinple bat nahikoa da (adib: zure izena). Talde-lanean, kode bakoitza nork esleitu duen jakiteko erabiltzen da.
```

Nola aldatu: Settings leihoan → **Coder name** → aldatu → gorde.

---

### Hizkuntza

QualCoder-en hizkuntza aldatzeko:

1. Ireki `Settings`
2. **Language** atalean hautatu hizkuntza (euskara ez dago; erdarazkoa aukeratu dezakezu)
3. **Itxi eta berrabiarazi** QualCoder hizkuntzak aplikatzeko

```{admonition} Kontuz
:class: warning
Hizkuntza aldatu ondoren QualCoder itxi eta berriro ireki behar da aldaketak ikusteko.
```

---

### Segurtasun kopiak (errespalduak)

QualCoder-ek automatikoki egiten ditu babeskopiak ordero, aktibatuta badago.

```{admonition} Gomendio garrantzitsua
:class: important
- Kode-egitura handiak berrantolatu aurretik egin eskuzko babeskopia.
- Babeskopiak `.qda` formatuan gordetzen dira, denbora-marka batekin: `proiektua_BKP_aaaammdd_hh.qda`
- 1 eta 5 babeskopia arteko gordetzeko konfiguratu daiteke.
```

Nola aktibatu: Settings → **Backups** → gaitu orduko babeskopia automatikoa.

---

### Itxura eta errendimendua

QualCoder-en itxura pertsonaliza daiteke (koloreak, letra-tamaina). Testu handiko fitxategiak izanez gero, txatal (chunk) txikiagoak erabiltzeko aukera dago errendimendua hobetzeko.

Settings atalean `Code Text` atalean: **chunk size** (lehenetsita 50.000 karaktere, gutxitu daiteke).
