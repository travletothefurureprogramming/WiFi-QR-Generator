# WiFi QR Generator

A simple and efficient utility to generate QR codes for your WiFi network, allowing guests to connect instantly by scanning the code with their smartphones. This project comes in two versions: a Command Line Interface (CLI) and a Graphical User Interface (GUI).

## Features

- **Dual Versions:** 
  - **CLI:** Fast, terminal-based generator for quick use.
  - **GUI:** Built with `CustomTkinter` for a modern, user-friendly desktop experience.
- **Save Location:** Choose exactly where you want to save the generated QR code image on your device.
- **Show/Hide Password:** Option to toggle password visibility within the GUI for convenience and security.
- **Robust Error Handling:** Built-in validation to prevent crashes and ensure smooth generation.
- **Print Option:** Integrated printing capabilities (currently in beta/development).

## Development Changelog (Devlogs)

* **Update 4:** Added comprehensive error handling and input validation.
* **Update 3:** Implemented password visibility toggle, custom save directory selection for the QR code, and initial print integration.
* **Update 2:** Designed and developed the modern desktop GUI using `CustomTkinter`.
* **Update 1:** Created the core WiFi QR generator logic operating via the terminal (CLI).

## Getting Started

1. Download the github release wich contains .exe programms for both CLI and GUI app
2. Open the .exe you want and start generate

## How to use it
### CLI

* Select what you want to do:
  - Generate QR code (To generate a new qr code)
  - View history (To view previous generations)
  - Delete history (To delete the current history)
  - Exit (To exit)

For qr code generation:

1. Enter the SSID

2. Enter password
Note: The WiFi password is entered securely and is hidden while typing. Although no characters are displayed on the screen, your input is still being recorded correctly.

3. Select Security Type 

4. Select qr code size

5. The qr code will be saved and it will open in your's computer gallery
