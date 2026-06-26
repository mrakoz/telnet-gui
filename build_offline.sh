#!/bin/bash
set -e

echo "Starting 32-bit build..."

# === ADJUST THIS PATH to match your WSL mount of the project folder ===
PROJECT_DIR="/mnt/c/Users/<YOUR_USER>/Desktop/telnet-gui-project"
# ===================================================================

# Clean and prepare build dir
rm -rf /root/build
mkdir -p /root/build

# Copy source from the Windows project root
cp -r "$PROJECT_DIR"/main.py /root/build/
cp -r "$PROJECT_DIR"/storage.py /root/build/
cp -r "$PROJECT_DIR"/telnet_worker.py /root/build/
cp -r "$PROJECT_DIR"/icon.png /root/build/
cd /root/build

# Build the executable using PyInstaller
echo "Running PyInstaller..."
LC_ALL=C python3 -m PyInstaller --onefile main.py -n telnet-gui

# Create output directories on the Windows side
OUTDIR="$PROJECT_DIR/telnet-gui-offline-32bit"
rm -rf "$OUTDIR"
mkdir -p "$OUTDIR/libs"

# Copy the generated binary
cp dist/telnet-gui "$OUTDIR/"

echo "Collecting 32-bit libraries..."
cd /usr/lib/i386-linux-gnu/
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
cp -a /usr/lib/i386-linux-gnu/qt5/plugins/platforms/libqxcb.so "$OUTDIR/libs/platforms/" 2>/dev/null || true

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

echo "=== 32-bit build complete! ==="
ls -la "$OUTDIR/telnet-gui"
