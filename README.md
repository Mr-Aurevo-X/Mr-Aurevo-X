<div align="center">

# `>_ mr-aurevo-x@workshop:~`

**Atelier d’outils locaux** — Cursor construit · Mr-Aurevo-X teste et valide  
gratuit · autant local que possible

<a href="#windows"><img src="https://img.shields.io/badge/WINDOWS-PC_Command-39ff14?style=for-the-badge&labelColor=050807" alt="Windows"/></a>
<a href="#linux"><img src="https://img.shields.io/badge/LINUX-Command_+_hubs-00f0ff?style=for-the-badge&labelColor=050807" alt="Linux"/></a>
<a href="#ia"><img src="https://img.shields.io/badge/IA-atelier-39ff14?style=for-the-badge&labelColor=050807&logo=cursor&logoColor=39ff14" alt="IA"/></a>

</div>

---

Outils **sans compte**, pensés pour tourner **chez toi**.  
L’IA écrit le code. Je cadre, je casse, je signe.

**EN** — Local-first tools. Cursor builds. I QA and ship.

---

<a id="windows"></a>

## Windows

### PC Command — c’est quoi

**PC Command**, c’est **4 hubs** (pas un seul .exe fourre-tout).  
Chaque hub = une fenêtre admin, modules du même thème, zip portable `Launch-Hub-*.zip`, UAC.  
**Autant local que possible** : pas de compte, pas de télémétrie ; la vérif de version GitHub est optionnelle / désactivable.

**Public** · PolyForm Noncommercial 1.0.0 · **v2.0.0**

