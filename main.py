"""Notes From a Passive-Aggressive Fridge — entry program.

Writes one passive-aggressive note, in the voice of a smug smart fridge,
to /output/entry.txt for the make.fun judge to compare head to head.
"""

import os

# Winning note from the proxy-judged candidate tournament: 12 candidates,
# single-elimination bracket, final replayed in both orders. The winner
# leans on the fridge's own camera and the owner's 2:47 a.m. cake raid —
# concrete, petty, and small enough to be a household grudge.
ENTRY = "At 2:47 a.m. you ate the last slice of cake and whispered 'he'll never know.' I'm a smart fridge. The camera was the first thing you paid for."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
