from abjad import *


### EXAMPLE ONE ###


rhythm_maker_a = rhythmmakertools.NoteRhythmMaker()

divisions = [(3, 8), (5, 4), (1, 4), (13, 16)]

selections = rhythm_maker_a(divisions)

for selection in selections:
    selection

staff = Staff(selections, context_name='RhythmicStaff')
show(staff)

def make_sketch(rhythm_maker, divisions):
    # rhythmic creation
    selections = rhythm_maker(divisions)
    # instantiating containers
    voice = Voice(selections)
    staff = Staff([voice], context_name='RhythmicStaff')
    score = Score([staff])
    lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
    # applying typographic overrides
    voice.remove_commands.append('Forbid_line_break_engraver')
    override(staff).time_signature.stencil = False
    override(staff).bar_line.stencil = False
    override(score).bar_number.stencil = False
    lilypond_file.layout_block.indent = 0
    return lilypond_file

sketch = make_sketch(rhythm_maker_a, divisions)
show(sketch)

divisions_b = [(5, 16), (3, 8), (3, 8), (5, 8), (1, 4)]
sketch = make_sketch(rhythm_maker, divisions_b)
show(sketch)

divisions_b *= 20
sketch = make_sketch(rhythm_maker, divisions_b)
show(sketch)

import random

random_numerators = [random.randrange(1, 16 + 1) for x in range(100)]
random_divisions = [(x, 32) for x in random_numerators]
sketch = make_sketch(rhythm_maker, random_divisions)

### EXAMPLE TWO ###


talea = rhythmmakertools.Talea(
    counts=[1, 2, 3],
    denominator=16,
    )

for i in range(20):
    print(i, talea[i])

### A

talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(talea=talea)
selections = talea_rhythm_maker(divisions)
for selection in selections:
    selection
sketch = make_sketch(talea_rhythm_maker, divisions)
show(staff)

### B

tie_specifier = rhythmmakertools.TieSpecifier(
    tie_across_divisions=True,
    )
talea_rhythm_maker = new(
    talea_rhythm_maker,
    tie_specifier=tie_specifier,
    )
staff = make_sketch(talea_rhythm_maker, divisions)
show(staff)

### C

burnish_specifier = rhythmmakertools.BurnishSpecifier(
    left_classes=(Rest, Note),
    left_counts=(1,),
    )
talea_rhythm_maker = new(
    talea_rhythm_maker,
    burnish_specifier=burnish_specifier,
    )
staff = make_sketch(talea_rhythm_maker, divisions)
show(staff)


### EXAMPLE THREE ###


#def make_sketch(rhythm_maker, divisions, rotation=0):
#    selections = rhythm_maker(divisions, rotation=rotation)
#    measure = Measure((9, 8), selections)
#    staff = Staff([measure], context_name='RhythmicStaff')
#    return staff
#
#staff = make_sketch(rhythm_maker_d, divisions, rotation=1)
#show(staff)
#
#staff = make_sketch(rhythm_maker_d, divisions, rotation=2)
#show(staff)
#
#staff = make_sketch(rhythm_maker_d, divisions, rotation=3)
#show(staff)


### EXAMPLE THREE ###


score = Score()
for i in range(12):
    selections = talea_rhythm_maker(divisions, rotation=i)
    voice = Voice(selections)
    staff = Staff([voice], context_name='RhythmicStaff')
    score.append(staff)
    divisions = sequencetools.rotate_sequence(divisions, 1)

for voice in iterate(score).by_class(Voice):
    voice.remove_commands.append('Forbid_line_break_engraver')

for staff in iterate(score).by_class(Staff):
    override(staff).time_signature.stencil = False
    override(staff).bar_line.stencil = False

override(score).bar_number.stencil = False
lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
lilypond_file.layout_block.indent = 0

show(lilypond_file)