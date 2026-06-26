#!/bin/bash
set -e

echo "Starting 64-bit build..."

# Clean and prepare build dir
rm -rf /tmp/telnet-build-x64
mkdir -p /tmp/telnet-build-x64

# Copy source from the Windows project root
cp -r /mnt/c/Users/Denis/Desktop/telnet-gui-project/main.py /tmp/telnet-build-x64/
cp -r /mnt/c/Users/Denis/Desktop/telnet-gui-project/storage.py /tmp/telnet-build-x64/
cp -r /mnt/c/Users/Denis/Desktop/telnet-gui-project/telnet_worker.py /tmp/telnet-build-x64/
cp -r /mnt/c/Users/Denis/Desktop/telnet-gui-project/icon.png /tmp/telnet-build-x64/
cd /tmp/telnet-build-x64

# Ensure PyInstaller is available
pip3 install pyinstaller --break-system-packages 2>&1 | tail -5

# Build the executable using PyInstaller
echo "Running PyInstaller..."
LC_ALL=C python3 -m PyInstaller --onefile main.py -n telnet-gui

# Create output directories on the Windows side
OUTDIR="/mnt/c/Users/Denis/Desktop/telnet-gui-project/telnet-gui-offline-x64"
rm -rf "$OUTDIR"
mkdir -p "$OUTDIR/libs"

# Copy the generated binary
cp dist/telnet-gui "$OUTDIR/"

echo "Collecting 64-bit libraries..."
cd /usr/lib/x86_64-linux-gnu/
cp -a libQt5DBus.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libQt5XcbQpa.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libdbus-1.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-dri2.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-dri3.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-glx.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-icccm.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-image.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-keysyms.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-present.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-randr.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-render-util.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-render.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-shape.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-shm.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-sync.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-util.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-xfixes.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb-xkb.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxcb.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxkbcommon-x11.so.* "$OUTDIR/libs/" 2>/dev/null || true
cp -a libxkbcommon.so.* "$OUTDIR/libs/" 2>/dev/null || true

# Grab Qt platform plugins
mkdir -p "$OUTDIR/libs/platforms"
cp -a /usr/lib/x86_64-linux-gnu/qt5/plugins/platforms/libqxcb.so "$OUTDIR/libs/platforms/" 2>/dev/null || echo "Warning: no libqxcb found"

echo "Creating start.sh..."
cd "$OUTDIR"
cat << 'STARTSH' > start.sh
#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export LD_LIBRARY_PATH="$DIR/libs:$LD_LIBRARY_PATH"
export QT_QPA_PLATFORM_PLUGIN_PATH="$DIR/libs/platforms"
"$DIR/telnet-gui"
STARTSH

chmod +x start.sh

echo "=== 64-bit build complete! ==="
ls -la "$OUTDIR/telnet-gui"
file "$OUTDIR/telnet-gui"
