### PDX Python

## Introduction

- Who am I?
    - A composer and programmer.
    - My education: Harvard, MIT, Oberlin.
- Why am I here?
    - How I came to programming?
    - How I came to Python: Abjad
- What is Abjad?
    - Read the Abjad blurb.

## Background

- Historical context of Abjad.
    - Mozart's Dice Game
    - Birth of computer-assisted composition (CAC)
    - Xenakis and Fortran
        - https://www.youtube.com/watch?v=AE1M2iwjTsM
    - Also, IRCAM, Murail, Saariaho, Ferneyhough
    - David Cope
- The current landscape is heavily DSP-driven:
    - Heavy representation by Lisp-descended languages
    - OpenMusic, PWGL
    - Max, PD, SuperCollider
- History of Abjad's development.
    - A variety of attempts at finding or making a typesetter.
- Python, LilyPond and LaTeX
    - Why Python?
        - Don't hide from programming.
        - Other people are smarter than you.
        - It gets out of the way.
        - It's interpreted.
        - There's a lot of people using it, and a healthy ecosystem.
    - Demo LaTeX
    - Demo LilyPond

## Examples, part I

- Making simple rhythms and pitches

## Reprise

- What is Abjad? What isn't Abjad?
    - A library for modeling notation.
    - (Hopefully) non-opinionated.
    - Typesetting-oriented.
    - Totally deterministic.
    - No AI, no magic.
    - No audio (just optional MIDI)
    - No floating point (just rationals)
- Abjad and Python's ecosystem:
    - Sphinx
    - Pytest
    - PLY
    - Six
- Why would you work like this?
    - To find new ways of doing things (to get away from yourself).
    - To integrate outside information into your work.
    - To automate workflows.
    - To trace the origin of all objects.
    - To re-use work from one piece into another explicitly.
    - Maybe it's just how you think.

## Object model and usage

- Components: Container and Leaves
- Attachments: Indicator and Spanner
- Contexts and Indicator Scope
- Atomic Data Types: Pitch, Duration, Octave, Accidental
- Protocols: Illustration
- Interacting with the score: Agents and Interfaces
- Typographic overrides.
- Modeling LilyPond files.

## Examples, part II

## A small concert

## Documenting with Abjad

- Abjad's development has been highly documentation-driven.
- Graphviz and ReST models
- IPython
- Abjad-book & LaTeX
- Sphinx
- Documentation tools

## Document processing: a teaser

- The canonical score layout
- Segment makers, segments, materials
- The IDE

## Conclusion

- Recap the intro 
- Who are we?
- Where can you read more?