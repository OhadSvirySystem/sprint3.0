import numpy as np
import sounddevice as sd
DURATION = 0.3
SAMPLE_RATE = 44100
FREQUENCIES = {0: 2000, 1: 4000,2:6000}
SAMPLES_PER_BIT = 6

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
    startSignal = [2]*5
    data = np.array([0, 1, 1, 1, 0, 0, 0, 1, 0, 1,0,1,0,0,0,1,0,0,1,0,0,0,0,1])
    data = [0,1]*30
    data = startSignal + data + startSignal
    print("Data to transmit:", data)
    print("length of data:", len(data))
    # Pre-generate all sine waves and concatenate them
    sine_waves = np.concatenate([generate_sine_wave(FREQUENCIES[val], DURATION, SAMPLE_RATE) for val in data])

    # Play the concatenated wave
    sd.play(sine_waves, samplerate=SAMPLE_RATE)
    sd.wait()  # Wait until the sound has finished playing

    print("Done playing the wave!")
