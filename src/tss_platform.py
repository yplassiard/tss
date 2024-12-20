"""
TSS - Train Station Simulator - platform specific setup
"""

import platform


def platform_setup() -> None:
    """Setup environment variables and paths for the current platform
    """
    import os
    import platform
    try:
        machine = platform.machine()  # arm64 / amd64 / x86
        system = platform.system()  # Windows / Linux / Mac
        system = system.lower()

        cur_dir = os.getcwd()  # our base directory to look for resources

        # Set up FMod requirements
        fmod_lib = 'fmod.dll'
        if system == 'windows':
            fmod_lib = 'fmod.dll'
        elif system == 'linux':
            fmod_lib = 'libfmod.so'
        elif system == 'darwin':
            fmod_lib = 'fmod.dylib'
        else:
            raise RuntimeError("Unsupported platform: {system}")
        fmod_path = os.path.join(cur_dir, "res", system, machine, fmod_lib)
        os.environ["PYFMODEX_DLL_PATH"] = fmod_path
    except Exception as ex:
        print(f"Failed to setup dependencies: {ex}")
        raise ex
