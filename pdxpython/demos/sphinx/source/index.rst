An abjad-book demo
==================

Blah blah blah.

..  abjad::

    from abjad import *

Blah blah blah.

..  abjad::

    staff = Staff("c'4 d'4 e'4 f'4")
    show(staff)
    attach(Slur(), staff[:])
    show(staff)
    for note in staff:
        print(format(note))

Blah blah blah.

..  abjad::

    graph(staff)