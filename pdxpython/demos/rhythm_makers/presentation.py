from abjad import *


def make_sketch_lilypond_file(component):
    for voice in iterate(component).by_class(Voice):
        voice.remove_commands.append('Forbid_line_break_engraver')
    override(component).bar_line.stencil = False
    override(component).bar_number.stencil = False
    override(component).beam.positions = schemetools.SchemePair(4, 4)
    override(component).spacing_spanner.strict_grace_spacing = True
    override(component).spacing_spanner.strict_note_spacing = True
    override(component).spacing_spanner.uniform_stretching = True
    override(component).stem.length = 8.25
    override(component).text_script.outside_staff_padding = 1
    override(component).time_signature.stencil = False
    override(component).tuplet_bracket.bracket_visibility = True
    override(component).tuplet_bracket.minimum_length = 3
    override(component).tuplet_bracket.outside_staff_padding = 1.5
    override(component).tuplet_bracket.padding = 1.5
    override(component).tuplet_bracket.springs_and_rods = \
        schemetools.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
    override(component).tuplet_bracket.staff_padding = 2.25
    override(component).tuplet_number.text = \
        schemetools.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
    set_(component).proportional_notation_duration = \
        schemetools.SchemeMoment(1, 24)
    set_(component).tuplet_full_length = True
    lilypond_file = lilypondfiletools.make_basic_lilypond_file(component)
    lilypond_file.layout_block.indent = 0
    return lilypond_file


def make_sketch(rhythm_maker, divisions):
    # rhythmic creation
    selections = rhythm_maker(divisions)
    voice = Voice(selections)
    staff = Staff([voice], context_name='RhythmicStaff')
    score = Score([staff])
    lilypond_file = make_sketch_lilypond_file(score)
    return lilypond_file


__all__ = [
    'make_sketch',
    'make_sketch_lilypond_file',
    ]