| Hub | Rôle | Visibilité |
|:--|:--|:--|
| [Système](https://github.com/Mr-Aurevo-X/Hub-Systeme) | ménage · RAM · process · désinstall | **public** |
| [Réseau](https://github.com/Mr-Aurevo-X/Hub-Reseau) | adaptateurs · carte · traffic · Wi‑Fi | **public** |
| [Sécurité](https://github.com/Mr-Aurevo-X/Hub-Securite) | FileGuard · CertView · RepoRadar · WinAudit | **public** |
| [Utilitaires](https://github.com/Mr-Aurevo-X/Hub-Utilitaires) | UtilKit + MediaKit | **public** |

SmartScreen possible : binaires **non signés**.

<div align="center">
<img src="https://raw.githubusercontent.com/Mr-Aurevo-X/Hub-Systeme/main/docs/screenshots/dashboard.png" alt="Hub Système — accueil" width="720"/>
</div>

### Standalones

| App | Rôle | Visibilité | Version |
|:--|:--|:--|:--|
| [QrTools](https://github.com/Mr-Aurevo-X/QrTools) | QR simple + lot | **public** | v2.0.0 |
| [UnitConvert](https://github.com/Mr-Aurevo-X/UnitConvert) | unités + devises (BCE + cache offline) | **public** | v2.0.0 |
| [TimeTools](https://github.com/Mr-Aurevo-X/TimeTools) | horodatage · chrono · Pomodoro | **public** | v2.0.0 |
| [PixClean](https://github.com/Mr-Aurevo-X/PixClean) | strip EXIF / GPS / XMP | **public** | v2.0.0 |
| [GameChangelog](https://github.com/Mr-Aurevo-X/GameChangelog) | patch notes Steam | **public** | v1.0.3 |
| [Game Lounge](https://github.com/Mr-Aurevo-X/Game-Lounge) | hub de jeux web (28 \*-X, site statique) | **privé** | — |
| [SoftTunes](https://github.com/Mr-Aurevo-X/SoftTunes) | prépa session + HUD FPS *(pas un booster)* | **public** | v2.0.2 |
| [LocalDock](https://github.com/Mr-Aurevo-X/LocalDock) | racines de confiance · scan · loopback | **public** | v0.1.0 |

---

<a id="linux"></a>

## Linux

### Linux Command — c’est quoi

**Linux Command**, c’est le **commander / launcher optionnel** (Tauri) : grille des hubs, install copier-coller, vérif GitHub en lecture seule.  
Les hubs sont des **apps GTK 4 autonomes** — tu n’es pas obligé d’installer le launcher.

| App | Rôle | Visibilité | Version |
|:--|:--|:--|:--|
| [Linux Command](https://github.com/Mr-Aurevo-X/Linux-Command) | launcher / commander (optionnel) | **privé** | v0.2.0 |
| [Hub Système](https://github.com/Mr-Aurevo-X/Hub-Systeme-Linux) | santé · process · paquets · disques · journaux | **privé** | v1.0.0 |
| [Hub Réseau](https://github.com/Mr-Aurevo-X/Hub-Reseau-Linux) | interfaces · flotte · diagnostic | **privé** | v1.0.0 |
| [Hub Sécurité](https://github.com/Mr-Aurevo-X/Hub-Securite-Linux) | audit · secrets · permissions | **privé** | v1.0.0 |
| [Hub Utilitaires](https://github.com/Mr-Aurevo-X/Hub-Utilitaires-Linux) | search · hash · PDF · images · disk map | **privé** | v1.0.0 |
| [Hub Dev](https://github.com/Mr-Aurevo-X/Hub-Dev-Linux) | loopback + ports locaux | **privé** | v1.0.0 |

### Standalones

| App | Rôle | Visibilité | Version |
|:--|:--|:--|:--|
| [Crypto Tracker](https://github.com/Mr-Aurevo-X/crypto-tracker) | surveillance crypto **locale** — pas un exchange, pas d’achat/vente | **privé** (sources) · **binaires publics** | Flatpak [1.2.21](https://github.com/Mr-Aurevo-X/linux-flatpak-releases/releases/tag/crypto-tracker-v1.2.21) · natif [1.2.17](https://github.com/Mr-Aurevo-X/linux-releases/releases/tag/crypto-tracker-v1.2.17) |
| [Game Lounge](https://github.com/Mr-Aurevo-X/Game-Lounge) | hub de jeux web (28 \*-X, site statique) | **privé** | — |

---

<a id="ia"></a>

## IA — atelier

<div align="center">

<img src="assets/ia-matrix.svg" alt="Mr-Aurevo-X — session IA" width="100%"/>

</div>

```diff
+ CURSOR ......... architecture, code, tooling, ship
+ MR-AUREVO-X .... idées, tests réels, QA, feu vert
! RÈGLE .......... si ça sort, l’IA l’a écrit — je l’ai validé
```

L’IA construit et opère. Mr-Aurevo-X apporte les idées, casse / teste, et valide.

**EN** — Cursor AI builds & operates. Mr-Aurevo-X brings ideas, stress-tests, and the green light.

| Projet | Rôle | Visibilité | Version |
|:--|:--|:--|:--|
| [FakeVPS](https://github.com/Mr-Aurevo-X/FakeVPS) | Ubuntu local style VPS | **public** | v1.0.0 |
| [Mr-X Sentinel](https://github.com/Mr-Aurevo-X/Mr-X-Sentinel) | bot Discord self-host | **public** · figé | v2.0.0 |

---

## Sur mesure — création personnalisée

`BY_REQUEST` | `AI_BUILT` | `HUMAN_QA` | `GITHUB_COMPLIANT` | `SCOPE_FIRST`

Logiciels **à la demande**, **toujours via IA** — même règle que le reste de l’atelier : **Cursor construit** · **Mr-Aurevo-X** cadre le brief, teste et **valide**.  
Ce n’est pas une presta « développeur humain au kilo ».

Périmètre typique : utilitaires desktop, outils locaux, scripts / automatisations, intégrations légères.  
Chaque demande reste **conforme** aux [ToS GitHub](https://docs.github.com/site-policy/github-terms/github-terms-of-service), à l’[AUP](https://docs.github.com/site-policy/acceptable-use-policies/github-acceptable-use-policy) et aux [Community Guidelines](https://docs.github.com/site-policy/github-terms/github-community-guidelines) — pas de malware, pas de contournement sécurité / DRM, pas de spam.

Tout **repo public** est et restera **gratuit**. Le sur-mesure se discute en amont (besoin, délais, livrables, privé ou public).

```diff
+ MODEL .......... Cursor AI builds | Mr-Aurevo-X ideas + QA + sign-off
+ IN_SCOPE ....... desktop tools | admin helpers | local-first apps | Discord bots (compliant)
+ PROCESS ........ brief → feasibility → estimate → AI build → human QA → handoff
! OUT_OF_SCOPE ... cheats | cracks | spyware | ToS / AUP violations | "code only by hand / no AI"
```

| | |
|:--|:--|
| **Contact** | [Discord DM](https://discord.com/users/406891052516114442) — décrire le besoin |
| **Livraison** | sources construites par l’IA + chemin de build · QA Mr-Aurevo-X · repo GitHub privé ou public |
| **Stack** | Python · pywebview · PowerShell · GTK / Flatpak · Node / React (selon brief) |
| **Engagement** | pas d’engagement sans accord écrit |

---

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-Mr--Aurevo--X-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=050807)](https://discord.com/users/406891052516114442)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-39ff14?style=for-the-badge&logo=paypal&logoColor=00f0ff&labelColor=050807)](https://www.paypal.com/paypalme/aurevo1)
[![Revolut](https://img.shields.io/badge/Revolut-mr__aurevo__x-00f0ff?style=for-the-badge&logo=revolut&logoColor=39ff14&labelColor=050807)](https://revolut.me/mr_aurevo_x)

**Built by Cursor AI · Ideas & QA by Mr-Aurevo-X**

`end_of_transmission // stay curious`

</div>
