# Development Guide

This document explains how to build the **Telnet GUI** offline releases from scratch. The build process uses **WSL** (Windows Subsystem for Linux) with Ubuntu containers — the developer machine is Windows, the build environment is Linux under WSL.

## Project Layout

```
~/telnet-gui-project/
├── main.py              # GUI (PyQt5)
├── storage.py           # Profile storage, Export/Import
├── telnet_worker.py     # Telnet engine (async thread)
├── icon.png             # App icon
├── README.md            # User documentation
├── DEVELOPMENT_GUIDE.md # This file
├── build_offline.sh     # Build script for 32-bit (i386) release
├── build_offline_x64.sh # Build script for 64-bit (x86_64) release
├── telnet-gui.deb       # Optional DEB package
│
├── telnet-gui-offline-32bit\   # Output: 32-bit offline build
│   ├── telnet-gui               # PyInstaller binary
│   ├── start.sh                 # Launcher wrapper
│   └── libs/                    # Bundled XCB/Qt libraries
│       └── platforms/
│           └── libqxcb.so
│
└── telnet-gui-offline-x64\     # Output: 64-bit offline build
    ├── telnet-gui
    ├── start.sh
    └── libs/
        └── platforms/
            └── libqxcb.so
```

## Build Architecture (Offline Edition)

The app uses **PyInstaller** to compile Python + PyQt5 into a standalone executable. The tricky part is **XCB graphics libraries** — bare Linux systems often lack them, causing the infamous error:

```
qt.qpa.plugin: Could not load the Qt platform plugin "xcb"
```

### The Fix: `start.sh` + `libs/` folder

1. **PyInstaller** compiles `main.py` into a static binary (`telnet-gui`)
2. **Required `.so` libraries** are collected from the WSL system and placed in a `libs/` folder next to the binary
3. **`start.sh`** launches the binary with `LD_LIBRARY_PATH` pointed at `libs/`, so the dynamic linker finds our bundled libraries first

### `start.sh` wrapper

```bash
#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export LD_LIBRARY_PATH="$DIR/libs:$LD_LIBRARY_PATH"
export QT_QPA_PLATFORM_PLUGIN_PATH="$DIR/libs/platforms"
"$DIR/telnet-gui" "$@"
```

## Build Process (WSL)

Building is done inside **WSL** (Ubuntu) because PyInstaller must produce a Linux binary. The build scripts mount the Windows project folder via `/mnt/c/`, compile the code, collect libraries from `/usr/lib/`, and write the output back to the Windows filesystem.

### Prerequisites (WSL Ubuntu)

```bash
# Inside WSL (Ubuntu 20.04 recommended for glibc compatibility)
sudo apt update
sudo apt install python3 python3-pip pyqt5-dev-tools \
    libxcb-xinerama0 libxcb-icccm4 libxcb-image0 \
    libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 \
    libxcb-shape0 libxcb-xfixes0 libxcb-xkb1 \
    libxkbcommon-x11-0 libdbus-1-3

# PyInstaller
pip3 install pyinstaller --break-system-packages
```

### Building 32-bit (i386)

**Additional setup:** 32-bit build requires a separate WSL instance with Ubuntu i386 or an i386 chroot.

Run `build_offline.sh` inside the 32-bit WSL:

```bash
# Inside 32-bit WSL
bash build_offline.sh
```

The script:
1. Copies source files from the Windows project folder to `/root/build/`
2. Runs `pyinstaller --onefile main.py -n telnet-gui`
3. Copies `.so` libraries from `/usr/lib/i386-linux-gnu/` → output `libs/`
4. Generates `start.sh`
5. Output goes to `~/telnet-gui-project/telnet-gui-offline-32bit/`

### Building 64-bit (x86_64)

Run `build_offline_x64.sh` inside a standard 64-bit WSL:

```bash
# Inside 64-bit WSL
bash build_offline_x64.sh
```

Same process, but libraries come from `/usr/lib/x86_64-linux-gnu/`.

### What the build script collects

| Library path | Purpose |
|-------------|---------|
| `libQt5DBus.so.*` | Qt D-Bus |
| `libQt5XcbQpa.so.*` | Qt XCB platform plugin |
| `libdbus-1.so.*` | D-Bus transport |
| `libxcb*.so.*` | X11 protocol libraries |
| `libxkbcommon*.so.*` | Keyboard handling |
| `libqxcb.so` | Qt platform plugin (→ `libs/platforms/`) |

## Release Packaging

After a successful build, the output directory contains everything needed:

```
telnet-gui-offline-32bit.zip   (or telnet-gui-offline-x64.zip)
├── telnet-gui                  # Compiled binary (~15 MB)
├── start.sh                    # Launcher
├── libs/                       # Bundled system libraries
│   ├── libQt5DBus.so.5
│   ├── libQt5XcbQpa.so.5
│   ├── libxcb*.so.*
│   ├── libxkbcommon*.so.*
│   └── platforms/
│       └── libqxcb.so
```

Zip the folder and upload to GitHub Releases.

## Offline Build Constraints

- **Build on old glibc**: Ubuntu 20.04 is recommended — newer distros produce binaries that won't run on Lubuntu 16.04
- **32-bit vs 64-bit**: Separate WSL instances are needed for each architecture
- **No internet needed on target**: The entire app (binary + libs + launcher) fits in a ZIP that works on a bare offline Linux machine

## Debugging

If the app crashes on a new Linux system, run with verbose Qt logging:

```bash
QT_DEBUG_PLUGINS=1 ./start.sh
```

This prints exactly which `.so` file is missing. Copy the missing library from a working system into `libs/`.

Common missing files:
- `libxcb-xinerama.so.0` — many minimal systems lack this
- `libxkbcommon-x11.so.0` — keyboard compositing
