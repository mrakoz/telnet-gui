# Telnet GUI Client

![Telnet GUI Logo](https://img.shields.io/badge/Telnet-GUI-blue.svg)
![Python](https://img.shields.io/badge/python-3.5%2B-green.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-orange.svg)

*(🇷🇺 Русская версия ниже)*

**Telnet GUI** is a fast, native, and modern Telnet client for Linux, built with Python and PyQt5. It features a dark-themed interface, profile management, and an interactive mode for character-by-character communication (useful for MUD games or router configurations).

## Features
- **Profile Manager:** Save, edit, and delete server connections (Name, IP, Port).
- **Smart Logs:** Each profile remembers its own terminal output when switching between tabs.
- **Interactive Mode:** Toggle "Interactive Mode" to send keystrokes directly to the server in real time (byte-by-byte), bypassing the need to press Enter.
- **Asynchronous Engine:** The network operations run in a background thread, preventing the UI from freezing even during timeouts or network failures.
- **Backward Compatible:** Verified to run flawlessly even on older systems (like Ubuntu 16.04 with Python 3.5).
- **Debian Package (.deb):** Easy to install and integrates perfectly into the Linux application menu.

## Installation

Download the latest `.deb` package from the [Releases](https://github.com/mrakoz/telnet-gui/releases) page.

```bash
wget https://github.com/mrakoz/telnet-gui/releases/download/v1.2.3/telnet-gui_1.2.3.deb
sudo dpkg -i telnet-gui_1.2.3.deb
```
If you encounter missing dependencies (like PyQt5), fix them with:
```bash
sudo apt-get install -f
```

## How to Use
1. Launch the app from your application menu (under **Network/Internet** -> **Telnet GUI**) or type `telnet-gui` in your terminal.
2. Click **Add** on the left panel to save a new server profile (e.g., `telehack.com`, Port `23`).
3. Select your profile and click **Connect**.
4. Type your commands in the bottom input line and press `Enter` to send.
5. Check the **Interactive Mode** box if you need real-time key capture (useful for text-based UI menus on remote hosts).

---

# Telnet GUI Client (На русском)

**Telnet GUI** — это быстрый, нативный и современный графический Telnet-клиент для Linux, написанный на Python и PyQt5. Он предлагает стильный тёмный интерфейс, менеджер профилей и интерактивный режим для посимвольной отправки данных (идеально для MUD-игр или настройки сетевого оборудования).

## Основные возможности
- **Менеджер профилей:** Сохраняйте, редактируйте и удаляйте настройки серверов (Имя, IP-адрес, Порт).
- **Умные логи:** При переключении между сохранёнными серверами история консоли для каждого из них бережно сохраняется.
- **Интерактивный режим (Interactive Mode):** Включите галочку, чтобы перехватывать нажатия клавиш и отправлять их на сервер в реальном времени (побайтово) без необходимости нажимать `Enter`.
- **Асинхронный движок:** Работа с сетью вынесена в фоновый поток. Интерфейс никогда не "зависает" при ожидании ответа или обрывах связи.
- **Обратная совместимость:** Программа оптимизирована для работы даже на старых ОС (таких как Ubuntu/Lubuntu 16.04 с Python 3.5).
- **Удобный пакет (.deb):** Приложение устанавливается одной командой и добавляет красивый ярлык в меню приложений Linux.

## Установка

Скачайте свежий `.deb` пакет со страницы [Releases](https://github.com/mrakoz/telnet-gui/releases).

```bash
wget https://github.com/mrakoz/telnet-gui/releases/download/v1.2.3/telnet-gui_1.2.3.deb
sudo dpkg -i telnet-gui_1.2.3.deb
```
Если система пожалуется на нехватку зависимостей (например, PyQt5), выполните:
```bash
sudo apt-get install -f
```

## Как пользоваться
1. Запустите приложение из меню (в разделе **Сеть / Интернет** -> **Telnet GUI**) или введите команду `telnet-gui` в терминале.
2. Нажмите **Add** на левой панели, чтобы добавить новый сервер (например, IP `telehack.com`, порт `23`).
3. Выберите нужный сервер в списке и нажмите **Connect**.
4. Вводите команды в нижнюю текстовую строку и нажимайте `Enter` для их отправки.
5. Поставьте галочку **Interactive Mode**, если удаленный сервер ожидает посимвольного ввода (например, для навигации по консольным меню).
