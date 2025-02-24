
TMP_FILE = "tmp.mid"


def load_note_midi() -> dict[str, int]:
    table: dict[str, int] = {}
    with open("pitches_abc.txt", "r") as fh:
        for line in fh:
            note, _, midi = line.strip().split(",")
            table[note] = int(midi)
    return table


def play(notes):
    import pygame
    from midiutil.MidiFile import MIDIFile

    mf = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    volume = 100

    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 220)

    note_to_midi: dict[str, int] = load_note_midi()

    for t in notes:
        match t:
            case (note, duration):
                mf.addNote(track, channel,
                           note_to_midi[note], time, duration, volume)
                time += duration
            case note:
                mf.addNote(track, channel,
                           note_to_midi[note], time, 1, volume)
                time += 1

    with open(TMP_FILE, 'wb') as fh:
        mf.writeFile(fh)

    pygame.init()
    pygame.mixer.music.load(TMP_FILE)
    pygame.mixer.music.play()
    pygame.time.wait(30000)


# https://thesession.org/tunes/64
reel = [("E", 1), ("F#", 1), ("A", 1), ("A", 1), ("B", 1), ("A", 1), ("F#", 1), ("E", 1), ("D", 1), ("F#", 1),
        ("A", 1), ("A", 1), ("B", 1), ("A", 2), ("d", 1), ("e", 1), ("f#", 1), ("B", 1), ("B", 1), ("A", 1),
        ("B", 1), ("c#", 1), ("d", 1), ("e", 1), ("f#", 1), ("d", 1), ("g", 1), ("f#", 1), ("e", 1), ("f#", 1),
        ("d", 1), ("B", 1), ("F#", 1), ("A", 1), ("A", 1), ("B", 1), ("A", 1), ("F#", 1), ("E", 1), ("D", 1),
        ("F#", 1), ("A", 1), ("A", 1), ("B", 1), ("A", 2), ("d", 1), ("e", 1), ("f#", 1), ("B", 1), ("B", 1),
        ("A", 1), ("B", 1), ("c#", 1), ("D", 1), ("B", 1), ("A", 1), ("F#", 1), ("E", 1), ("F#", 1), ("D", 3),
        ("e", 1), ("f#", 1), ("a", 1), ("a", 1), ("g", 1), ("f#", 1), ("d", 1), ("d", 1), ("e", 1), ("f#", 1),
        ("d", 1), ("a", 1), ("d", 1), ("f#", 1), ("d", 1), ("d", 2), ("e", 1), ("f#", 1), ("g", 1), ("a", 1),
        ("b", 1), ("e", 1), ("e", 1), ("f#", 1), ("g", 1), ("e", 1), ("b", 1), ("e", 1), ("g", 1), ("e", 1),
        ("e", 2), ("f#", 1), ("a", 1), ("a", 1), ("f#", 1), ("b", 2), ("a", 1), ("f#", 1), ("d", 1), ("e", 1),
        ("f#", 1), ("d", 1), ("e", 2), ("d", 1), ("e", 1), ("f#", 1), ("B", 1), ("B", 1), ("A", 1), ("B", 1),
        ("c#", 1), ("d", 1), ("B", 1), ("A", 1), ("F#", 1), ("E", 1), ("F#", 1), ("D", 3)]


c_whistle: list[str] = "C D E F G A A# B".split()
d_whistle: list[str] = "D E F# G A B C C#".split()
a_whistle: list[str] = "A B C# D E F# G G#".split()

# ================================================================================
# Your code starts here:
# --------------------------------------------------------------------------------

# https://docs.python.org/3/tutorial/datastructures.html#sets

# Can G be played on all three whistles?

# What is are the notes in common in the C whistle and the D whistle?

# What is are the notes are in E that are not in D?

# What are all the playable notes?

# What notes are part of the reel?

# Which whistles are able to play the reel? Note that the whistle can play both uppercase and lowercase notes, ex: D whistle can play "F#" and "f#".


# uncomment to hear the reel:
# play(reel)
