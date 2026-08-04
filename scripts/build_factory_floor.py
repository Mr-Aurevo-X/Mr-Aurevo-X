# -*- coding: utf-8 -*-
"""Generate factory-floor.svg (dual-split green/cyan) and rewrite README."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
README = ROOT / "README.md"

GREEN = "#39ff14"
CYAN = "#00f0ff"
BG = "#050807"
DEEP = "#020403"
MUTED = "#4d7a5c"
SOFT_G = "#6aff9a"
SOFT_C = "#7ec8ff"
STROKE_G = "#1a3d2a"
STROKE_C = "#0a3a44"


def factory_svg() -> str:
    # Dense ops/factory board — honest "crafted showcase", dual-split colors
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="420" viewBox="0 0 1100 420" role="img" aria-label="Workshop factory floor crafted status board">
  <defs>
    <linearGradient id="floorBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#030605"/>
      <stop offset="50%" stop-color="#050807"/>
      <stop offset="100%" stop-color="#030a0c"/>
    </linearGradient>
    <linearGradient id="split" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{GREEN}"/>
      <stop offset="100%" stop-color="{CYAN}"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M24 0H0V24" fill="none" stroke="{GREEN}" stroke-opacity="0.06"/>
    </pattern>
  </defs>

  <rect width="1100" height="420" fill="url(#floorBg)"/>
  <rect width="1100" height="420" fill="url(#grid)"/>
  <rect x="12" y="12" width="1076" height="396" rx="14" fill="{BG}" stroke="url(#split)" stroke-width="2"/>

  <!-- title bar -->
  <rect x="24" y="24" width="1052" height="36" rx="6" fill="{DEEP}" stroke="{STROKE_G}"/>
  <text x="40" y="47" fill="{SOFT_G}" font-family="Consolas, ui-monospace, monospace" font-size="14">workshop floor -- factory status board</text>
  <text x="780" y="47" fill="{MUTED}" font-family="Consolas, ui-monospace, monospace" font-size="11">CRAFTED SHOWCASE</text>
  <text x="930" y="47" fill="{CYAN}" font-family="Consolas, ui-monospace, monospace" font-size="11">NOT LIVE CI</text>

  <!-- LEFT: dual lanes BUILD / QA -->
  <rect x="24" y="72" width="250" height="300" rx="8" fill="{DEEP}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="40" y="96" fill="{GREEN}" font-family="Consolas, monospace" font-size="13">LANE A -- BUILD</text>
  <text x="40" y="118" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">Cursor AI</text>
  <text x="40" y="144" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">architecture</text>
  <text x="40" y="164" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">host + ui kits</text>
  <text x="40" y="184" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">packaging / ship</text>
  <text x="40" y="204" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">Lancer.cmd first</text>
  <rect x="40" y="220" width="200" height="6" rx="3" fill="#0a1a12"/>
  <rect x="40" y="220" width="168" height="6" rx="3" fill="{GREEN}">
    <animate attributeName="width" values="120;200;168;120" dur="8s" repeatCount="indefinite"/>
  </rect>
  <text x="40" y="250" fill="{MUTED}" font-family="Consolas, monospace" font-size="10">throughput (decorative)</text>

  <line x1="40" y1="268" x2="254" y2="268" stroke="{STROKE_G}"/>

  <text x="40" y="294" fill="{CYAN}" font-family="Consolas, monospace" font-size="13">LANE B -- QA</text>
  <text x="40" y="316" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">Mr-Aurevo-X</text>
  <text x="40" y="342" fill="{CYAN}" font-family="Consolas, monospace" font-size="12">ideas | break tests</text>
  <text x="40" y="362" fill="{CYAN}" font-family="Consolas, monospace" font-size="12">sign-off | vision</text>

  <!-- CENTER: mounts + vitrine ticker -->
  <rect x="286" y="72" width="520" height="300" rx="8" fill="{DEEP}" stroke="{STROKE_C}" stroke-width="1.5"/>
  <text x="302" y="96" fill="{CYAN}" font-family="Consolas, monospace" font-size="13">MOUNTS -- Dev Central Tree</text>

  <!-- mount chips -->
  <rect x="302" y="112" width="110" height="28" rx="4" fill="#071410" stroke="{GREEN}"/>
  <text x="316" y="130" fill="{GREEN}" font-family="Consolas, monospace" font-size="11">atelier ON</text>
  <rect x="422" y="112" width="110" height="28" rx="4" fill="#071410" stroke="{GREEN}"/>
  <text x="440" y="130" fill="{GREEN}" font-family="Consolas, monospace" font-size="11">salon ON</text>
  <rect x="542" y="112" width="110" height="28" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="564" y="130" fill="{CYAN}" font-family="Consolas, monospace" font-size="11">lab ON</text>
  <rect x="662" y="112" width="120" height="28" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="678" y="130" fill="{CYAN}" font-family="Consolas, monospace" font-size="11">vitrine PUB</text>

  <text x="302" y="168" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="12">ATELIER  | PC Command hub | +30 tools | UAC</text>
  <text x="302" y="190" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="12">SALON    | Game launcher + X titles | forks</text>
  <text x="302" y="212" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="12">LAB      | R&amp;D | Discordbots | prototypes</text>
  <text x="302" y="234" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="12">VITRINE  | 7 public desktop tools | free</text>

  <line x1="302" y1="250" x2="786" y2="250" stroke="{STROKE_C}"/>
  <text x="302" y="274" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">PUBLIC TICKER</text>

  <!-- scrolling ticker strip -->
  <clipPath id="tick"><rect x="302" y="286" width="484" height="28" rx="4"/></clipPath>
  <rect x="302" y="286" width="484" height="28" rx="4" fill="#030605" stroke="{STROKE_G}"/>
  <g clip-path="url(#tick)" font-family="Consolas, monospace" font-size="12" fill="{GREEN}">
    <text x="310" y="305">
      QrMake  |  UnitConvert  |  DeviseConvert  |  EpochClock  |  StopwatchPlus  |  MetaStrip  |  QrBatch  |  QrMake  |
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-520 0" dur="22s" repeatCount="indefinite"/>
    </text>
  </g>

  <text x="302" y="348" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">rule: if it ships, AI wrote it -- Mr-Aurevo-X signed it off</text>
  <text x="302" y="368" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">SoT: Dev Central Tree | Lancer before exe</text>

  <!-- RIGHT: sentinel + connect -->
  <rect x="818" y="72" width="258" height="300" rx="8" fill="{DEEP}" stroke="{CYAN}" stroke-width="1.5"/>
  <text x="834" y="96" fill="{CYAN}" font-family="Consolas, monospace" font-size="13">SIGNAL -- LAB</text>
  <text x="834" y="122" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="12">Mr-X-Sentinel</text>
  <text x="834" y="144" fill="{CYAN}" font-family="Consolas, monospace" font-size="11">Discord bot platform</text>
  <text x="834" y="166" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">mod | eco | XP | AI</text>
  <text x="834" y="186" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">music | tickets</text>
  <circle cx="1000" cy="130" r="5" fill="{CYAN}">
    <animate attributeName="opacity" values="1;0.3;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="1012" y="134" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">bot</text>

  <line x1="834" y1="206" x2="1056" y2="206" stroke="{STROKE_C}"/>
  <text x="834" y="230" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">CONNECT</text>
  <text x="834" y="254" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">Discord user</text>
  <text x="834" y="274" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">guns.lol</text>
  <text x="834" y="294" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">PayPal | Revolut</text>

  <rect x="834" y="318" width="210" height="36" rx="6" fill="#071018" stroke="{GREEN}"/>
  <text x="848" y="340" fill="{GREEN}" font-family="Consolas, monospace" font-size="11">FACTORY = ONLINE</text>

  <!-- footer honesty -->
  <text x="40" y="396" fill="{MUTED}" font-family="Consolas, monospace" font-size="10">crafted board -- decorative status only | no fake chat | no fake git diffs | dual-split BUILD green / QA cyan</text>
</svg>
'''


def write_readme(placeholder_sha: str = "PENDING") -> None:
    sha = placeholder_sha
    body = f'''<div align="center">

# `>_ mr-aurevo-x@workshop:~`

**AI-run workshop - Cursor builds | Mr-Aurevo-X QA | Windows factory**

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/{sha}/assets/hero-boot.svg?v={sha}" alt="Boot console scrolling" width="100%"/>

<br/>

[![GitHub followers](https://img.shields.io/github/followers/Mr-Aurevo-X?style=for-the-badge&logo=github&logoColor=39ff14&color=050807&labelColor=071410)](https://github.com/Mr-Aurevo-X)
[![Profile views](https://komarev.com/ghpvc/?username=Mr-Aurevo-X&style=for-the-badge&color=00f0ff&label=VISITORS)](https://github.com/Mr-Aurevo-X)
[![Cursor AI](https://img.shields.io/badge/BUILT_BY-CURSOR_AI-39ff14?style=for-the-badge&labelColor=050807&logo=cursor&logoColor=39ff14)](https://cursor.com)
[![Mr-Aurevo-X QA](https://img.shields.io/badge/IDEAS_%26_QA-MR--AUREVO--X-00f0ff?style=for-the-badge&labelColor=050807)](https://github.com/Mr-Aurevo-X)

`STATUS=ONLINE` | `VITRINE=public` | `ATELIER+SALON+LAB=private` | `MODE=AI_OPERATED` | `COLOR=DUAL_SPLIT`

</div>

---

## sessions - dual console

<div align="center">

<table>
  <tr>
    <td width="50%" align="center">
      <img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/{sha}/assets/console-build.svg?v={sha}" alt="Cursor AI build console (green)" width="100%"/>
    </td>
    <td width="50%" align="center">
      <img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/{sha}/assets/console-qa.svg?v={sha}" alt="Mr-Aurevo-X QA console (cyan)" width="100%"/>
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
> **EN** - Cursor AI builds & operates. Mr-Aurevo-X brings ideas, stress-tests, and the green light.

---

## workshop floor

Single crafted factory board (dual-split: **BUILD green** / **QA cyan**). Decorative status only -- not live CI, not live chat.

<div align="center">

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/{sha}/assets/factory-floor.svg?v={sha}" alt="Workshop factory floor status board" width="100%"/>

</div>

---

## featured - public vitrine

**7 outils desktop | gratuits | locaux (sauf DeviseConvert : taux BCE + cache offline) | `.exe` sans installation**
`public | AI-built | human-tested` | SoT `Dev Central Tree\\Git Vitrine Public\\`

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
|-- atelier/     L'Atelier Windows | PC Command (+30 tools)   [private]
|-- salon/       Game launcher + X titles | forks              [private]
|-- lab/         Lab launcher + R&D | Discordbots | prototypes [private]
`-- vitrine/     7 public desktop tools                        [public]
```

<details>
<summary><strong>full workshop map - arborescences</strong></summary>

<a id="atelier"></a>

### atelier - PC Command

SoT : `L'Atelier Windows\\` | hub **PC Command** | admin UAC | `Lancer.cmd`

```text
L'Atelier Windows/
|-- MrAurevoX-Launcher/     * PC Command hub  (private)
|-- MrAurevoX-UI/           kit UI partage
|-- MrAurevoX-Releases/     packaging / portable
|
|-- * Flagships
|   |-- WinCleaner/         nettoyage | caches | traces | debloat
|   |-- WinAudit/           audit heuristique local
|   `-- DiskMap/            carte disque | doublons
|
|-- system                  AudioDevice | FocusBlock | MonitorInfo | PowerPlan
|                           PrintQueue | ProcessGuard | RestorePoint | ShellKit
|                           StartupX | SysInspect | UninstX | UserSessions
|-- network                 NetAdmin | NetMap | WifiKey
|-- files                   FileGuard | HashCheck | InboxSort | LinkKit
|                           PdfKit | Renamer | ZipTools
|-- config                  CertView | EnvEditor | FontManager | HotkeyList
|-- media                   Capture | ColorPicker | ImgBatch | WallpaperPick
|-- productivity            ClipBoard
`-- tools                   PassGen | RepoRadar | TextLab | Trad-X
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

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/main/assets/github-stats.svg?v=bd7c646" height="165" alt="GitHub stats"/>

<br/>

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/main/assets/github-streak.svg?v=bd7c646" alt="Streak"/>

<br/>

<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Mr-Aurevo-X/output/github-contribution-grid-snake-dark.svg?v=30919088429" alt="Contribution snake" width="100%"/>

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
'''
    README.write_text(body, encoding="utf-8", newline="\n")


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "factory-floor.svg").write_text(factory_svg(), encoding="utf-8", newline="\n")
    # remove obsolete fake triple
    for name in ("console-queue.svg", "console-pulse.svg", "console-who.svg"):
        p = ASSETS / name
        if p.exists():
            p.unlink()
            print("removed", name)
    write_readme("PENDING")
    print("wrote factory-floor.svg + README (PENDING sha)")


if __name__ == "__main__":
    main()
