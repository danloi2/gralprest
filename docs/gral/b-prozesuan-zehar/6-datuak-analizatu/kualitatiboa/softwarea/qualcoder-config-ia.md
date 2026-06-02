---
title: "QualCoder: IA konfigurazioa"
---

!!! note "Atal aurreratua"
    IA konfiguratzea hautazkoa da. Oinarrizko kodifikazio-analisia egiteko ez da beharrezkoa.

!!! note "Zertarako erabil dezaket IA?"
    - Testu zatiak automatikoki kodifikatzea
    - Kode-kategoriak proposatzea
    - Galderak egitea zure datuen gainean

Dokumentazio ofiziala: [Configuración de la IA — QualCoder Doc](https://qualcoder-org.github.io/doc/es/2.3.-AI-Setup/)

---

## 1. IA aktibatzea

IA lehenetsita desaktibatuta dago. Aktibatzeko:

1. Joan `AI` → `Setup Wizard`
2. Onartu aktibazioa (opt-in)
3. Hautatu eredua (ikus behean)

---

## 2. Ereduak: zein aukeratu?

QualCoder-ek hainbat LLM eredu onartzen ditu:

Adimen artifiziala (QualCoder)
: Softwareak gizakiaren interpretazio-lana simulatzeko edo laguntzeko erabiltzen dituen teknikak. QualCoder-en, testu-analisian laguntzeko erabiltzen da.

| Eredua | Kostua | Pribatutasuna | Gomendioa |
|:---|:---|:---|:---|
| **Blablador** | Doakoa | Bikaina — ez du datuak gordetzen | ✅ GRAL-erako |
| OpenAI GPT-4 | Ordainpekoa ($5 gutxienez) | Ertain | Kalitate altua |
| Ollama (lokala) | Doakoa | Perfektua — ez du sarearik erabiltzen | Teknikoki konplexua |

!!! tip "Gure gomendioa"
    GRAL-erako **Blablador** gomendatzen dugu: doakoa da, ez du datuak gordetzen eta unibertsitate-kontuarekin erregistratu daiteke.

---

## 3. Blablador API key sortzea

Blablador erabiltzeko, Helmholtz Society-ren GitLab-en API-gako bat behar duzu.

### Erregistroa eta API key lortzea

1. Sartu [GitLab Helmholtz](https://codebase.helmholtz.cloud/) gunean.
2. Egin klik **Sign in with Helmholtz ID** botoian eta hasi saioa (zure unibertsitate-kontuarekin, GitHub, Google edo ORCID erabiliz).
3. Behin barruan zaudela, joan goiko eskuineko profilera eta aukeratu **Edit profile**.
4. Ezkerreko menuan, klikatu **Access Tokens** atalean.
5. Sortu token berri bat ezaugarri hauekin:

!!! note "Token-aren konfigurazioa"
    - **Token name**: "QualCoder" (edo nahi duzun izena)
    - **Expiration date**: data bat jarri (adib: 2026-12-31)
    - **Scopes** (baimenak):
        - ✅ `api` (beharrezkoa)
        - ✅ `read_api` (gomendatua)

!!! warning "Segurtasuna"
    API-gakoa pasahitz baten moduan tratatu:

    - Ez partekatu
    - Ez igo biltegi publikoetara
    - Gorde modu seguruan

### QualCoder-en sartu

1. Kopiatu API key-a
2. Joan QualCoder → `AI` → `Settings`
3. Hautatu **Blablador** eredua
4. Itsatsi API key-a dagozkion eremuan

---

## 4. Pribatutasunari buruzko oharrak

!!! note "Datuen pribatutasuna"
    Edozein IA zerbitzu erabili aurretik:

    - Anonimizatu datu sentikorrak
    - Ez bidali identifikagarriak diren datu pertsonalak
    - Blablador-ek ez du datuak gordetzen, baina hobe da neurri hauek hartzea
