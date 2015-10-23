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
                    c'8 \< \p
                    r8
                    d'4
                    e'8 ~
                }
                {
                    \time 7/8
                    e'8
                    r8
                    fs'2
                    g'8 \f
                }
            }
            \context Staff = "Lower Staff" {
                {
                    \time 5/8
                    c4.
                    b8
                    r8
                }
                {
                    \time 7/8
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/4 {
                        c8
                        a8
                        af8
                        bf8
                    }
                    c'4
                    b4
                }
            }
        >>
    >>
}