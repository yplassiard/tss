# *-* coding: utf8 *-*

# Defines main game constants that can be used everywhere

# Main internal constants
import math
PI = math.pi
DEF_PI_DIVIDE = 160
DEF_ANGLE = (PI / DEF_PI_DIVIDE)

# camera modes
CAMERA_TOP = 1
CAMERA_SIDE = 2

# global configuration
CONFIG_RESOURCE_DIR = "res"
CONFIG_DATA_DIR = "data"
CONFIG_SOUNDS_DIR = "sounds"
CONFIG_PHRASES_DIR = "phrases"
CONFIG_NUMBERS_DIR = "numbers"
CONFIG_STATIONS_DIR = "stations"

INTERVAL_TICK_RESOLUTION = 0.01

# Audio constants
AUDIO_FX_VOLUME = 0.8
AUDIO_FX_SIGNAL_VOLUME = (AUDIO_FX_VOLUME / 1.5)
AUDIO_MUSIC_VOLUME = 0.8
AUDIO_FADE_INTERVAL = 10
AUDIO_STEREO_FIELD_WIDTH = 95
AUDIO_ERROR_SOUND = "error-sound"

SCENE_MINIMUM_INTERVAL = 10

# Specifics to TSS game

DEFAULT_SPACE_BETWEEN_LINE_AND_PLATFORM = 0.5  # meters
DEFAULT_SPEAKER_HEIGHT = 3.0  # meters
