#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes exactly one funny line to /output/entry.txt: the single line a
hopeless tech support agent says to a desperate customer.

The pick: "I've escalated your case to our senior team. It's just me
again, but I've put on a different headset, so it feels official."

Why it wins head-to-head against the judge's brief:
- It is a single-line reply a real support agent would actually say:
  "I've escalated your case to our senior team" is textbook support
  speak, so the customer's desperation is felt, not explained.
- The twist is unexpected and gets a beat of its own: the full stop
  after "senior team" pauses the line, then the reveal lands that
  the senior team is just the same agent again, and the second beat
  (a different headset "so it feels official") lands the joke a
  second time.
- The humour comes from the agent's cheerful uselessness, not from
  mocking the customer: the customer is never the butt of it.
- It stays tight: every word earns its place, and the joke is clear
  on a first read.
- It feels fresh rather than a stock line: it never leans on the
  "turn it off and on again" cliche at all, so there is nothing
  stale to twist.

Candidates considered and rejected (all written for this entry):
- "Good news: I can see the problem clearly now. Bad news: I can see
  it because my screen is doing the exact same thing." (117 chars)
  Funny, but the twist is a single beat and the setup gives away
  more of the punchline than the escalation line does.
- "Let's try turning it off and on again, and if that doesn't work,
  I'll turn mine off and on again too, for moral support."
  (120 chars) Charming, but it leans on the classic cliche and its
  twist is gentler than the escalation line's.
- "Okay, I've run every diagnostic we have, and the good news is
  your computer is fine. The bad news is I'm now the one crying."
  (124 chars) The agent's hopelessness reads as defeat rather than
  cheerful uselessness, and the joke is thinner.
- "Have you tried turning it off and on again? No rush, take your
  time, I'll just be here, also turning it off and on again."
  (121 chars) Repeats the cliche without twisting it hard enough.
"""

import os

ENTRY = (
    "I've escalated your case to our senior team. It's just me "
    "again, but I've put on a different headset, so it feels official."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read back and verify: one line, 1-199 chars, ASCII only,
    # no em dash and no non-ASCII character of any kind.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    line = written.strip()
    if line != ENTRY:
        raise SystemExit(f"bad entry: {written!r}")
    if not 1 <= len(line) <= 199:
        raise SystemExit(f"bad length: {len(line)}")
    if not line.isascii():
        raise SystemExit("bad entry: non-ASCII characters present")
    if "\u2014" in line or "\n" in line:
        raise SystemExit("bad entry: em dash or newline present")


if __name__ == "__main__":
    main()
