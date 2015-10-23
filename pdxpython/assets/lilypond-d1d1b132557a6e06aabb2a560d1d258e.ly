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
        c'4 (
        d'16 ~ )
        fs'8. (
        gs'8 ~ )
        e'8 (
        f'8. ~ )
        a'16 (
        b'4 )
        a'4 (
        b'16 ~ )
        ds''8. (
        e''8 ~ )
        c''8
    }
}