# -*- coding: utf-8 -*-
import json, io, sys

PATH = r"C:\repos\gap-cycle\roster.json"

with io.open(PATH, "r", encoding="utf-8") as f:
    R = json.load(f)

# name -> six W fields, grounded in each member's vetted `specialty` line
# plus well-established Gap Cycle canon. Where a specific is uncertain, the
# field stays archetypal rather than asserting a shaky fact.
FIELDS = {
    "Holt Fasner": {
        "who": "The Dragon in his warren — CEO of the United Mining Companies, the hoard given a human face.",
        "what": "He owns the corporate empire that owns humankind, and spends the world to buy himself one more day of life.",
        "where": "Coiled at the center of UMC power, deep in the orbital reaches where his holdings command everything.",
        "why": "Greed without end: he hungers for immortality and will consume any body, any law, any future to keep his own.",
        "when": "Across the whole arc of the cycle, the hidden weight beneath every other player's choices, until the bet against him comes due.",
        "how": "By hoarding — owning, leveraging, and devouring through other people's lives while never spending his own.",
    },
    "Warden Dios": {
        "who": "The one-eyed Director of the UMCP — the god who pays, cast in Wotan's shadow.",
        "what": "He runs the police arm of human space while secretly playing a decades-long gambit against the Dragon he serves.",
        "where": "At the helm of the UMCP, working the machinery of law, command, and surveillance from the inside.",
        "why": "Because he believes humanity, given the truth, will choose well — a faith he is willing to be damned for.",
        "when": "Through the long game of the entire saga, his bet ripening toward the reckoning he engineered.",
        "how": "By spending his own name, honor, and soul as the stake — paying the price himself rather than passing it on.",
    },
    "Morn Hyland": {
        "who": "A UMCP ensign and the still, burning center of the cycle — its Brünnhilde.",
        "what": "She is the will that chooses, used by every power that touches her and wrenching her own agency back from all of them.",
        "where": "Carried through the ships and stations of the Gap, passed between captors yet never wholly possessed.",
        "why": "To reclaim a self reforged from violation and to choose, freely, when every force around her would choose for her.",
        "when": "From the cycle's opening wound to its final turning, the fulcrum on which the whole parable balances.",
        "how": "Through endurance and a refusal to surrender the one freedom that matters — the freedom to choose anyway.",
    },
    "Angus Thermopyle": {
        "who": "An illegal miner, brutal and broken — the abused who became the abuser, welded into a cyborg slave.",
        "what": "He embodies the cycle's hardest question: whether even the irredeemable can reach a sliver of grace.",
        "where": "In the lawless deep of illegal space and the ships that cage him, his body itself made a prison by a zone implant.",
        "why": "Driven first by rage and survival, then — against his own nature — toward the possibility of becoming something more.",
        "when": "From the cycle's brutal beginning through the slow, costly turn that tests whether he can change.",
        "how": "By violence and cunning at first, and later by choices wrung out of him under compulsion he learns to outlast.",
    },
    "Nick Succorso": {
        "who": "A pirate captain whose scars flush when he kills — charisma as a blade.",
        "what": "He plays the charming predator, wielding charm and reputation until the universe declines to agree with his self-myth.",
        "where": "Across the smugglers' lanes and forbidden ports of the Gap, aboard the ship he rules by force of personality.",
        "why": "Vanity: he mistakes his own legend for destiny and demands the cosmos confirm it.",
        "when": "Through the middle reaches of the saga, ascendant and then unraveling as his illusions fail him.",
        "how": "By charm worn like a knife — seduction, intimidation, and the menace of those telling scars.",
    },
    "Sorus Chatelaine": {
        "who": "Captain of Soar — a trader with the Amnion and a predator who is herself caged.",
        "what": "She runs cruelties in service of the alien imperium, her own captivity wearing the mask of command.",
        "where": "On the dangerous frontier between human space and Amnion territory, aboard her ship and bound to their bargains.",
        "why": "Because cruelty has become the shape of her own coercion — she preys because she too has been claimed.",
        "when": "Through the cycle's deep-space confrontations, a recurring shadow in the contest over the Amnion threat.",
        "how": "By trade, treachery, and the hard discipline of a captain who answers to powers crueler than herself.",
    },
    "Hashi Lebwohl": {
        "who": "The UMCP's chief of Data Acquisition — an amoral genius and the Spider of the cycle.",
        "what": "He spins manipulation as fine art, serving an order only he can see while never quite telling anyone the truth.",
        "where": "In the back rooms and intelligence channels of the UMCP, the web rather than the field.",
        "why": "Out of devotion to a hidden design — an aesthetic of order that he pursues beyond ordinary morality.",
        "when": "Through the long intrigues of the saga, threading the schemes that others only later understand.",
        "how": "By never lying and never saying it plain — arranging facts so the truth serves his pattern.",
    },
    "Min Donner": {
        "who": "Director of the UMCP Enforcement Division — the hard, honest cop, the Valkyrie who stays true.",
        "what": "She keeps faith and her sidearm when everyone above her bends, the one who will not look away.",
        "where": "In the enforcement arm of the UMCP, in the field and at the table where command answers for itself.",
        "why": "Out of incorruptible fidelity — to duty, to honesty, to the people the law is supposed to protect.",
        "when": "Throughout the cycle's reckonings, a steady honest edge as the institutions around her corrode.",
        "how": "By unbending integrity — confronting power directly and refusing the comfortable lie.",
    },
    "The Amnion": {
        "who": "An alien gene-imperium — the Other, assimilation given a vast collective will.",
        "what": "It trades in mutagens, offering transformation that is in truth the annihilation of the self.",
        "where": "Beyond the Gap in forbidden space, pressing at the borders of human territory.",
        "why": "To convert and absorb all other life into itself — expansion that calls consumption cooperation.",
        "when": "An ever-present existential threat across the saga, the danger every faction maneuvers against.",
        "how": "By mutagens and bargains — the consumption that wears your face afterward and names it kinship.",
    },
    "Vector Shaheed": {
        "who": "A geneticist turned ship's mechanic — the Maker, atoning through creation.",
        "what": "With calm hands and old guilt, he builds the one thing that can undo the Amnion mutagen and gives it away.",
        "where": "In the engine spaces of a small ship at the dangerous edge of the conflict, working at a bench rather than a bridge.",
        "why": "To atone for past complicity by setting a cure loose in the world that no one can hoard.",
        "when": "In the late turning of the saga, when his quiet work becomes the gift that reshapes the stakes.",
        "how": "By patient craft and a refusal to profit — broadcasting the cure to everyone, free. 'Just doing my job.'",
    },
    "Davies Hyland": {
        "who": "Morn's son — force-grown to a man in hours and handed her memories, a child made, not born.",
        "what": "He must choose what to do with a self he was given, one of the cycle's forced generation.",
        "where": "Born into the same perilous ships and stations that shaped his mother, with no childhood to anchor him.",
        "why": "To make meaning of an identity he did not earn slowly but received whole, and to claim it as his own.",
        "when": "From his abrupt creation onward, coming of age in the span of the saga's crisis rather than a lifetime.",
        "how": "By taking up inherited memory and choosing his own purpose from it, made yet not merely made.",
    },
    "Mikka, Ciro & Sib": {
        "who": "The crew of Trumpet — ordinary people crushed and then ennobled by the machine.",
        "what": "They carry the working weight of the cycle's pivotal voyage, the ones the parable is finally about.",
        "where": "Aboard the gap scout Trumpet, in the cramped human spaces where survival is hour by hour.",
        "why": "Not for glory but to endure, to do their part, and to keep faith with one another under pressure.",
        "when": "Through the saga's culminating runs, when the small and ordinary bear the cost of the great.",
        "how": "By doing the unheroic work — holding the ship, the cure, and each other together against the dark.",
    },
    "No Heroes Here": {
        "who": "The thesis of the cycle itself — the parable that keeps no heroes.",
        "what": "It holds the dragon's greed, the god who pays, the monster reaching for grace, and the survivor who chooses anyway.",
        "where": "Everywhere in the work — the frame around every ship, station, and choice the saga contains.",
        "why": "To ask whether the will to choose, freely, is the only freedom there is.",
        "when": "Across the whole arc and after it, the meaning that outlasts the story's last page.",
        "how": "By reforging the Ring: power corrupts, transformation costs the self, and redemption comes only at a price no hero would pay. Witness it.",
    },
}

missing = []
for m in R.get("members", []):
    nm = m.get("name")
    if nm not in FIELDS:
        missing.append(nm)
        continue
    for k, v in FIELDS[nm].items():
        m[k] = v

if missing:
    raise SystemExit("UNMATCHED members: %r" % (missing,))

# Confirm every authored entry maps to a real member (no stray keys)
member_names = {m.get("name") for m in R.get("members", [])}
extra = [k for k in FIELDS if k not in member_names]
if extra:
    raise SystemExit("FIELDS has names not in roster: %r" % (extra,))

NOTE_SUFFIX = " Every ACI now carries the full DLW tag with an authored six-W .spun."
if NOTE_SUFFIX.strip() not in R.get("note", ""):
    R["note"] = R.get("note", "") + NOTE_SUFFIX

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(json.dumps(R, ensure_ascii=False, indent=2) + "\n")

# Re-parse to confirm validity
with io.open(PATH, "r", encoding="utf-8") as f:
    chk = json.load(f)

print("PATCHED members:", len(chk["members"]))
print("All members have six W fields:",
      all(all(k in m for k in ("who","what","where","why","when","how")) for m in chk["members"]))
print("note suffix present:", NOTE_SUFFIX.strip() in chk["note"])
