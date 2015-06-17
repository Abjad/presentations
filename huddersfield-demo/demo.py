from abjad import *


### EXAMPLE ONE ###


rhythm_maker_a = rhythmmakertools.NoteRhythmMaker()

divisions = [(3, 8), (5, 16), (1, 4), (3, 16)]

selections = rhythm_maker_a(divisions)
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
sketch = make_make_sketch(rhythm_maker, divisions_b)
show(sketch)

divisions_b *= 20
sketch = make_make_sketch(rhythm_maker, divisions_b)
show(sketch)

### EXAMPLE TWO ###


talea = rhythmmakertools.Talea(
    counts=[1, 2, 3],
    denominator=16,
    )
rhythm_maker_b = rhythmmakertools.TaleaRhythmMaker(talea=talea)

staff = make_make_sketch(rhythm_maker_b, divisions)
show(staff)


### EXAMPLE THREE ###


tie_specifier = rhythmmakertools.TieSpecifier(tie_across_divisions=True)
rhythm_maker_c = new(rhythm_maker_b, tie_specifier=tie_specifier)

staff = make_make_sketch(rhythm_maker_c, divisions)
show(staff)


### EXAMPLE FOUR ###


burnish_specifier = rhythmmakertools.BurnishSpecifier(
    left_classes=(Rest, Note),
    left_counts=(1,),
    )
rhythm_maker_d = new(rhythm_maker_c, burnish_specifier=burnish_specifier)

staff = make_make_sketch(rhythm_maker_d, divisions)
show(staff)


### EXAMPLE FIVE ###


def make_make_sketch(rhythm_maker, divisions, rotation=0):
    selections = rhythm_maker(divisions, rotation=rotation)
    measure = Measure((9, 8), selections)
    staff = Staff([measure], context_name='RhythmicStaff')
    return staff

staff = make_make_sketch(rhythm_maker_d, divisions, rotation=1)
show(staff)

staff = make_make_sketch(rhythm_maker_d, divisions, rotation=2)
show(staff)

staff = make_make_sketch(rhythm_maker_d, divisions, rotation=3)
show(staff)


### EXAMPLE SIX ###


rhythmic_score = Score()
for i in range(8):
    staff = make_make_sketch(rhythm_maker_d, divisions, rotation=i)
    rhythmic_score.append(staff)
    divisions = sequencetools.rotate_sequence(divisions, 1)

show(rhythmic_score)