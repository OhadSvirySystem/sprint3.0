import numpy as np
import sounddevice as sd
from scipy.fftpack import fft
import transmit as tr

from collections import Counter

def most_common_int(lst):
    if not lst:
        return None  # Handle the case where the list is empty
    counter = Counter(lst)
    most_common = counter.most_common(1)  # Get the most common element and its count
    return most_common[0][0]  # Return the element itself

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

def find_first_and_last_sequence(lst, sequence):
    sequence_length = len(sequence)
    first_index = None
    last_index = None

    for i in range(len(lst) - sequence_length + 1):
        if lst[i:i+sequence_length] == sequence:
            if first_index is None:
                first_index = i
            last_index = i

    return first_index, last_index

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
    numOfBits = 40  # Number of bits to transmit
    total_segments = numOfBits*tr.SAMPLES_PER_BIT # Total number of segments in the transmitted data

    # Record the incoming signal
    recorded_wave = record_wave(total_segments * duration_per_segment, sample_rate)

    # Decode the recorded wave
    decoded_data = decode_wave(recorded_wave, duration_per_segment, sample_rate)
    start_index,stop_index = find_first_and_last_sequence(decoded_data, [2]*3)

    # Extract the bits
    bits = decoded_data[start_index + 1:stop_index]

    # Convert the bits to bytes
    bytes = []
    for i in range(0, len(bits), tr.SAMPLES_PER_BIT):
        byte = bits[i:i+tr.SAMPLES_PER_BIT]
        bytes.append(most_common_int(byte))

    print("Bytes:", bytes)
    print("Decoded data:", decoded_data)



