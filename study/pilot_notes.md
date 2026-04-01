# Pilot Study Notes

**Date:** March 28-30, 2026
**Participants:** 4 (P01-P04)

## Recruitment
Grabbed 4 classmates/friends: 2 CS, 1 Bio, 1 Stats. Mix of data literacy
levels (2 to 5). Enough to shake out usability issues, not enough for real
analysis.

## What went well
- Survey flow worked without issues. Nobody got confused by the consent or
  demographics pages.
- Task prompts were clear — no one asked "what does this mean?"
- Timing capture worked correctly (checked against manual stopwatch for P01).
- Error bar and violin conditions went smoothly.

## Issues found

### HOPs grid confusion
All four participants mentioned the HOPs grid took longer or was harder to
read. P02 actually got the ranking task wrong on HOPs (picked Gentoo) and the
decision task wrong (said Agree). P01 and P04 both commented on the number
of panels being overwhelming.

Possible fixes:
- Reduce from 20 panels to maybe 9 or 12
- Make the panels bigger (current 4x5 grid is cramped)
- Add a note or label saying "each panel is one possible outcome"

### Estimation task wording
P02 estimated 50.0 for Chinstrap on the violin chart, which is off by about
1.2mm. Not sure if that's a wording issue or just a read error. Everyone
else was within 1mm. Keeping the task as-is for now but will watch this in
the real run.

### Completion time
- P01: ~6 min total
- P02: ~8 min
- P03: ~5 min
- P04: ~7 min

All under the 10-min target, which is good.

### Task carryover / learning effect (from Shelley's U3 feedback)
Shelley pointed out that using the same questions for all three encodings
means participants might remember answers from earlier blocks. This is a
real concern. Counterbalancing the encoding order helps (different people
see different encodings first), but it doesn't eliminate within-person
carryover. Considered using different questions per encoding, but the
problem is that different questions have different difficulty, so any
accuracy difference could be the question rather than the encoding. Decided
to keep the same questions and acknowledge carryover as a limitation in the
paper. The counterbalancing still lets us compare encodings fairly across
participants.

### Results collection (from Shelley's U3 feedback)
Updated the survey to include a "Copy to clipboard" button and a "Download
JSON" button on the thank-you page. After each session, I copy the JSON
and save it to a file. The thank-you screen shows a session id and group
letter so I can match each export to a person.

### Random group assignment (from Shelley's U3 feedback)
First try was localStorage + fixed Latin-square order so everyone gets a
turned-in sequence. That breaks when each person opens the link on their
own phone --- each browser starts fresh. Final approach: Fisher-Yates
shuffle on the three encodings each session (uniform over the same six
orderings as the Latin square). Session id is time-based + random so JSON
exports never collide. Group letter A--F is whichever row the shuffle
matched.

## Changes for the main study
1. Reduce HOPs grid to 12 panels (3x4 layout) and increase panel size.
   Bumped axis font sizes so values are easier to read.
2. Add a one-line caption under the HOPs chart: "Each panel shows one
   plausible outcome from resampling the data."
3. Updated survey.html: copy/download buttons, random shuffle of encodings
   per session, session id in the JSON.
4. No changes to task wording (keeping same tasks, counterbalancing
   mitigates order effects, carryover acknowledged as limitation).
