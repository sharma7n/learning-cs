# simple demo of python unit testing
# class under test will be the 'Piano' class, with the following UML definition:

# ----------------
# | Piano        |
# ----------------
# | type         |
# | manufacturer |
# | ------------ |
# | sound        |
# ----------------

# The piano being modeled has a very simplistic keyboard that only consists of one octave starting at middle C.

import unittest


class PianoTestCase(unittest.TestCase):

    def setUp(self):
        self.piano = Piano('baby_grand', 'kawai')

    def test_sound_single_key(self):
        ''' A single key, when played, will return Pitch number corresponding to that key. '''

        self.assertEqual(self.piano.sound('c'), 10)
        self.assertEqual(self.piano.sound('C'), 10)
        
    def test_sound_multiple_keys(self):
        ''' Multiple keys, when played together, will return an array of Pitch numbers corresponding to each key. 
            Multiple instances of the same key only produce one pitch. 
            Expected and actual values of the sound function are wrapped in set() since the order of the pitches does not matter. '''
        
        self.assertEqual(set(self.piano.sound('c', 'e', 'g')), set([10, 30, 50]))
        self.assertEqual(self.piano.sound('c', 'c', 'c'), 10)
        self.assertEqual(set(self.piano.sound('c', 'c', 'd', 'd', 'd')), set([10, 20]))

    def test_sound_null_key(self):
        ''' If a key is not played, no sound is returned. '''
        
        self.assertIsNone(self.piano.sound())

    def test_sound_invalid_key(self):
        ''' If a non-existent key is played, a KeyError is raised. '''

        self.assertRaises(KeyError, self.piano.sound, 'x')
        self.assertRaises(KeyError, self.piano.sound, 'cdefgab')
        self.assertRaises(KeyError, self.piano.sound, 5)


class Piano:

    NOTE_PITCHES = { # these values are entirely made-up.
        'c' : 10,
        'd' : 20,
        'e' : 30,
        'f' : 40,
        'g' : 50,
        'a' : 60,
        'b' : 70,
    }

    def __init__(self, piano_type, manufacturer):
        self.piano_type = piano_type
        self.manufacturer = manufacturer

    def sound(self, *notes):
        ''' Returns the pitch(es) produced by pressing a key or set of keys on the piano. '''

        pitches = {}

        for note in notes:
            try:
                note = note.lower()
            except AttributeError:
                pass
            pitches[note] = Piano.NOTE_PITCHES[note]

        if len(pitches) == 0:
            return None
        elif len(pitches) == 1:
            return list(pitches.values())[0]
        else:
            return list(pitches.values())

if __name__ == '__main__':
    unittest.main()