\new Score{
    \new PianoStaff<<
        \new Staff<<
            \new Voice{ \voiceOne c''4 d'' e'' f''}
            \new Voice{ \voiceTwo a'4 f' g' d'  }
            >>
        \new Staff<<
        \clef bass
            \new Voice{ \voiceOne c'4 c' c' c'}
            \new Voice{ \voiceTwo c' a b a }
            >>
        >>
}
