import librosa
from typing import Optional


def transient_tracker(filename: Optional[str] = "data/audio.wav"):
    """
    A function to track transient in audio files.

    Args:
        filename (str, optional): The path to the audio file. Defaults to "data/audio.wav".

    Returns:
        int: The estimated tempo in beats per minute.
    """
    # Step 1: Load the audio file
    y, sr = librosa.load(filename or "data/audio.wav", sr=None)

    # Step 2: Analyze rhythm and tempo directly
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    bpm_string = f"Estimated Tempo: {tempo} BPM"

    # Print or return the BPM as a string
    print(bpm_string)
    return tempo
