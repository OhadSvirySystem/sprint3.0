import numpy as np
import sounddevice as sd

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """
    Generate a sine wave at a specific frequency.

    :param frequency: Frequency of the sine wave in Hertz.
    :param duration: Duration of the sine wave in seconds.
    :param sample_rate: Number of samples per second. Defaults to 44100.
    :return: A numpy array containing the sine wave.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

if __name__ == "__main__":
    #check
    duration = 0.1  # Duration for each wave segment in seconds
    sample_rate = 44100

    data = np.array([0, 1, 1, 1, 0, 0, 0, 1, 0, 1,0,1,0,0,0,1,0,0,1,0,0,0,0,1])
    frequencies = {0: 3000, 1: 4000}

    # Pre-generate all sine waves and concatenate them
    sine_waves = np.concatenate([generate_sine_wave(frequencies[val], duration, sample_rate) for val in data])

    # Play the concatenated wave
    sd.play(sine_waves, samplerate=sample_rate)
    sd.wait()  # Wait until the sound has finished playing

    print("Done playing the wave!")
