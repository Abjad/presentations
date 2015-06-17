from abjad import *


### EXAMPLE ONE ###


divisions = [(3, 8), (5, 16), (1, 4), (3, 16)]
rhythm_maker_a = rhythmmakertools.NoteRhythmMaker()

selections = rhythm_maker_a(divisions)
measure = Measure((9, 8), selections)
staff = Staff([measure], context_name='RhythmicStaff')
show(staff)

def make_rhythmic_staff(rhythm_maker, divisions):
    selections = rhythm_maker(divisions)
    measure = Measure((9, 8), selections)
    staff = Staff([measure], context_name='RhythmicStaff')
    return staff

staff = make_rhythmic_staff(rhythm_maker_a, divisions)
show(staff)


### EXAMPLE TWO ###


talea = rhythmmakertools.Talea(
    counts=[1, 2, 3],
    denominator=16,
    )
rhythm_maker_b = rhythmmakertools.TaleaRhythmMaker(talea=talea)

staff = make_rhythmic_staff(rhythm_maker_b, divisions)
show(staff)


### EXAMPLE THREE ###


tie_specifier = rhythmmakertools.TieSpecifier(tie_across_divisions=True)
rhythm_maker_c = new(rhythm_maker_b, tie_specifier=tie_specifier)

staff = make_rhythmic_staff(rhythm_maker_c, divisions)
show(staff)


### EXAMPLE FOUR ###


burnish_specifier = rhythmmakertools.BurnishSpecifier(
    left_classes=(Rest, Note),
    left_counts=(1,),
    )
rhythm_maker_d = new(rhythm_maker_c, burnish_specifier=burnish_specifier)

staff = make_rhythmic_staff(rhythm_maker_d, divisions)
show(staff)


### EXAMPLE FIVE ###


def make_rhythmic_staff(rhythm_maker, divisions, rotation=0):
    selections = rhythm_maker(divisions, rotation=rotation)
    measure = Measure((9, 8), selections)
    staff = Staff([measure], context_name='RhythmicStaff')
    return staff

staff = make_rhythmic_staff(rhythm_maker_d, divisions, rotation=1)
show(staff)

staff = make_rhythmic_staff(rhythm_maker_d, divisions, rotation=2)
show(staff)

staff = make_rhythmic_staff(rhythm_maker_d, divisions, rotation=3)
show(staff)


### EXAMPLE SIX ###


rhythmic_score = Score()
for i in range(8):
    staff = make_rhythmic_staff(rhythm_maker_d, divisions, rotation=i)
    rhythmic_score.append(staff)
    divisions = sequencetools.rotate_sequence(divisions, 1)

show(rhythmic_score)