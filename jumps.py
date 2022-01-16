##{
import pandas as pd
import numpy as np
from itertools import product
##}

##{
notes_english = [['Ab', 'A', 'A#'],
                 ['Bb', 'B', 'B#'],
                 ['Cb', 'C', 'C#'],
                 ['Db', 'D', 'D#'],
                 ['Eb', 'E', 'E#'],
                 ['Fb', 'F', 'F#'],
                 ['Gb', 'G', 'G#']]
notes_english = pd.DataFrame(notes_english,columns=['flat','natural','sharp'])
notes_spanish = [['La b',   'La ',  'La #'],
                 ['Si b',   'Si ',  'Si #'],
                 ['Do b',   'Do ',  'Do #'],
                 ['Re b',   'Re ',  'Re #'],
                 ['Mi b',   'Mi ',  'Mi #'],
                 ['Fa b',   'Fa ',  'Fa #'],
                 [ 'Sol b', 'Sol ', 'Sol #']]
notes_spanish = pd.DataFrame(notes_spanish,columns=['flat','natural','sharp'])

notes = [['Ab', 'A', 'A#'],
         ['Bb', 'B', 'B#'],
         ['Cb', 'C', 'C#'],
         ['Db', 'D', 'D#'],
         ['Eb', 'E', 'E#'],
         ['Fb', 'F', 'F#'],
         ['Gb', 'G', 'G#']]
# Semitone corresponding to each note, starting from A = 0
semitones = np.array([[-1, 0, 1],
                      [ 1, 2, 3],
                      [ 2, 3, 4],
                      [ 4, 5, 6],
                      [ 6, 7, 8],
                      [ 7, 8, 9],
                      [ 9,10,11]])

# intervals_semitones = list(np.array(range(1,13)).astype(str))
# intervals_tones = list(np.array(intervals_semitones)/2).astype(str)
# intervals_intervals = ['Minor 2nd',
#                        'Major 2nd',
#                        'Minor 3rd',
#                        'Major 3rd',
#                        'Perfect 4th',
#                        'Augmented 4th',
#                        'Perfect 5th',
#                        'Minor 6th',
#                        'Major 6th',
#                        'Minor 7th',
#                        'Major 7th',
#                        'Octave']
# intervals = pd.DataFrame({'semitones':intervals_semitones,
#                           'tones':intervals_tones,
#                           'intervals':intervals_intervals})
# intervals['semitones_numeric'] = intervals.index.values + 1

# english_intervals = product(notes_english, intervals_intervals)

def note_to_semitone(note):
    """
    Simple function to convert from note representation to
    semitone representation, starting from A = 0.
    For example,  'A#' or 'Bb' convert to 1.
    """
    mask_note = (notes == note)
    selected_semitone = np.ma.masked_array(semitones,mask=~mask_note).compressed()
    return selected_semitone

def semitone_to_note(semitone):
    """
    Simple function to convert from semitone representation to
    note representation, starting from A = 0.
    For example,  1 converts to 'A#, Bb'
    """
    semitone = semitone % 12
    mask_semitone = (semitones == semitone) | (semitones == semitone - 12) | (semitones == semitone + 12)
    selected_notes = np.ma.masked_array(notes,mask=~mask_semitone).compressed()
    selected_notes = list(selected_notes)
    selected_notes = ' , '.join(selected_notes)
    return selected_notes

def get_note_after_interval(note,interval,addition):
    """
    Given a note and an interval, get the final note after applying the interval.
    return a tuple of 3 elements with the
    resulting note in the three possible notations.

    Args:
        note(str): original note.
        interval(str): interval.



        interval_format(str): either tones, seminotes or interval.
        addition (bool): if True, perform addition. If not, substraction.

    Returns:
        Tuple of 3 elements with the final note in the 3 possible notations.
    """
    semitone = 
    starting_semitone = notes_semitones[mask_semitones]
    return starting_semitone
#     starting_semitones = notes.set_index(note_format).loc[note,starting_semitones]
#     semitones_in_interval = intervals.set_index(interval_type).loc[interval,semitones_numeric]
#     final_semitones = starting_semitones + semitones_in_interval
#     index = final_semitones / 12
##}

##{
# Generate decks for interval jumps:
# - In English, with intervals in semitones
# - In English, with intervals in tones
# - In English, with intervals in classical names
# - In Spanish, with intervals in semitones
# - In Spanish, with intervals in tones
# - In Spanish, with intervals in classical names

# For each note, you need to generate 12 jumps (12 intervals in semitones make up an octave)
# in 2 directions (up or down).
# 12 notes * 12 jumps * 2 = 288 notes for each format above
##}

##{
get_note_after_interval('F',3,True)
##}

##{
note_to_semitone('F')
##}

##{
semitone_to_note(1)
##}
