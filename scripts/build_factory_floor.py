# -*- coding: utf-8 -*-
"""Generate factory-floor.svg (dual-split green/cyan) and rewrite README.

README.md is the SoT for the dual Windows/Linux vitrine. This script must
emit that same structure (4 public hubs + WIN/LIN featured) so a re-run cannot
regress to the old flat catalogue.
"""
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
    # Dual WIN/LIN factory board — keep in lockstep with assets/factory-floor.svg
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="460" viewBox="0 0 1100 460" role="img" aria-label="Workshop factory floor crafted status board">
  <defs>
    <linearGradient id="floorBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#030605"/>
      <stop offset="50%" stop-color="{BG}"/>
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

  <rect width="1100" height="460" fill="url(#floorBg)"/>
  <rect width="1100" height="460" fill="url(#grid)"/>
  <rect x="12" y="12" width="1076" height="436" rx="14" fill="{BG}" stroke="url(#split)" stroke-width="2"/>

  <!-- title bar -->
  <rect x="24" y="24" width="1052" height="36" rx="6" fill="{DEEP}" stroke="{STROKE_G}"/>
  <text x="40" y="47" fill="{SOFT_G}" font-family="Consolas, ui-monospace, monospace" font-size="14">workshop floor -- factory status board</text>
  <text x="780" y="47" fill="{MUTED}" font-family="Consolas, ui-monospace, monospace" font-size="11">CRAFTED SHOWCASE</text>
  <text x="930" y="47" fill="{CYAN}" font-family="Consolas, ui-monospace, monospace" font-size="11">NOT LIVE CI</text>

  <!-- LEFT: dual lanes BUILD / QA -->
  <rect x="24" y="72" width="250" height="340" rx="8" fill="{DEEP}" stroke="{GREEN}" stroke-width="1.5"/>
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
  <text x="40" y="386" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">WIN .exe + LIN binaries</text>

  <!-- CENTER: mounts + dual tickers -->
  <rect x="286" y="72" width="520" height="340" rx="8" fill="{DEEP}" stroke="{STROKE_C}" stroke-width="1.5"/>
  <text x="302" y="96" fill="{CYAN}" font-family="Consolas, monospace" font-size="13">MOUNTS -- Dev Central Tree</text>

  <!-- mount chips row 1 (atelier public · lounge private · softtunes public · changelog public) -->
  <rect x="302" y="112" width="100" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="316" y="129" fill="{CYAN}" font-family="Consolas, monospace" font-size="11">atelier</text>
  <rect x="410" y="112" width="100" height="26" rx="4" fill="#071410" stroke="{GREEN}"/>
  <text x="428" y="129" fill="{GREEN}" font-family="Consolas, monospace" font-size="11">lounge</text>
  <rect x="518" y="112" width="108" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="528" y="129" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">softtunes</text>
  <rect x="634" y="112" width="124" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="642" y="129" fill="{CYAN}" font-family="Consolas, monospace" font-size="9">changelog</text>

  <!-- mount chips row 2 (public) -->
  <rect x="302" y="146" width="108" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="314" y="163" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">vitrine</text>
  <rect x="418" y="146" width="108" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="442" y="163" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">linux</text>
  <rect x="534" y="146" width="108" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="548" y="163" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">fakevps</text>
  <rect x="650" y="146" width="108" height="26" rx="4" fill="#071018" stroke="{CYAN}"/>
  <text x="662" y="163" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">sentinel</text>

  <text x="302" y="184" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">ATELIER  | 4 hubs + LocalDock v0.1.0</text>
  <text x="302" y="200" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">LOUNGE   | Game Lounge web | 28 *-X</text>
  <text x="302" y="216" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">SOFTTUNES| v2.0.0 public | session</text>
  <text x="302" y="232" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">GCHANGELOG| v1.0.3 public | Steam notes</text>
  <text x="302" y="248" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">FAKEVPS  | 1.0.0 final | public src</text>
  <text x="302" y="264" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">WIN      | 4 desktop .exe | PolyForm</text>
  <text x="302" y="280" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">LINUX    | 3 apps | binaries only</text>

  <line x1="302" y1="286" x2="786" y2="286" stroke="{STROKE_C}"/>
  <text x="302" y="306" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">WIN TICKER</text>
  <text x="520" y="306" fill="{CYAN}" font-family="Consolas, monospace" font-size="12">LIN TICKER</text>

  <clipPath id="tickWin"><rect x="302" y="314" width="484" height="24" rx="4"/></clipPath>
  <rect x="302" y="314" width="484" height="24" rx="4" fill="#030605" stroke="{STROKE_G}"/>
  <g clip-path="url(#tickWin)" font-family="Consolas, monospace" font-size="12" fill="{GREEN}">
    <text x="310" y="331">
      QrTools  |  UnitConvert  |  TimeTools  |  PixClean  |  QrTools  |
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-520 0" dur="22s" repeatCount="indefinite"/>
    </text>
  </g>

  <clipPath id="tickLin"><rect x="302" y="346" width="484" height="24" rx="4"/></clipPath>
  <rect x="302" y="346" width="484" height="24" rx="4" fill="#030605" stroke="{STROKE_C}"/>
  <g clip-path="url(#tickLin)" font-family="Consolas, monospace" font-size="12" fill="{CYAN}">
    <text x="310" y="363">
      Crypto Tracker  |  Gest Linux Pro  |  MrAurevoX Kit  |  native + Flatpak  |  Crypto Tracker  |
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-420 0" dur="18s" repeatCount="indefinite"/>
    </text>
  </g>

  <text x="302" y="388" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">rule: if it ships, AI wrote it -- Mr-Aurevo-X signed it off</text>
  <text x="302" y="404" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">SoT: Dev Central Tree | Hub-* + SoftTunes + GameChangelog public</text>

  <!-- RIGHT: ship channel + connect -->
  <rect x="818" y="72" width="258" height="340" rx="8" fill="{DEEP}" stroke="{CYAN}" stroke-width="1.5"/>
  <text x="834" y="96" fill="{CYAN}" font-family="Consolas, monospace" font-size="13">SHIP -- PER REPO</text>
  <text x="834" y="122" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="12">Hub-* Releases</text>
  <text x="834" y="144" fill="{CYAN}" font-family="Consolas, monospace" font-size="11">Launch-Hub-*.zip each remote</text>
  <text x="834" y="166" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">SoftTunes.zip | GameChangelog.zip</text>
  <text x="834" y="186" fill="{MUTED}" font-family="Consolas, monospace" font-size="11">no central installer</text>
  <circle cx="1000" cy="130" r="5" fill="{CYAN}">
    <animate attributeName="opacity" values="1;0.3;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="1012" y="134" fill="{CYAN}" font-family="Consolas, monospace" font-size="10">ok</text>

  <line x1="834" y1="206" x2="1056" y2="206" stroke="{STROKE_C}"/>
  <text x="834" y="230" fill="{GREEN}" font-family="Consolas, monospace" font-size="12">CONNECT</text>
  <text x="834" y="254" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">Discord user</text>
  <text x="834" y="274" fill="{SOFT_G}" font-family="Consolas, monospace" font-size="11">guns.lol</text>
  <text x="834" y="294" fill="{SOFT_C}" font-family="Consolas, monospace" font-size="11">PayPal | Revolut</text>

  <rect x="834" y="330" width="210" height="36" rx="6" fill="#071018" stroke="{GREEN}"/>
  <text x="848" y="352" fill="{GREEN}" font-family="Consolas, monospace" font-size="11">FACTORY = ONLINE</text>
  <text x="834" y="390" fill="{MUTED}" font-family="Consolas, monospace" font-size="10">WIN + LIN public</text>

  <!-- footer honesty -->
  <text x="40" y="436" fill="{MUTED}" font-family="Consolas, monospace" font-size="10">crafted board -- decorative status only | no fake chat | no fake git diffs | dual-split BUILD green / QA cyan</text>
</svg>
'''


# README.md is the SoT. Do not regenerate it from this script
# (a stale template here previously regressed featured tables / mounts).

def write_readme(placeholder_sha: str = "PENDING") -> None:
    raise RuntimeError(
        "README.md is SoT — pin SHAs with pin_and_clean.py, do not rewrite the card"
    )


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "factory-floor.svg").write_text(factory_svg(), encoding="utf-8", newline="\n")
    for name in ("console-queue.svg", "console-pulse.svg", "console-who.svg"):
        p = ASSETS / name
        if p.exists():
            p.unlink()
            print("removed", name)
    # README.md is SoT — do not overwrite (keeps live WIN/LIN featured versions).
    print("wrote factory-floor.svg (README unchanged)")


if __name__ == "__main__":
    main()
