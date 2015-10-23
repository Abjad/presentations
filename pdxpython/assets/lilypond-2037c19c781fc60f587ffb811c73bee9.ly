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
        c'4
        d'4
        e'4
        f'4
        g'4
        a'4
        b'4
        c''4
    }
}