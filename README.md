# Telnet GUI Client

![Telnet GUI Logo](https://img.shields.io/badge/Telnet-GUI-blue.svg)
![Linux](https://img.shields.io/badge/Linux-Standalone-green.svg)
![Offline Ready](https://img.shields.io/badge/Offline-Ready-orange.svg)

*(ðŸ‡·ðŸ‡º Ð ÑƒÑÑÐºÐ°Ñ Ð²ÐµÑ€ÑÐ¸Ñ Ð½Ð¸Ð¶Ðµ)*

**Telnet GUI** is a fast, native, and modern Telnet client for Linux, built with Python and PyQt5. It features a dark-themed interface, profile management, and an interactive mode for character-by-character communication (useful for MUD games or router configurations).

## Features
- **Export/Import:** Save and restore your entire server list as JSON files â€” handy for backups or transferring profiles between machines.
- **Profile Manager:** Save, edit, and delete server connections (Name, IP, Port).
- **Smart Logs:** Each profile remembers its own terminal output when switching between tabs.
- **Interactive Mode:** Toggle "Interactive Mode" to send keystrokes directly to the server in real time (byte-by-byte), bypassing the need to press Enter.
- **Asynchronous Engine:** The network operations run in a background thread, preventing the UI from freezing even during timeouts or network failures.
- **100% Offline Standalone Build:** The application is packaged to run on entirely barebones Linux systems without an internet connection. It brings its own Python runtime, Qt engine, and low-level X11/XCB libraries.

## Installation

Download the latest release from the [Releases](https://github.com/mrakoz/telnet-gui/releases) page.

Choose the archive for your architecture:
- **`telnet-gui-offline-32bit.zip`** â€” for 32-bit (i386) systems, e.g. Lubuntu/Ubuntu 16.04
- **`telnet-gui-offline-x64.zip`** â€” for 64-bit (x86_64) modern Linux systems

1. Download the zip for your architecture.
2. Extract the archive.
3. Open the extracted folder, double-click on `start.sh` and click **Execute** (or **Execute in Terminal**).

> [!NOTE]
> The `start.sh` script automatically sets up the environment to load the bundled libraries, ensuring it runs on minimal or offline Linux systems without needing `sudo apt install`.

## How to Use
1. Launch the app using `start.sh`.
2. Click **Add** on the left panel to save a new server profile (e.g., `telehack.com`, Port `23`).
3. Select your profile and click **Connect**.
4. Type your commands in the bottom input line and press `Enter` to send.
5. Check the **Interactive Mode** box if you need real-time key capture (useful for text-based UI menus on remote hosts).

---

# Telnet GUI Client (ÐÐ° Ñ€ÑƒÑÑÐºÐ¾Ð¼)

**Telnet GUI** â€” ÑÑ‚Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ð¹, Ð½Ð°Ñ‚Ð¸Ð²Ð½Ñ‹Ð¹ Ð¸ ÑÐ¾Ð²Ñ€ÐµÐ¼ÐµÐ½Ð½Ñ‹Ð¹ Ð³Ñ€Ð°Ñ„Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ Telnet-ÐºÐ»Ð¸ÐµÐ½Ñ‚ Ð´Ð»Ñ Linux. ÐžÐ½ Ð¿Ñ€ÐµÐ´Ð»Ð°Ð³Ð°ÐµÑ‚ ÑÑ‚Ð¸Ð»ÑŒÐ½Ñ‹Ð¹ Ñ‚Ñ‘Ð¼Ð½Ñ‹Ð¹ Ð¸Ð½Ñ‚ÐµÑ€Ñ„ÐµÐ¹Ñ, Ð¼ÐµÐ½ÐµÐ´Ð¶ÐµÑ€ Ð¿Ñ€Ð¾Ñ„Ð¸Ð»ÐµÐ¹ Ð¸ Ð¸Ð½Ñ‚ÐµÑ€Ð°ÐºÑ‚Ð¸Ð²Ð½Ñ‹Ð¹ Ñ€ÐµÐ¶Ð¸Ð¼ Ð´Ð»Ñ Ð¿Ð¾ÑÐ¸Ð¼Ð²Ð¾Ð»ÑŒÐ½Ð¾Ð¹ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐ¸ Ð´Ð°Ð½Ð½Ñ‹Ñ… (Ð¸Ð´ÐµÐ°Ð»ÑŒÐ½Ð¾ Ð´Ð»Ñ MUD-Ð¸Ð³Ñ€ Ð¸Ð»Ð¸ Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ¸ ÑÐµÑ‚ÐµÐ²Ð¾Ð³Ð¾ Ð¾Ð±Ð¾Ñ€ÑƒÐ´Ð¾Ð²Ð°Ð½Ð¸Ñ).

## ÐžÑÐ½Ð¾Ð²Ð½Ñ‹Ðµ Ð²Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ÑÑ‚Ð¸
- **Ð­ÐºÑÐ¿Ð¾Ñ€Ñ‚/Ð˜Ð¼Ð¿Ð¾Ñ€Ñ‚:** Ð¡Ð¾Ñ…Ñ€Ð°Ð½ÑÐ¹Ñ‚Ðµ Ð¸ Ð²Ð¾ÑÑÑ‚Ð°Ð½Ð°Ð²Ð»Ð¸Ð²Ð°Ð¹Ñ‚Ðµ Ð²ÐµÑÑŒ ÑÐ¿Ð¸ÑÐ¾Ðº ÑÐµÑ€Ð²ÐµÑ€Ð¾Ð² Ð² JSON â€” ÑƒÐ´Ð¾Ð±Ð½Ð¾ Ð´Ð»Ñ Ð±ÑÐºÐ°Ð¿Ð¾Ð² Ð¸Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ½Ð¾ÑÐ° Ð¼ÐµÐ¶Ð´Ñƒ Ð¼Ð°ÑˆÐ¸Ð½Ð°Ð¼Ð¸.
- **ÐœÐµÐ½ÐµÐ´Ð¶ÐµÑ€ Ð¿Ñ€Ð¾Ñ„Ð¸Ð»ÐµÐ¹:** Ð¡Ð¾Ñ…Ñ€Ð°Ð½ÑÐ¹Ñ‚Ðµ, Ñ€ÐµÐ´Ð°ÐºÑ‚Ð¸Ñ€ÑƒÐ¹Ñ‚Ðµ Ð¸ ÑƒÐ´Ð°Ð»ÑÐ¹Ñ‚Ðµ Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ¸ ÑÐµÑ€Ð²ÐµÑ€Ð¾Ð² (Ð˜Ð¼Ñ, IP-Ð°Ð´Ñ€ÐµÑ, ÐŸÐ¾Ñ€Ñ‚).
- **Ð£Ð¼Ð½Ñ‹Ðµ Ð»Ð¾Ð³Ð¸:** ÐŸÑ€Ð¸ Ð¿ÐµÑ€ÐµÐºÐ»ÑŽÑ‡ÐµÐ½Ð¸Ð¸ Ð¼ÐµÐ¶Ð´Ñƒ ÑÐ¾Ñ…Ñ€Ð°Ð½Ñ‘Ð½Ð½Ñ‹Ð¼Ð¸ ÑÐµÑ€Ð²ÐµÑ€Ð°Ð¼Ð¸ Ð¸ÑÑ‚Ð¾Ñ€Ð¸Ñ ÐºÐ¾Ð½ÑÐ¾Ð»Ð¸ Ð´Ð»Ñ ÐºÐ°Ð¶Ð´Ð¾Ð³Ð¾ Ð¸Ð· Ð½Ð¸Ñ… Ð±ÐµÑ€ÐµÐ¶Ð½Ð¾ ÑÐ¾Ñ…Ñ€Ð°Ð½ÑÐµÑ‚ÑÑ.
- **Ð˜Ð½Ñ‚ÐµÑ€Ð°ÐºÑ‚Ð¸Ð²Ð½Ñ‹Ð¹ Ñ€ÐµÐ¶Ð¸Ð¼ (Interactive Mode):** Ð’ÐºÐ»ÑŽÑ‡Ð¸Ñ‚Ðµ Ð³Ð°Ð»Ð¾Ñ‡ÐºÑƒ, Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð¿ÐµÑ€ÐµÑ…Ð²Ð°Ñ‚Ñ‹Ð²Ð°Ñ‚ÑŒ Ð½Ð°Ð¶Ð°Ñ‚Ð¸Ñ ÐºÐ»Ð°Ð²Ð¸Ñˆ Ð¸ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ Ð¸Ñ… Ð½Ð° ÑÐµÑ€Ð²ÐµÑ€ Ð² Ñ€ÐµÐ°Ð»ÑŒÐ½Ð¾Ð¼ Ð²Ñ€ÐµÐ¼ÐµÐ½Ð¸ (Ð¿Ð¾Ð±Ð°Ð¹Ñ‚Ð¾Ð²Ð¾) Ð±ÐµÐ· Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼Ð¾ÑÑ‚Ð¸ Ð½Ð°Ð¶Ð¸Ð¼Ð°Ñ‚ÑŒ `Enter`.
- **ÐÑÐ¸Ð½Ñ…Ñ€Ð¾Ð½Ð½Ñ‹Ð¹ Ð´Ð²Ð¸Ð¶Ð¾Ðº:** Ð Ð°Ð±Ð¾Ñ‚Ð° Ñ ÑÐµÑ‚ÑŒÑŽ Ð²Ñ‹Ð½ÐµÑÐµÐ½Ð° Ð² Ñ„Ð¾Ð½Ð¾Ð²Ñ‹Ð¹ Ð¿Ð¾Ñ‚Ð¾Ðº. Ð˜Ð½Ñ‚ÐµÑ€Ñ„ÐµÐ¹Ñ Ð½Ð¸ÐºÐ¾Ð³Ð´Ð° Ð½Ðµ "Ð·Ð°Ð²Ð¸ÑÐ°ÐµÑ‚" Ð¿Ñ€Ð¸ Ð¾Ð¶Ð¸Ð´Ð°Ð½Ð¸Ð¸ Ð¾Ñ‚Ð²ÐµÑ‚Ð° Ð¸Ð»Ð¸ Ð¾Ð±Ñ€Ñ‹Ð²Ð°Ñ… ÑÐ²ÑÐ·Ð¸.
- **100% ÐÐ²Ñ‚Ð¾Ð½Ð¾Ð¼Ð½Ð¾ÑÑ‚ÑŒ (Offline Ready):** ÐŸÑ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸Ðµ ÑƒÐ¿Ð°ÐºÐ¾Ð²Ð°Ð½Ð¾ Ð²Ð¼ÐµÑÑ‚Ðµ Ñ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ð¼ Ð¸Ð½Ñ‚ÐµÑ€Ð¿Ñ€ÐµÑ‚Ð°Ñ‚Ð¾Ñ€Ð¾Ð¼ Python, Ð³Ñ€Ð°Ñ„Ð¸Ñ‡ÐµÑÐºÐ¸Ð¼ Ð´Ð²Ð¸Ð¶ÐºÐ¾Ð¼ Qt Ð¸ Ð±Ð°Ð·Ð¾Ð²Ñ‹Ð¼Ð¸ ÑÐ¸ÑÑ‚ÐµÐ¼Ð½Ñ‹Ð¼Ð¸ Ð±Ð¸Ð±Ð»Ð¸Ð¾Ñ‚ÐµÐºÐ°Ð¼Ð¸ XCB. ÐžÐ½Ð¾ Ð·Ð°Ð¿ÑƒÑÑ‚Ð¸Ñ‚ÑÑ Ð´Ð°Ð¶Ðµ Ð½Ð° "Ð³Ð¾Ð»Ð¾Ð¹" ÑÐ¸ÑÑ‚ÐµÐ¼Ðµ Ð±ÐµÐ· Ð¸Ð½Ñ‚ÐµÑ€Ð½ÐµÑ‚Ð°!

## Ð£ÑÑ‚Ð°Ð½Ð¾Ð²ÐºÐ° (ÐÐ²Ñ‚Ð¾Ð½Ð¾Ð¼Ð½Ð°Ñ Ð²ÐµÑ€ÑÐ¸Ñ)

Ð¡ÐºÐ°Ñ‡Ð°Ð¹Ñ‚Ðµ Ð¿Ð¾ÑÐ»ÐµÐ´Ð½Ð¸Ð¹ Ñ€ÐµÐ»Ð¸Ð· ÑÐ¾ ÑÑ‚Ñ€Ð°Ð½Ð¸Ñ†Ñ‹ [Releases](https://github.com/mrakoz/telnet-gui/releases).

Ð’Ñ‹Ð±ÐµÑ€Ð¸Ñ‚Ðµ Ð°Ñ€Ñ…Ð¸Ð² Ð¿Ð¾Ð´ Ð²Ð°ÑˆÑƒ Ð°Ñ€Ñ…Ð¸Ñ‚ÐµÐºÑ‚ÑƒÑ€Ñƒ:
- **`telnet-gui-offline-32bit.zip`** â€” Ð´Ð»Ñ 32-Ð±Ð¸Ñ‚Ð½Ñ‹Ñ… (i386) ÑÐ¸ÑÑ‚ÐµÐ¼, Ð½Ð°Ð¿Ñ€Ð¸Ð¼ÐµÑ€ Lubuntu/Ubuntu 16.04
- **`telnet-gui-offline-x64.zip`** â€” Ð´Ð»Ñ 64-Ð±Ð¸Ñ‚Ð½Ñ‹Ñ… (x86_64) ÑÐ¾Ð²Ñ€ÐµÐ¼ÐµÐ½Ð½Ñ‹Ñ… Linux

1. Ð¡ÐºÐ°Ñ‡Ð°Ð¹Ñ‚Ðµ Ð°Ñ€Ñ…Ð¸Ð² Ð¿Ð¾Ð´ Ð²Ð°ÑˆÑƒ Ð°Ñ€Ñ…Ð¸Ñ‚ÐµÐºÑ‚ÑƒÑ€Ñƒ.
2. Ð Ð°ÑÐ¿Ð°ÐºÑƒÐ¹Ñ‚Ðµ Ð°Ñ€Ñ…Ð¸Ð² (Extract) Ð² Ð»ÑŽÐ±ÑƒÑŽ ÑƒÐ´Ð¾Ð±Ð½ÑƒÑŽ Ð¿Ð°Ð¿ÐºÑƒ.
3. Ð—Ð°Ð¹Ð´Ð¸Ñ‚Ðµ Ð² Ð¿Ð°Ð¿ÐºÑƒ Ð¸ Ð´Ð²Ð°Ð¶Ð´Ñ‹ ÐºÐ»Ð¸ÐºÐ½Ð¸Ñ‚Ðµ Ð¿Ð¾ Ñ„Ð°Ð¹Ð»Ñƒ `start.sh`. 
4. Ð’ Ð¿Ð¾ÑÐ²Ð¸Ð²ÑˆÐµÐ¼ÑÑ Ð¾ÐºÐ½Ðµ Ð²Ñ‹Ð±ÐµÑ€Ð¸Ñ‚Ðµ **Execute** (Ð’Ñ‹Ð¿Ð¾Ð»Ð½Ð¸Ñ‚ÑŒ).

> [!IMPORTANT]
> Ð—Ð°Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð½ÑƒÐ¶Ð½Ð¾ Ð¸Ð¼ÐµÐ½Ð½Ð¾ Ñ‡ÐµÑ€ÐµÐ· `start.sh`. Ð­Ñ‚Ð¾Ñ‚ ÑÐºÑ€Ð¸Ð¿Ñ‚ Ð½ÐµÐ·Ð°Ð¼ÐµÑ‚Ð½Ð¾ Ð¿Ð¾Ð´ÐºÐ¸Ð´Ñ‹Ð²Ð°ÐµÑ‚ ÑÐ¸ÑÑ‚ÐµÐ¼Ðµ Ð²ÑÐµ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°ÑŽÑ‰Ð¸Ðµ Ð±Ð¸Ð±Ð»Ð¸Ð¾Ñ‚ÐµÐºÐ¸ Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸ `libs`, Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÑ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð±ÐµÐ· ÑƒÑÑ‚Ð°Ð½Ð¾Ð²ÐºÐ¸ ÐºÐ°ÐºÐ¸Ñ…-Ð»Ð¸Ð±Ð¾ Ð¿Ð°ÐºÐµÑ‚Ð¾Ð² Ñ‡ÐµÑ€ÐµÐ· `apt`.

## ÐšÐ°Ðº Ð¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒÑÑ
1. Ð—Ð°Ð¿ÑƒÑÑ‚Ð¸Ñ‚Ðµ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸Ðµ Ñ‡ÐµÑ€ÐµÐ· `start.sh`.
2. ÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ **Add** Ð½Ð° Ð»ÐµÐ²Ð¾Ð¹ Ð¿Ð°Ð½ÐµÐ»Ð¸, Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾Ð±Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ð¾Ð²Ñ‹Ð¹ ÑÐµÑ€Ð²ÐµÑ€ (Ð½Ð°Ð¿Ñ€Ð¸Ð¼ÐµÑ€, IP `telehack.com`, Ð¿Ð¾Ñ€Ñ‚ `23`).
3. Ð’Ñ‹Ð±ÐµÑ€Ð¸Ñ‚Ðµ Ð½ÑƒÐ¶Ð½Ñ‹Ð¹ ÑÐµÑ€Ð²ÐµÑ€ Ð² ÑÐ¿Ð¸ÑÐºÐµ Ð¸ Ð½Ð°Ð¶Ð¼Ð¸Ñ‚Ðµ **Connect**.
4. Ð’Ð²Ð¾Ð´Ð¸Ñ‚Ðµ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ Ð² Ð½Ð¸Ð¶Ð½ÑŽÑŽ Ñ‚ÐµÐºÑÑ‚Ð¾Ð²ÑƒÑŽ ÑÑ‚Ñ€Ð¾ÐºÑƒ Ð¸ Ð½Ð°Ð¶Ð¸Ð¼Ð°Ð¹Ñ‚Ðµ `Enter` Ð´Ð»Ñ Ð¸Ñ… Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐ¸.
5. ÐŸÐ¾ÑÑ‚Ð°Ð²ÑŒÑ‚Ðµ Ð³Ð°Ð»Ð¾Ñ‡ÐºÑƒ **Interactive Mode**, ÐµÑÐ»Ð¸ ÑƒÐ´Ð°Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐµÑ€Ð²ÐµÑ€ Ð¾Ð¶Ð¸Ð´Ð°ÐµÑ‚ Ð¿Ð¾ÑÐ¸Ð¼Ð²Ð¾Ð»ÑŒÐ½Ð¾Ð³Ð¾ Ð²Ð²Ð¾Ð´Ð° (Ð½Ð°Ð¿Ñ€Ð¸Ð¼ÐµÑ€, Ð´Ð»Ñ Ð½Ð°Ð²Ð¸Ð³Ð°Ñ†Ð¸Ð¸ Ð¿Ð¾ ÐºÐ¾Ð½ÑÐ¾Ð»ÑŒÐ½Ñ‹Ð¼ Ð¼ÐµÐ½ÑŽ).
