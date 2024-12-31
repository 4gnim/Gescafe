# Gescafe

**Gescafe** is a Python-based application designed to detect hand gestures for ordering interfaces. This application utilizes OpenCV and cvzone modules to track hands and map gestures to different ordering modes. The project aims to demonstrate innovative, touchless, and interactive user interfaces.

---

## Key Features

- **Hand Gesture Detection:** Tracks hands using a camera with high accuracy.
- **Ordering Modes:** Several ordering modes can be accessed via hand gestures.
- **Navigation Gestures:**
  - Select modes using finger gestures.
  - "Back" gesture to return to the previous mode.
- **Dynamic Icons:** Displays selected icons on the screen based on user input.
- **Reset Functionality:** Reset all selections using a dedicated key.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or newer
- OpenCV
- cvzone
- NumPy

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/4gnim/Gescafe.git
   cd gescafe
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the `Resources` folder is available and contains:
   - **Background.png:** Background image for the application.
   - **Modes:** Folder containing mode images.
   - **Icons:** Folder containing selection icons.

---

## How to Use

1. Run the application:
   ```bash
   python gescafe.py
   ```
2. Use hand gestures to select modes:
   - **[0, 1, 0, 0, 0]:** Select option 1.
   - **[0, 1, 1, 0, 0]:** Select option 2.
   - **[0, 1, 1, 1, 0]:** Select option 3.
   - **[1, 1, 1, 1, 1]:** Go back to the previous mode.
3. Selected icons will appear at the bottom of the screen.
4. Press `n` to reset all selections.
5. Press `q` to exit the application.

---

## Folder Structure

```
Resources/
  Background.png
  Modes/
    mode1.png
    mode2.png
    ...
  Icons/
    icon1.png
    icon2.png
    ...
```

---

## Technologies Used

- **OpenCV:** Captures video and processes real-time images.
- **cvzone:** Detects hands and determines landmark positions.
- **NumPy:** Handles image and array data manipulation.

---

## Contribution

Contributions are welcome! To add features or fix bugs, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature X"
   ```
4. Push to your branch:
   ```bash
   git push origin your-feature
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Enjoy using Gescafe!**
