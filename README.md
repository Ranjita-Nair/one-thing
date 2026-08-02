
# one-thing

For anyone who has sat at 11pm with fourteen tabs open, four hours gone,
and nothing started — and concluded it was a character flaw.

It isn't. It's a starting problem.

A to-do list shows you everything you haven't done.
This shows you exactly one thing, phrased small enough to actually begin.

## Run it

    python3 one_thing.py                     # get your one thing
    python3 one_thing.py add reply to Priya  # capture a task in three seconds

Tasks live in `tasks.txt`, one per line. It isn't in this repo — mine are mine,
yours are yours. The program makes do without it.

## Status

Reads a real file now. Survives blank lines, stray whitespace, and the file not
being there at all. Capture is fast enough that I actually use it.

Still picks by a crude rule: shortest task wins. That's a guess wearing a
decision's clothes. Next it gets an LLM, and something closer to judgement about
what "startable" really means.
