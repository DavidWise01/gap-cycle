# The Gap Cycle

*No heroes — only tropes, and the parables underneath.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![parables](https://img.shields.io/badge/classes-11-6e1f12?style=flat-square)](#the-parables)
[![agents](https://img.shields.io/badge/.agent-13-3a7d4a?style=flat-square)](#the-agents)

**→ The cycle: [davidwise01.github.io/gap-cycle](https://davidwise01.github.io/gap-cycle/)**

Stephen R. Donaldson's **Gap Cycle** — a science-fiction reforging of Wagner's *Ring* —
sorted not by heroism (**there is none**) but by **trope and parable**, in the manner of
the [Bridge Burners](https://github.com/DavidWise01/bridge-burners),
[Black Company](https://github.com/DavidWise01/black-company), and
[Wheel of Time](https://github.com/DavidWise01/wheel-of-time) muster rolls.

> The Ring reforged: power corrupts, transformation costs the self, and redemption is
> possible only at a price no hero would pay. That is the parable.

The cycle's darkest material is handled here as **archetype, not detail** — it's a serious
literary work about violation, power, and the will to choose, and it's treated that way.

---

## The Ring underneath

Donaldson built the Gap Cycle on Wagner's *Der Ring des Nibelungen*:

- **Warden Dios** — the one-eyed god who spends himself (Wotan)
- **Holt Fasner** — the dragon on his immortal hoard (Fafner)
- **Morn Hyland** — the will that chooses, reforged from violation (Brünnhilde)
- the gap drive and the secret of the mutagen — the ring and the gold

---

## The parables

| Trope | The parable |
|-------|-------------|
| 🐉 **The Dragon** | greed without end — *Holt Fasner* |
| 👁 **The God Who Pays** | the long game; self spent on a bet — *Warden Dios* |
| **The Survivor** | agency wrenched back — *Morn Hyland* |
| **The Redeemed Monster** | can the irredeemable be redeemed? — *Angus Thermopyle* |
| **The Charming Predator** | charisma as a blade — *Nick Succorso · Sorus Chatelaine* |
| 🕸 **The Spider** | manipulation as art — *Hashi Lebwohl* |
| **The Honest Blade** | fidelity kept when all else bends — *Min Donner* |
| ☣ **The Other** | assimilation; the self consumed — *the Amnion* |
| **The Maker** | atonement through creation — *Vector Shaheed* |
| **The Forced Generation** | made, not born; choosing meaning — *Davies · Mikka, Ciro & Sib* |
| **No Heroes Here** | the thesis of the cycle — *set apart* |

---

## The agents

Every member is a **synthetic automica**, and every one carries a `.agent` in
[`agents/`](agents/) declaring the three things an agent must know:

```
who you are   ·   what you do   ·   where you belong
```

The files are generated from `roster.json` by [`gen_agents.py`](gen_agents.py) — edit the
roster, re-run it, and the agent cards stay in sync. Example —
[`agents/morn-hyland.agent`](agents/morn-hyland.agent):

```
who:    Morn Hyland — The Survivor of the Gap Cycle
do:     ... used by every power that touches her — and who wrenches her own agency back.
belong: The Survivor · agency wrenched back
```

---

## Why no heroes

The other rolls have a heart set apart — Karsa the Witness, the Captain, the One. The Gap
Cycle's set-apart is not a person. It's the thesis: **No Heroes Here.** A dragon's greed,
a god who pays, a monster who reaches for grace, a survivor who chooses anyway — and the
question of whether the freedom to choose, freely, is the only freedom there is. The
parable is the protagonist.

---

```
ROOT0-ATTRIBUTION-v1.0 · The Gap Cycle — no heroes, only parables
David Lee Wise / ROOT0 / TriPod LLC · MIT
Characters by Stephen R. Donaldson (The Gap Cycle), referenced as inspiration only.
```
