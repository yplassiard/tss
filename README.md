# TSS - Train Station Simulator

## Purpose

The purpose of this repository is to create a train station simulator / route planner at first stage, and then leverage on this work to create hopefully a fully-feature train driving system.

## Build and run

To build and run this, you'll need:
- Python (from 3.9 to 3.13)
- a working **pip** tool.

### Prepare your environment

After cloning this repository it is strongly encouraged to create a Python virtual environment:
```bash
cd /path/to/tss
python -m venv .
. ./bin/activate
```

Note: On some systems, especially but not limited to GNU/Linux, you need to use "python3" instead of "python".

### Install dependencies

To install dependencies:
```bash
pip install -r REQUIREMENTS.txt
```

### Run TSS

To run the game:
```bash
python main.py
```

### Notes


Some notes:
- This is not even alpha stage for now, so expect bugs
- Before running the game, be sure to activate the virtual environment. This has to be done each time you open a terminal to run the game:
```bash
. ./bin/activate
```
- The controls are only done for keyboard for now, although jystick support is planned for the future.



## Reporting issues

Any contribution is appreciated, either via issue or pull request.
When the game runs, it generates a file called **tss.log** which contains some information about what is being done. Be sure to include this file while reporting an issue. You may want to flush this file at some point if it becomes too large after many game sessions.
