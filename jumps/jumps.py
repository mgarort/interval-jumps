ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

notes_to_ids = {'A': 0,
                'A#': 1, 'Bb': 1,
                'B': 2,
                'C': 3,
                'C#': 4, 'Db': 4,
                'D': 5,
                'D#': 6, 'Eb': 6,
                'E': 7,
                'F': 8,
                'F#': 9, 'Gb': 9,
                'G': 10,
                'G#': 11, 'Ab': 11,
               }

ids_to_notes = {0: 'A',
                1: 'A# / Bb',
                2: 'B',
                3: 'C',
                4: 'C# / Db',
                5: 'D',
                6: 'D# / Eb',
                7: 'E',
                8: 'F',
                9: 'F# / Gb',
                10: 'G',
                11: 'G# / Ab',
               }

intervals_to_semitones = {}

{'Minor 2nd'     : 1 ,
 'Major 2nd'     : 2 ,
 'Minor 3rd'     : 3 ,
 'Major 3rd'     : 4 ,
 'Perfect 4th'   : 5 ,
 'Augmented 4th' : 6 ,
 'Perfect 5th'   : 7 ,
 'Minor 6th'     : 8 ,
 'Major 6th'     : 9 ,
 'Minor 7th'     : 10,
 'Major 7th'     : 11,
 'Octave'        : 12,
}



##{
intervals = ['Minor 2nd', 'Major 2nd', 'Minor 3rd', 'Major 3rd',
             'Perfect 4th', 'Augmented 4th', 'Perfect 5th', 'Minor 6th',
             'Major 6th', 'Minor 7th', 'Major 7th', 'Octave']
intervals_to_semitones = {k:v for k,v in zip(intervals,range(1,13))}
semitones_to_intervals = {v:k for k,v in intervals_to_semitones.items()}
##}















def note_plus_semitones(note, semitones):
    """
    Given a starting note in letter format and an interval in semitones,
    return the final note.

    Params:
        note(str): starting note
        semitones(int): interval in semitones

    Returns:
        String with name of final note.
    """
    start_id = notes_to_ids[note]
    end_id = (start_id + semitones) % 12
    return ids_to_notes[end_id]
