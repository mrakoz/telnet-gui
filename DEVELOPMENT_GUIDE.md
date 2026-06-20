# Development & AI Context Guide

This document is intended for human developers and **AI Assistants (Agents)** who will work on this project in the future. It explains the core architecture, the build process, and the specific hacks we implemented to ensure 100% offline compatibility on Linux.

## 🤖 Note to Future AI Agents
If you are an AI assistant starting a new conversation with the user to modify this utility:
1. **Do NOT break the offline build system.** We specifically moved away from `.deb` packages and `apt` dependencies because the user requires this application to run on completely "naked" and offline Linux installations (e.g., barebones Lubuntu 16.04).
2. **Do NOT suggest using package managers.** The app must remain a self-contained ZIP archive.
3. Read the "Build Architecture" section carefully before modifying how the app starts.

## Project Overview
**Telnet GUI** is a fast, native, and modern Telnet client for Linux, built with Python 3 and PyQt5.
- **UI Framework:** PyQt5.
- **Networking:** Asynchronous thread-based engine to prevent UI freezing during slow connections.

## Build Architecture (Ultimate Offline Edition)
The biggest challenge in this project was making the PyQt5 GUI run on minimal Linux systems without an internet connection. By default, PyInstaller does not bundle low-level X11/XCB graphics libraries, causing `qt.qpa.plugin: Could not load the Qt platform plugin "xcb"` errors.

### The Solution: `start.sh` + `libs/` folder
To solve this, we implemented a standalone "portable" architecture:
1. **The Binary:** We compile the python code using PyInstaller (`pyinstaller --onefile ...`).
2. **The Libraries (`libs/`):** We manually extracted all required XCB dependencies (e.g., `libqxcb.so`, `libxcb-xinerama.so.0`, `libQt5XcbQpa.so.5`) and placed them in a `libs` directory next to the executable.
3. **The Wrapper (`start.sh`):** The user launches the app via `start.sh`. This script dynamically sets the `LD_LIBRARY_PATH` environment variable to point to our `libs/` folder.

**Why this works:** Setting `LD_LIBRARY_PATH` forces the Linux dynamic linker to load our bundled libraries *first*. If the host system lacks an XCB library, the app seamlessly uses ours. 

### Contents of `start.sh`
```bash
#!/bin/bash
# Get the absolute path of the directory containing this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Force the system to look for libraries in our custom 'libs' folder first
export LD_LIBRARY_PATH="$DIR/libs:$LD_LIBRARY_PATH"

# Force Qt to look for platform plugins in the libs/platforms folder
export QT_QPA_PLATFORM_PLUGIN_PATH="$DIR/libs/platforms"

# Run the PyInstaller binary
"$DIR/telnet-gui" "$@"
```

## How to Create a Release
If you need to compile a new version:
1. Make sure you build on an older Linux system (e.g., Ubuntu 20.04 or 16.04) to ensure maximum forward compatibility with glibc versions.
2. Setup a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pyqt5 pyinstaller
   ```
3. Compile the code:
   ```bash
   pyinstaller --onefile --windowed --name telnet-gui main.py
   ```
4. Package the resulting `telnet-gui` binary together with the `start.sh` script and the pre-existing `libs/` folder into a ZIP archive.

## Debugging
If the app fails to start on a new Linux system, run `start.sh` with maximum Qt logging enabled:
```bash
QT_DEBUG_PLUGINS=1 ./start.sh
```
This will print exactly which `lib*.so` file is missing. You can then copy the missing library from a working system into the `libs/` folder.
