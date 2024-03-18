import re
import unittest
from FillerCounter import find_first_speaker_line

class TestFirstSpeakerLine(unittest.TestCase):
    def test_first_line_is_speaker(self):
        list = ["First Last:", "words"]
        first_speaker_line = find_first_speaker_line(list)
        self.assertEqual(first_speaker_line, 0)

    def test_first_line_is_not_speaker(self):
        list = ["not in right format", "First Last:", "words"]
        first_speaker_line = find_first_speaker_line(list)
        self.assertEqual(first_speaker_line, 1)