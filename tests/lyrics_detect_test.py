from antiroller import lyrics_detect as ld

lyrics = ld.lyrics

weird_lyrics = [
    ".NEVER. GONNA. GIVE .YOU. UP.",
    ".n.",
    "Nev ergon nagi ve youu p"
]

def test_check_lyrics_default():
    for line in lyrics:
        assert ld.check_lyrics(line) == True

def test_weird_lyrics():
    assert ld.check_lyrics(".NEVER. GONNA. GIVE .YOU. UP.") == True
    assert ld.check_lyrics(".n.") == True