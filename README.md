


# RoboSpeaker 1.1

Welcome to RoboSpeaker 1.1, a simple text-to-speech application . This application allows you to enter text, and it will speak the text out loud. It also supports quitting the application with a farewell message when you type "q".

## Features

- Converts text input to speech.
- Quits the application with a farewell message when "q" is entered.
- Cross-platform support (macOS and Windows).

## Prerequisites

### macOS

No additional dependencies are required as the `say` command is built into macOS.

### Windows

You need to install the `pyttsx3` library for text-to-speech functionality.

```bash
pip install pyttsx3
```

## Usage

### macOS Version

1. Clone the repository or download the `robospeaker_mac.py` script.
2. Run the script using Python:

    ```bash
    python robospeaker_mac.py
    ```

3. Follow the on-screen instructions. Type your text and press Enter to hear it spoken aloud. Type "q" to quit the application with a farewell message.

### Cross-Platform Version (using `pyttsx3`)

1. Clone the repository or download the `robospeaker.py` script.
2. Install the `pyttsx3` library if you haven't already:

    ```bash
    pip install pyttsx3
    ```

3. Run the script using Python:

    ```bash
    python robospeaker.py
    ```

4. Follow the on-screen instructions. Type your text and press Enter to hear it spoken aloud. Type "q" to quit the application with a farewell message.



---

