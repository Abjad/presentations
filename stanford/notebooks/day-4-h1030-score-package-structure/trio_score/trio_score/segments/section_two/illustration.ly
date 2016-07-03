% 2016-07-02 16:47

\version "2.19.41"
\language "english"

\include "../../stylesheets/stylesheet.ily"

\header {}

\layout {}

\paper {}

\score {
    \context Score = "Example Score" <<
        \context Staff = "Example Staff" {
            \context Voice = "Example Voice" {
                c'4 (
                d'4
                e'4
                f'4 )
            }
        }
    >>
}