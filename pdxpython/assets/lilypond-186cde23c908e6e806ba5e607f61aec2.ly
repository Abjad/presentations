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
}