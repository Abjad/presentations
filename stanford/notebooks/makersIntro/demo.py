from abjad import *
from presentation import *


### PRE ###


def show_demo():
    talea = rhythmmakertools.Talea(
        counts=[1, 2, 3],
        denominator=16,
        )
    tie_specifier = rhythmmakertools.TieSpecifier(
        tie_across_divisions=True,
        )
    burnish_specifier = rhythmmakertools.BurnishSpecifier(
        left_classes=(Rest, Note),
        left_counts=(1,),
        )
    talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        extra_counts_per_division=[0, 1, 1],
        burnish_specifier=burnish_specifier,
        tie_specifier=tie_specifier,
        )
    divisions = [(3, 8), (5, 4), (1, 4), (13, 16)]
    score = Score()
    for i in range(8):
        selections = talea_rhythm_maker(divisions, rotation=i)
        voice = Voice(selections)
        staff = Staff([voice], context_name='RhythmicStaff')
        score.append(staff)
        divisions = sequencetools.rotate_sequence(divisions, 1)
    lilypond_file = make_sketch_lilypond_file(score)
    show(lilypond_file)

#show_demo()


### EXAMPLE ONE ###


note_rhythm_maker = rhythmmakertools.NoteRhythmMaker()

divisions = [(3, 8), (5, 4), (1, 4), (13, 16)]

selections = note_rhythm_maker(divisions)

for selection in selections:
    selection

staff = Staff(selections, context_name='RhythmicStaff')
#show(staff)

from presentation import *

sketch = make_sketch(note_rhythm_maker, divisions)
#show(sketch)

divisions_b = [(5, 16), (3, 8), (3, 8), (5, 8), (1, 4)]
sketch = make_sketch(note_rhythm_maker, divisions_b)
#show(sketch)

divisions_b *= 20
sketch = make_sketch(note_rhythm_maker, divisions_b)
#show(sketch)

import random
random_numerators = [random.randrange(1, 16 + 1) for x in range(100)]
random_divisions = [(x, 32) for x in random_numerators]
sketch = make_sketch(note_rhythm_maker, random_divisions)


### EXAMPLE TWO ###


talea = rhythmmakertools.Talea(
    counts=[1, 2, 3],
    denominator=16,
    )

#for i in range(20):
#    print(i, talea[i])

### INITIAL TALEA RHYTHM-MAKER

talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(talea=talea)

divisions  # remind ourselves of original divisions

sketch = make_sketch(talea_rhythm_maker, divisions)
#show(staff)

### SPECIFIERS

tie_specifier = rhythmmakertools.TieSpecifier(
    tie_across_divisions=True,
    )

burnish_specifier = rhythmmakertools.BurnishSpecifier(
    left_classes=[Rest],
    left_counts=[1, 0],
    )

extra_counts_per_division = [0, 1, 1]

### TEMPLATED

talea_rhythm_maker = new(
    talea_rhythm_maker,
    burnish_specifier=burnish_specifier,
    extra_counts_per_division=extra_counts_per_division,
    tie_specifier=tie_specifier,
    )

divisions  # remind ourselves of original divisions

sketch = make_sketch(talea_rhythm_maker, divisions)
# show(sketch)


### EXAMPLE THREE ###


score = Score()
for i in range(12):
    selections = talea_rhythm_maker(divisions, rotation=i)
    voice = Voice(selections)
    staff = Staff([voice], context_name='RhythmicStaff')
    score.append(staff)
    divisions = sequencetools.rotate_sequence(divisions, 1)

sketch = make_sketch_lilypond_file(score)

#show(sketch)