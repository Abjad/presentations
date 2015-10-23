\version "2.19.0"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "../stylesheet.ily"

\header {
    tagline = \markup {}
}

\layout {}

\paper {}

\markup {
    \box
        \pad-around
            #1
            \center-column
                {
                    \bold
                        "Los Angeles"
                    \italic
                        "May - August 2014"
                }
    }