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
}