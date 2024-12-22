"""
TSS - Train Station Simulator

Speech module
"""

import os
import threading

class SpeechSystem:
    """self-voicing speech system
    """
    _speak_queue : list[str] = []
    _is_speaking: bool = False
    _should_quit: bool = False
    _quit_lock: Threading.RLock = threading.RLock()
    _speech_path: str | None = None

    def __init__(self, path: str, *args, **kwargs) -> Self:
        super().__init__(*args, **kwargs)
        if not os.path.exists(path):
            raise RuntimeError(f"Speech init failed: {path} not found")

    def run(self) -> None:
        """ Runs the speech thread, waiting for something to speak"""
        quit = _should_quit
        while quit is False:
            with self._quit_lock:
                quit = self._should_quit
            try:
                data = self._queue.get_nowait()
            except queue.Empty:
                time.sleep(0.1)  # sleep for 10ms to avoid CPU usage
                continue
            if not isinstance(data, list):
                data = [data]
            self._speak_queue.extend(data)
            
def initialize() -> bool:
    """Initializes our home-made speech system
    """
    import gameconfig

    return True

def cancelSpeech() -> None:
    """Cancels the currently speaking item(s)
    """

def speak(item: str | list[str], interrups: bool = False) -> bool:
    """ Queues the given item(s) for sreaking.
    """
    if isinstance(item, str):
        item = [item]
    for it in item:
        print(f"Speaking {it}")
    return True
