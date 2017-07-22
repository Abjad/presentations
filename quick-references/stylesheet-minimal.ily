\version "2.19.0"

#(ly:set-option 'relative-includes #t)

\include "stylesheet.ily"

\layout {
    \context {
        \Score
        \override BarLine.stencil = ##f
        \override TimeSignature.stencil = ##f
    }
}
