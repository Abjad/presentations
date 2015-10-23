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
    \new Score <<
        \new Staff {
            {
                \time 5/8
                c'8
                    - \markup {
                        \circle
                            0
                        }
                r8
                    - \markup {
                        \circle
                            2
                        }
                d'4
                    - \markup {
                        \circle
                            3
                        }
                e'8
                    - \markup {
                        \circle
                            5
                        }
            }
            {
                \time 7/8
                e'8
                    - \markup {
                        \circle
                            7
                        }
                r8
                    - \markup {
                        \circle
                            9
                        }
                fs'2
                    - \markup {
                        \circle
                            11
                        }
                g'8
                    - \markup {
                        \circle
                            15
                        }
            }
        }
        \new Staff {
            {
                \time 5/8
                c4.
                    - \markup {
                        \circle
                            1
                        }
                b8
                    - \markup {
                        \circle
                            4
                        }
                r8
                    - \markup {
                        \circle
                            6
                        }
            }
            {
                \time 7/8
                a8
                    - \markup {
                        \circle
                            8
                        }
                af8
                    - \markup {
                        \circle
                            10
                        }
                bf8
                    - \markup {
                        \circle
                            12
                        }
                c'4
                    - \markup {
                        \circle
                            13
                        }
                b4
                    - \markup {
                        \circle
                            14
                        }
            }
        }
    >>
}