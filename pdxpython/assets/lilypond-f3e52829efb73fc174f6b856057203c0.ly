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
    \new Staff {
        c'8. ~
        e'16 (
        fs'8 ~ )
        d'8 (
        e'16 ~ )
        gs'8.
        f'8. ~
        a'16 (
        b'8 ~ )
        g'8 (
        a'16 ~ )
        cs''8.
        b'8. ~
        ds''16 (
        e''8 ~ )
        c''8
    }
}