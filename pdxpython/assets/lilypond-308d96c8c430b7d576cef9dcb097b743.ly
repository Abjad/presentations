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
        c'4 -\accent (
        d'16 ~ )
        d''8. -\accent (
        e''8 ~ )
        e'8 -\accent (
        f'8. ~ )
        f''16 -\accent (
        g''4 )
        a'4 -\accent (
        b'16 ~ )
        b''8. -\accent (
        c'''8 ~ )
        c''8 -\accent
    }
}