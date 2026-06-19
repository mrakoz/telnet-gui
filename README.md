# Telnet GUI Client

A modern, simple, and powerful Telnet client for Linux with a beautiful graphical interface written in Python and PyQt6.

## Features

- **Profile Management**: Save, edit, and delete your frequently used Telnet servers.
- **Split-Pane UI**: Navigate profiles on the left while monitoring output on the right.
- **Syntax Highlighting**: Distinct colors for client commands, server responses, info messages, and errors.
- **Interactive Mode (Character Mode)**: Perfect for MUDs, hardware routers, and interactive servers! When the **Interactive Mode** checkbox is enabled, simply click on the large terminal window and start typing. Every keystroke is sent directly to the server in real-time, bypassing the need to press Enter.

## Installation

Download the `.deb` package from the [Releases page](https://github.com/mrakoz/telnet-gui/releases) and install it using:

```bash
sudo dpkg -i telnet-gui.deb
```
*(Dependencies like python3-pyqt6 will be handled automatically if installed via gdebi or apt).*

## Usage

You can launch the application from your desktop environment's application menu (under Network/Utility) or by running:
```bash
telnet-gui
```
