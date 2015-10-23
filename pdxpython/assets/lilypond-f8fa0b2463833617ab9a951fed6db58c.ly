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
    \new Score <<
        \new Staff {
            {
                \time 5/8
                c'8
                r8
                d'4
                e'8
            }
            {
                \time 7/8
                e'8
                r8
                fs'2
                g'8
            }
        }
        \new Staff {
            {
                \time 5/8
                c4.
                b8
                r8
            }
            {
                \time 7/8
                a8
                af8
                bf8
                c'4
                b4
            }
        }
    >>
}