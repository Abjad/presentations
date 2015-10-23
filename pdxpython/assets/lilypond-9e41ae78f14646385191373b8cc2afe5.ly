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
    \context Staff = "Upper Staff" {
        {
            \time 5/8
            \tempo 4=56
            c'8 -\accent \< \p
                - \markup {
                    \circle
                        0
                    }
            r8
                - \markup {
                    \circle
                        2
                    }
            d'4 -\accent (
                - \markup {
                    \circle
                        3
                    }
            e'8 ~
                - \markup {
                    \circle
                        5
                    }
        }
        {
            \time 7/8
            e'8 )
            r8
                - \markup {
                    \circle
                        9
                    }
            fs'2 -\accent (
                - \markup {
                    \circle
                        11
                    }
            g'8 \f )
                - \markup {
                    \circle
                        15
                    }
        }
    }
}