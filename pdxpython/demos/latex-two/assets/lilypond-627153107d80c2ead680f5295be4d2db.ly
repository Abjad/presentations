\version "2.19.0"
\language "english"

#(set-global-staff-size 12)

\header {
    tagline = \markup {}
}

\layout {
    indent = #0
    ragged-right = ##t
    \context {
        \Score
        \remove Bar_number_engraver
        \override SpacingSpanner #'strict-grace-spacing = ##t
        \override SpacingSpanner #'strict-note-spacing = ##t
        \override SpacingSpanner #'uniform-stretching = ##t
        \override TupletBracket #'bracket-visibility = ##t
        \override TupletBracket #'minimum-length = #3
        \override TupletBracket #'padding = #2
        \override TupletBracket #'springs-and-rods = #ly:spanner::set-spacing-rods
        \override TupletNumber #'text = #tuplet-number::calc-fraction-text
        proportionalNotationDuration = #(ly:make-moment 1 24)
        tupletFullLength = ##t
    }
}

\paper {
    left-margin = 1\in
}

\score {
    \new Staff {
        c'4
        d'4
        e'4
        f'4
    }
}