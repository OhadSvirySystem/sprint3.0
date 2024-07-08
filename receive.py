import numpy as np
import sounddevice as sd
from scipy.fftpack import fft
import transmit as tr

def record_wave(duration, sample_rate=44100):
    """
    Record audio from the microphone.

    :param duration: Duration of the recording in seconds.
    :param sample_rate: Number of samples per second. Defaults to 44100.
    :return: A numpy array containing the recorded audio.
    """
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  # Wait until the recording is done
    print("Recording done!")
    return recording.flatten()

def decode_wave(recording, segment_duration, sample_rate=44100):
    """
    Decode a recorded wave into a data array based on frequency detection.

    :param recording: Numpy array containing the recorded audio.
    :param segment_duration: Duration of each segment in seconds.
    :param sample_rate: Number of samples per second. Defaults to 44100.
    :return: List containing the decoded data.
    """
    segment_length = int(segment_duration * sample_rate)
    num_segments = len(recording) // segment_length
    data = []
    
    for i in range(num_segments):
        segment = recording[i*segment_length:(i+1)*segment_length]
        segment_fft = fft(segment)
        freqs = np.fft.fftfreq(len(segment), 1/sample_rate)
        
        # Get the peak frequency
        peak_freq = abs(freqs[np.argmax(np.abs(segment_fft))])
        
        if peak_freq < (tr.FREQUENCIES[0]+tr.FREQUENCIES[1])/2:  # Compare with the average of the two frequencies
            data.append(0)
        elif peak_freq < (tr.FREQUENCIES[1]+tr.FREQUENCIES[2])/2:
            data.append(1)
        else:
            data.append(2)
            
    
    return data

if __name__ == "__main__":
    # Parameters
    duration_per_segment = tr.DURATION/tr.SAMPLES_PER_BIT  # Duration for each wave segment in seconds
    sample_rate = tr.SAMPLE_RATE
    numOfBits = 200  # Number of bits to transmit
    total_segments = numOfBits*tr.SAMPLES_PER_BIT # Total number of segments in the transmitted data

    # Record the incoming signal
    recorded_wave = record_wave(total_segments * duration_per_segment, sample_rate)

    # Decode the recorded wave
    decoded_data = decode_wave(recorded_wave, duration_per_segment, sample_rate)
    # Find the start signal
    start_index = decoded_data.index(2)

    # Find the stop signal
    stop_index = decoded_data.index(2, start_index + 1)

    # Extract the bits
    bits = decoded_data[start_index + 1:stop_index]

    # Convert the bits to bytes
    bytes = []
    for i in range(0, len(bits), tr.SAMPLES_PER_BIT):
        byte = bits[i:i+tr.SAMPLES_PER_BIT]
        bytes.append(byte)

    print("Bytes:", bytes)
    print("Decoded data:", decoded_data)
