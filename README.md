# Telnet GUI Client

![Telnet GUI Logo](https://img.shields.io/badge/Telnet-GUI-blue.svg)
![Linux](https://img.shields.io/badge/Linux-Standalone-green.svg)
![Offline Ready](https://img.shields.io/badge/Offline-Ready-orange.svg)

*(🇷🇺 Русская версия ниже)*

**Telnet GUI** is a fast, native, and modern Telnet client for Linux, built with Python and PyQt5. It features a dark-themed interface, profile management, and an interactive mode for character-by-character communication (useful for MUD games or router configurations).

## Features
- **Export/Import:** Save and restore your entire server list as JSON files — handy for backups or transferring profiles between machines.
- **Profile Manager:** Save, edit, and delete server connections (Name, IP, Port).
- **Smart Logs:** Each profile remembers its own terminal output when switching between tabs.
- **Interactive Mode:** Toggle "Interactive Mode" to send keystrokes directly to the server in real time (byte-by-byte), bypassing the need to press Enter.
- **Asynchronous Engine:** The network operations run in a background thread, preventing the UI from freezing even during timeouts or network failures.
- **100% Offline Standalone Build:** The application is packaged to run on entirely barebones Linux systems without an internet connection. It brings its own Python runtime, Qt engine, and low-level X11/XCB libraries.

## Installation

Download the latest release from the [Releases](https://github.com/mrakoz/telnet-gui/releases) page.

Choose the archive for your architecture:
- **`telnet-gui-offline-32bit.zip`** — for 32-bit (i386) systems, e.g. Lubuntu/Ubuntu 16.04
- **`telnet-gui-offline-x64.zip`** — for 64-bit (x86_64) modern Linux systems

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

# Telnet GUI Client (На русском)

**Telnet GUI** — это быстрый, нативный и современный графический Telnet-клиент для Linux. Он предлагает стильный тёмный интерфейс, менеджер профилей и интерактивный режим для посимвольной отправки данных (идеально для MUD-игр или настройки сетевого оборудования).

## Основные возможности
- **Экспорт/Импорт:** Сохраняйте и восстанавливайте весь список серверов в JSON — удобно для бэкапов или переноса между машинами.
- **Менеджер профилей:** Сохраняйте, редактируйте и удаляйте настройки серверов (Имя, IP-адрес, Порт).
- **Умные логи:** При переключении между сохранёнными серверами история консоли для каждого из них бережно сохраняется.
- **Интерактивный режим (Interactive Mode):** Включите галочку, чтобы перехватывать нажатия клавиш и отправлять их на сервер в реальном времени (побайтово) без необходимости нажимать `Enter`.
- **Асинхронный движок:** Работа с сетью вынесена в фоновый поток. Интерфейс никогда не "зависает" при ожидании ответа или обрывах связи.
- **100% Автономность (Offline Ready):** Приложение упаковано вместе с собственным интерпретатором Python, графическим движком Qt и базовыми системными библиотеками XCB. Оно запустится даже на "голой" системе без интернета!

## Установка (Автономная версия)

Скачайте последний релиз со страницы [Releases](https://github.com/mrakoz/telnet-gui/releases).

Выберите архив под вашу архитектуру:
- **`telnet-gui-offline-32bit.zip`** — для 32-битных (i386) систем, например Lubuntu/Ubuntu 16.04
- **`telnet-gui-offline-x64.zip`** — для 64-битных (x86_64) современных Linux

1. Скачайте архив под вашу архитектуру.
2. Распакуйте архив (Extract) в любую удобную папку.
3. Зайдите в папку и дважды кликните по файлу `start.sh`. 
4. В появившемся окне выберите **Execute** (Выполнить).

> [!IMPORTANT]
> Запускать нужно именно через `start.sh`. Этот скрипт незаметно подкидывает системе все недостающие библиотеки из папки `libs`, позволяя приложению работать без установки каких-либо пакетов через `apt`.

## Как пользоваться
1. Запустите приложение через `start.sh`.
2. Нажмите **Add** на левой панели, чтобы добавить новый сервер (например, IP `telehack.com`, порт `23`).
3. Выберите нужный сервер в списке и нажмите **Connect**.
4. Вводите команды в нижнюю текстовую строку и нажимайте `Enter` для их отправки.
5. Поставьте галочку **Interactive Mode**, если удаленный сервер ожидает посимвольного ввода (например, для навигации по консольным меню).
