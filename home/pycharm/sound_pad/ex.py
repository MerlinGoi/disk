import sounddevice as sd
import numpy as np
from pydub import AudioSegment

# Find the virtual cable output
print(sd.query_devices())

# Replace this with your actual VB-Cable output device index
virtual_output_index = 4

audio = AudioSegment.from_file("я так зделал,и оно работет.mp3")
audio = audio.set_channels(2).set_frame_rate(44100)

samples = np.array(audio.get_array_of_samples()).astype(np.float32) / (2**15)
samples = samples.reshape(-1, audio.channels)

# Play to the "CABLE Input" device
sd.play(samples, samplerate=44100, device=virtual_output_index)
sd.wait()