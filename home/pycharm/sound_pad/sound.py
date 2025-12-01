import sounddevice as sd
import soundfile as sf


def play_to_mic(path, device_name=None):
    """
    Play an audio file to a virtual microphone or input device.

    Parameters:
    - path: str, path to the audio file (wav, flac, etc.)
    - device_name: str or int, optional. Name or index of the input device.
                   If None, plays to default input device.
    """
    # Load audio file
    data, samplerate = sf.read(path, dtype='float32')

    # If device_name is given, find its index
    if device_name is not None:
        devices = sd.query_devices()
        device_index = None
        for i, dev in enumerate(devices):
            if dev['max_input_channels'] > 0 and device_name.lower() in dev['name'].lower():
                device_index = i
                break
        if device_index is None:
            raise ValueError(f"Input device '{device_name}' not found.")
    else:
        device_index = None  # use default input device

    # Play audio to the input device (virtual mic)
    sd.play(data, samplerate, device=device_index)
    sd.wait()
    print(f"Finished playing {path} to device {device_name or 'default input'}")
