# *-* coding: utf-8 *-*
"""AGE -- AudioGame Engine
Main program
"""

import traceback

import core
import tss_platform
import speech


if __name__ == '__main__':
    tss_platform.platform_setup()
    try:
        core.initialize()
        core.run()
    except KeyboardInterrupt:
        speech.terminate()
    except Exception as ex:
        print(f"Uncaught exception: {ex}")
        traceback.print_tb(ex.__traceback__)
