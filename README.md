<div align="center">

# `>_ mr-aurevo-x@workshop:~`

**AI-run workshop - Cursor builds | Mr-Aurevo-X QA | Windows factory**

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/c136a35/assets/hero-boot.svg?v=c136a35" alt="Boot console scrolling" width="100%"/>

<br/>

[![GitHub followers](https://img.shields.io/github/followers/Mr-Aurevo-X?style=for-the-badge&logo=github&logoColor=39ff14&color=050807&labelColor=071410)](https://github.com/Mr-Aurevo-X)
[![Profile views](https://komarev.com/ghpvc/?username=Mr-Aurevo-X&style=for-the-badge&color=00f0ff&label=VISITORS)](https://github.com/Mr-Aurevo-X)
[![Cursor AI](https://img.shields.io/badge/BUILT_BY-CURSOR_AI-39ff14?style=for-the-badge&labelColor=050807&logo=cursor&logoColor=39ff14)](https://cursor.com)
[![Mr-Aurevo-X QA](https://img.shields.io/badge/IDEAS_%26_QA-MR--AUREVO--X-00f0ff?style=for-the-badge&labelColor=050807)](https://github.com/Mr-Aurevo-X)

`STATUS=ONLINE` | `VITRINE=public` | `PC_COMMAND=5_HUBS` | `ATELIER+SALON+LAB=private` | `MODE=AI_OPERATED` | `COLOR=DUAL_SPLIT`

</div>

---

## sessions - dual console

<div align="center">

<table>
  <tr>
    <td width="50%" align="center">
      <img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/c136a35/assets/console-build.svg?v=c136a35" alt="Cursor AI build console (green)" width="100%"/>
    </td>
    <td width="50%" align="center">
      <img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/c136a35/assets/console-qa.svg?v=c136a35" alt="Mr-Aurevo-X QA console (cyan)" width="100%"/>
    </td>
  </tr>
</table>

</div>

```diff
+ CURSOR AI ........ architecture | code | refactors | tooling | shipping
+ MR-AUREVO-X ...... product ideas | real-world testing | QA | vision
! RULE ............. if it ships, AI wrote it - Mr-Aurevo-X signed it off
```

> **FR** - L'IA construit et opere. Mr-Aurevo-X apporte les idees, casse / teste, et valide.
>
> **EN** - Cursor AI builds & operates. Mr-Aurevo-X brings ideas, stress-tests, and the green light.

---

## workshop floor

Single crafted factory board (dual-split: **BUILD green** / **QA cyan**). Decorative status only -- not live CI, not live chat.

<div align="center">

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/c136a35/assets/factory-floor.svg?v=c136a35" alt="Workshop factory floor status board" width="100%"/>

</div>

---

## featured - public vitrine

**7 outils desktop | gratuits | locaux (sauf DeviseConvert : taux BCE + cache offline) | `.exe` sans installation**
`public | AI-built | human-tested` | SoT `Dev Central Tree\Git Vitrine Public\`

| Outil | Role | Lien |
|:--|:--|:--|
| **QrMake** | QR multi-payloads | [repo](https://github.com/Mr-Aurevo-X/QrMake) / [releases](https://github.com/Mr-Aurevo-X/QrMake/releases/latest) |
| **UnitConvert** | Convertisseur d'unites | [repo](https://github.com/Mr-Aurevo-X/UnitConvert) / [releases](https://github.com/Mr-Aurevo-X/UnitConvert/releases/latest) |
| **DeviseConvert** | Devises BCE + cache offline | [repo](https://github.com/Mr-Aurevo-X/DeviseConvert) / [releases](https://github.com/Mr-Aurevo-X/DeviseConvert/releases/latest) |
| **EpochClock** | Unix <-> date locale/UTC | [repo](https://github.com/Mr-Aurevo-X/EpochClock) / [releases](https://github.com/Mr-Aurevo-X/EpochClock/releases/latest) |
| **StopwatchPlus** | Chrono / alarmes / Pomodoro | [repo](https://github.com/Mr-Aurevo-X/StopwatchPlus) / [releases](https://github.com/Mr-Aurevo-X/StopwatchPlus/releases/latest) |
| **MetaStrip** | Strip EXIF/GPS/XMP | [repo](https://github.com/Mr-Aurevo-X/MetaStrip) / [releases](https://github.com/Mr-Aurevo-X/MetaStrip/releases/latest) |
| **QrBatch** | QR en lot -> PNG + ZIP | [repo](https://github.com/Mr-Aurevo-X/QrBatch) / [releases](https://github.com/Mr-Aurevo-X/QrBatch/releases/latest) |

---

## mounts - filesystem

```text
/workshop
|-- atelier/     PC Command | 5 hubs in-hub (Dashboard + modules) [private]
|-- salon/       Game launcher + X titles | forks                  [private]
|-- lab/         Lab launcher + R&D | Discordbots | prototypes     [private]
`-- vitrine/     7 public desktop tools                            [public]
```

<details>
<summary><strong>full workshop map - arborescences</strong></summary>

<a id="atelier"></a>

### atelier - PC Command (5 hubs)

SoT : `Dev Central Tree\01_Hubs\` | pywebview + WebView2 | UAC admin | lazy DOM | ConfirmGate  
Ship : `Launch-Hub-*.exe` / `Hubs.zip` via Install-Easy (plus de launcher plat / `PCCommand.exe`)

```text
01_Hubs/
|-- Hub-Systeme/        * SystemClean | RamCleaner | ProcessHub | UninstX | SysInspect | ...
|-- Hub-Reseau/         * NetAdmin | NetMap | RoadWay-X | WifiKey
|-- Hub-Securite/       * FileGuard | CertView | RepoRadar | WinAudit
|-- Hub-Dev/            * Lua/Dll/JsonClean | HashCheck | ProtAudit | IdentityReset | EnvEditor
`-- Hub-Utilitaires/    * UtilKit (+ ShellKit) | MediaKit | Capture | ColorPicker | ...

02_Shared_Infrastructure/
|-- UI-proprietaire/    pc-command-kit SoT
|-- SecurityHelpers/    ConfirmGate + security.py
|-- HostHelpers/        window_chrome | suite_launch
|-- Install-Easy-Private/  installer (Hubs.zip + Lab + Salon packs)
`-- MrAurevoX-Releases/ packaging / portable assets

standalones (Lab siblings) : Auto-Dox | Opti (later) | Track
```

<a id="salon"></a>

### salon - Game hub

```text
Game/
|-- Salon/                  * game launcher  (private)
|-- * Original X            Incremental-X | Factory-X | Empire-X | Colony-X
|                           Deck-X | Battler-X | Tower-X | Puzzle-X | Story-X
|-- forks                   Antimatter-X | Evolve-X | Idle* | IndustryIdle-X | ...
`-- tools                   GameChangelog | PreviewCars
```

<a id="lab"></a>

### lab - R&D / prototypes / bots

Hub **Lab** | `Lancer.cmd` | `Lab.exe` | `launcher.py`

```text
Lab/
|-- Lancer.cmd | Lab.exe    * Lab launcher  (private)
|-- Privacy / OSINT         Track | IdentityReset | Auto-Dox
|-- Perf / reseau           Opti | RoadWay-X | Ram Cleaner
|-- Reverse / recovery      LuaClean | DllClean | JsonClean | ProtAudit | LuaObfuscator
`-- DiscordBots/
    `-- Mr-X-Sentinel/      * Discord bot platform (private)
                            mod | security | eco | XP | tickets | music | AI
```

</details>

---

## telemetry

<div align="center">

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/main/assets/github-stats.svg?v=08bc455" height="165" alt="GitHub stats"/>

<br/>

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/main/assets/github-streak.svg?v=08bc455" alt="Streak"/>

<br/>

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/output/github-contribution-grid-snake-dark.svg?v=31804052317" alt="Contribution snake" width="100%"/>

</div>

---

## stack

<div align="center">

![Python](https://img.shields.io/badge/-Python-050807?style=for-the-badge&logo=python&logoColor=39ff14)
![PowerShell](https://img.shields.io/badge/-PowerShell-050807?style=for-the-badge&logo=powershell&logoColor=00f0ff)
![JavaScript](https://img.shields.io/badge/-JavaScript-050807?style=for-the-badge&logo=javascript&logoColor=39ff14)
![TypeScript](https://img.shields.io/badge/-TypeScript-050807?style=for-the-badge&logo=typescript&logoColor=00f0ff)
![HTML5](https://img.shields.io/badge/-HTML5-050807?style=for-the-badge&logo=html5&logoColor=39ff14)
![CSS3](https://img.shields.io/badge/-CSS3-050807?style=for-the-badge&logo=css3&logoColor=00f0ff)
![Windows](https://img.shields.io/badge/-Windows-050807?style=for-the-badge&logo=windows&logoColor=39ff14)
![WebView2](https://img.shields.io/badge/-WebView2-050807?style=for-the-badge&logo=microsoftedge&logoColor=00f0ff)
![pywebview](https://img.shields.io/badge/-pywebview-050807?style=for-the-badge&logo=python&logoColor=39ff14)
![PyInstaller](https://img.shields.io/badge/-PyInstaller-050807?style=for-the-badge&logo=python&logoColor=00f0ff)
![Chart.js](https://img.shields.io/badge/-Chart.js-050807?style=for-the-badge&logo=chartdotjs&logoColor=39ff14)
![Git](https://img.shields.io/badge/-Git-050807?style=for-the-badge&logo=git&logoColor=00f0ff)
![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-050807?style=for-the-badge&logo=githubactions&logoColor=39ff14)
![Cursor](https://img.shields.io/badge/-Cursor_AI-050807?style=for-the-badge&logo=cursor&logoColor=00f0ff)
![Node.js](https://img.shields.io/badge/-Node.js-050807?style=for-the-badge&logo=nodedotjs&logoColor=39ff14)
![pnpm](https://img.shields.io/badge/-pnpm-050807?style=for-the-badge&logo=pnpm&logoColor=00f0ff)
![discord.js](https://img.shields.io/badge/-discord.js-050807?style=for-the-badge&logo=discord&logoColor=5865F2)
![Discord](https://img.shields.io/badge/-Discord_Bots-050807?style=for-the-badge&logo=discord&logoColor=00f0ff)
![Next.js](https://img.shields.io/badge/-Next.js-050807?style=for-the-badge&logo=nextdotjs&logoColor=39ff14)
![React](https://img.shields.io/badge/-React-050807?style=for-the-badge&logo=react&logoColor=00f0ff)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-050807?style=for-the-badge&logo=postgresql&logoColor=39ff14)
![Prisma](https://img.shields.io/badge/-Prisma-050807?style=for-the-badge&logo=prisma&logoColor=00f0ff)
![Redis](https://img.shields.io/badge/-Redis-050807?style=for-the-badge&logo=redis&logoColor=39ff14)
![Docker](https://img.shields.io/badge/-Docker-050807?style=for-the-badge&logo=docker&logoColor=00f0ff)
![FastAPI](https://img.shields.io/badge/-FastAPI-050807?style=for-the-badge&logo=fastapi&logoColor=39ff14)
![Lavalink](https://img.shields.io/badge/-Lavalink-050807?style=for-the-badge&logo=discord&logoColor=00f0ff)

</div>

---

## connect - support

<div align="center">

> **FR** - Lien social + coups de pouce volontaires (la vitrine publique reste gratuite).
>
> **EN** - Social link + optional tips (the public vitrine stays free).

<br/>

[![Discord](https://img.shields.io/badge/Discord-Mr--Aurevo--X-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=050807)](https://discord.com/users/406891052516114442)
[![guns.lol](https://img.shields.io/badge/guns.lol-mr__aurevo__x-00f0ff?style=for-the-badge&labelColor=050807&color=071410)](https://guns.lol/mr_aurevo_x)

<br/>

[![PayPal](https://img.shields.io/badge/PayPal-Donate-39ff14?style=for-the-badge&logo=paypal&logoColor=00f0ff&labelColor=050807)](https://www.paypal.com/paypalme/aurevo1)
[![Revolut](https://img.shields.io/badge/Revolut-mr__aurevo__x-00f0ff?style=for-the-badge&logo=revolut&logoColor=39ff14&labelColor=050807)](https://revolut.me/mr_aurevo_x)

</div>

---

<div align="center">

**Built by Cursor AI | Ideas & QA by Mr-Aurevo-X**
**AI-operated workshop - not a portfolio of vibes, a factory of tools.**

<br/>

`end_of_transmission // stay curious`

</div>
