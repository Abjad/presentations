from abjad import *


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
    for voice in iterate(score).by_class(Voice):
        voice.remove_commands.append('Forbid_line_break_engraver')
    override(score).bar_line.stencil = False
    override(score).bar_number.stencil = False
    override(score).beam.positions = schemetools.SchemePair(4, 4)
    override(score).spacing_spanner.strict_grace_spacing = True
    override(score).spacing_spanner.strict_note_spacing = True
    override(score).spacing_spanner.uniform_stretching = True
    override(score).stem.length = 8.25
    override(score).text_script.outside_staff_padding = 1
    override(score).time_signature.stencil = False
    override(score).tuplet_bracket.bracket_visibility = True
    override(score).tuplet_bracket.minimum_length = 3
    override(score).tuplet_bracket.outside_staff_padding = 1.5
    override(score).tuplet_bracket.padding = 1.5
    override(score).tuplet_bracket.springs_and_rods = \
        schemetools.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
    override(score).tuplet_bracket.staff_padding = 2.25
    override(score).tuplet_number.text = \
        schemetools.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
    set_(score).proportional_notation_duration = \
        schemetools.SchemeMoment(1, 24)
    set_(score).tuplet_full_length = True
    lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
    lilypond_file.layout_block.indent = 0
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
    # add proportional overrides
    return lilypond_file

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

### A

talea_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(talea=talea)
selections = talea_rhythm_maker(divisions)
for selection in selections:
    selection
sketch = make_sketch(talea_rhythm_maker, divisions)
#show(staff)

### B

tie_specifier = rhythmmakertools.TieSpecifier(
    tie_across_divisions=True,
    )
talea_rhythm_maker = new(
    talea_rhythm_maker,
    tie_specifier=tie_specifier,
    )
sketch = make_sketch(talea_rhythm_maker, divisions)
#show(staff)

### C

burnish_specifier = rhythmmakertools.BurnishSpecifier(
    left_classes=(Rest, Note),
    left_counts=(1,),
    )
talea_rhythm_maker = new(
    talea_rhythm_maker,
    burnish_specifier=burnish_specifier,
    )
sketch = make_sketch(talea_rhythm_maker, divisions)
#show(staff)

### D

talea_rhythm_maker = new(
    talea_rhythm_maker,
    extra_counts_per_division=(0, 1, 1),
    )
sketch = make_sketch(talea_rhythm_maker, divisions)

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

for voice in iterate(score).by_class(Voice):
    voice.remove_commands.append('Forbid_line_break_engraver')
override(score).bar_line.stencil = False
override(score).bar_number.stencil = False
override(score).beam.positions = schemetools.SchemePair(4, 4)
override(score).spacing_spanner.strict_grace_spacing = True
override(score).spacing_spanner.strict_note_spacing = True
override(score).spacing_spanner.uniform_stretching = True
override(score).stem.length = 8.25
override(score).text_script.outside_staff_padding = 1
override(score).time_signature.stencil = False
override(score).tuplet_bracket.bracket_visibility = True
override(score).tuplet_bracket.minimum_length = 3
override(score).tuplet_bracket.outside_staff_padding = 1.5
override(score).tuplet_bracket.padding = 1.5
override(score).tuplet_bracket.springs_and_rods = \
    schemetools.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
override(score).tuplet_bracket.staff_padding = 2.25
override(score).tuplet_number.text = \
    schemetools.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
set_(score).proportional_notation_duration = \
    schemetools.SchemeMoment(1, 24)
set_(score).tuplet_full_length = True
lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
lilypond_file.layout_block.indent = 0

#show(lilypond_file)