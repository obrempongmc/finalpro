import pyaudio
import wave

# Constants for audio recording
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16  # Format of the audio samples
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 16000  # Sampling rate (number of samples per second)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream for recording
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,  # Specify that this is an input stream (for recording)
    frames_per_buffer=FRAMES_PER_BUFFER  # Specify the buffer size for each read operation
)

# Print a message to indicate that recording is starting
print("Starting Recording")

# Set the duration of the recording (in seconds)
seconds = 5

# Initialize a list to store the recorded audio frames
frames = []

# Loop to record audio for the specified duration
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    # Read audio data from the stream and append it to the frames list
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

# Stop the audio stream
stream.stop_stream()

# Close the audio stream
stream.close()

# Terminate the PyAudio instance to release resources
p.terminate()

# Save the recorded audio to a WAV file
# Open a new WAV file in write mode
obj = wave.open("output.wav", "wb")
# Set the number of audio channels
obj.setnchannels(CHANNELS)
# Set the sample width (in bytes) based on the audio format
obj.setsampwidth(p.get_sample_size(FORMAT))
# Set the sample rate
obj.setframerate(RATE)
# Write the audio frames to the WAV file
obj.writeframes(b"".join(frames))
# Close the WAV file
obj.close()
