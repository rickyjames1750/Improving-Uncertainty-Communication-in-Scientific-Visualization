# Study Protocol

## Overview

Within-subjects study comparing three uncertainty encodings on a set of
standardized interpretation tasks. Each participant sees all three chart
types and answers the same three task types per chart.

## Participants

- Target: N >= 24 (4 per counterbalancing group)
- Recruitment: convenience sample from the CS department and classmates
- Eligibility: normal or corrected-to-normal vision, comfortable reading
  English

## Procedure

1. Participant opens the survey link.
2. Consent page: brief description of the study, time estimate (~10 min),
   confirmation that responses are anonymous.
3. Demographics: age range, major/field, self-rated data literacy (1-5).
4. Instructions: "You will see three different charts showing penguin
   measurements. For each chart you'll answer three short questions."
5. Trials: 3 blocks (one per encoding), each with 3 tasks (ranking,
   estimation, decision). Encoding order is counterbalanced across
   participants.
6. Post-study: optional open-ended feedback ("Any comments on the charts?").
7. Thank-you page.

## Timing

- Stimulus displayed until participant submits response.
- Time recorded from stimulus onset to response submit (JavaScript
  `performance.now()`).

## Platform

Simple HTML/CSS/JS page. Stimuli are static PNGs embedded in the page.
Responses logged to a JSON file or Google Sheets backend. No server needed
for the prototype (responses can be collected via Google Forms as fallback).

## Consent Language (draft)

> You are invited to participate in a short research study about how people
> read charts. The study takes about 10 minutes. You will view several
> charts and answer questions about them. Your responses are anonymous and
> no personally identifiable information is collected. Participation is
> voluntary and you may stop at any time.

## Files

- `tasks.md` — task definitions and counterbalancing scheme
- `survey.html` — survey prototype (self-contained, open in any browser)
