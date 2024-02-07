import unittest
from ..src.transient import transient_tracker


class TestTransientTracker(unittest.TestCase):

    def test_transient_tracker_with_default_filename(self):
        # Arrange
        expected_tempo = 129.19921875  # Replace with the expected tempo value for the default audio file
        # Act
        result = transient_tracker()
        # Assert
        self.assertEqual(result, expected_tempo)

    def test_transient_tracker_with_custom_filename(self):
        # Arrange
        custom_filename = "data/audio.wav"  # Replace with a custom audio file path
        expected_tempo = 129.19921875  # Replace with the expected tempo value for the custom audio file
        # Act
        result = transient_tracker(custom_filename)
        # Assert
        self.assertEqual(result, expected_tempo)


if __name__ == "__main__":
    unittest.main()
