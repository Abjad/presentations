\version "2.19.41"
\language "english"

#(ly:set-option 'relative-includes #t)
\include "../../stylesheets/stylesheet.ily"

#(set-default-paper-size "letter" 'portrait)
#(set-global-staff-size 12)

\layout {
}

\paper {
}

\score {
    \include "../segments.ily"
}
