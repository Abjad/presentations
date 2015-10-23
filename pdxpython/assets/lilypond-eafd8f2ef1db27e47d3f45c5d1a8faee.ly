\version "2.19.0"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "../stylesheet.ily"

\header {
    tagline = \markup {}
}

\layout {}

\paper {}

\score {
    \context Score = "Score" <<
        \context StaffGroup = "Staff Group" <<
            \context Staff = "Upper Staff" {
                {
                    \time 5/8
                    \tempo 4=56
                    c'8 -\accent \< \p
                    r8
                    d'4 -\accent (
                    e'8 ~
                }
                {
                    \time 7/8
                    e'8 )
                    r8
                    fs'2 -\accent (
                    g'8 \f )
                }
            }
            \context Staff = "Lower Staff" \with {
                \override NoteHead #'style = #'slash
                \override StaffSymbol #'line-positions = #'(-4 . 4)
            } {
                {
                    \time 5/8
                    a8. -\staccato ~
                    a8. -\staccato
                    gs'8 (
                    r16 -\staccato )
                    r16 (
                }
                {
                    \time 7/8
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/4 {
                        a8
                        \tweak #'edge-height #'(0.7 . 0)
                        \times 2/3 {
                            c'16 -\staccato ~ )
                        }
                        \tweak #'edge-height #'(0.7 . 0)
                        \times 2/3 {
                            c'8 (
                        }
                        f'8
                        \tweak #'edge-height #'(0.7 . 0)
                        \times 2/3 {
                            c'16 -\staccato ~ )
                        }
                        \tweak #'edge-height #'(0.7 . 0)
                        \times 2/3 {
                            c'8 (
                        }
                    }
                    a'8 -\staccato ~ )
                    a'8 (
                    gs'16 -\staccato ~ )
                    gs'8. -\staccato
                }
            }
        >>
    >>
}