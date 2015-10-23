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
        a''8. -\accent (
        b''8 ~ )
        e'8 -\accent (
        f'8. ~ )
        c'''16 -\accent (
        d'''4 )
        a'4 -\accent (
        b'16 ~ )
        fs'''8. -\accent (
        g'''8 ~ )
        c''8 -\accent
    }
}