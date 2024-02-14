This Python script utilizes the `pyautogui` library for automating interactions with the Microsoft Edge browser and a web form. Here's a breakdown of what the code does:

1. Imports the necessary libraries: `pyautogui` and `time`.
2. Sets a pause of 1 second between each PyAutoGUI action.
3. Presses the Windows key to open the Start menu.
4. Types "microsoft edge" into the search bar and presses Enter to open Microsoft Edge.
5. Waits for 5 seconds to ensure the browser has opened.
6. Defines a variable `link` containing a file path to a local HTML file.(its necessary to be your own file path)
7. Enters the link into the browser's address bar and presses Enter.
8. Waits for 8 seconds for the page to load.
9. Imports the `pandas` library for reading CSV files.
10. Reads data from a CSV file named "produtos.csv" into a pandas DataFrame.
11. Iterates over each row of the DataFrame.
12. Performs the following actions for each row:
    - Clicks on a specific position on the screen (assuming it's a specific form input field).
    - Writes data from the DataFrame into the form fields.
    - Scrolls down the page.
13. The script finishes its execution.



---

## Automating Web Form Filling with PyAutoGUI

This is a Python code example that utilizes the PyAutoGUI library to automate the filling of a web form using the Microsoft Edge browser. The goal is to fill form fields with data stored in a CSV file.

### Features:

- Opens the Microsoft Edge browser.
- Loads a specific web page.
- Reads data from a CSV file.
- Fills form fields with data from the CSV file.
- Submits the form automatically.

### How to Use:

1. Install the necessary libraries:

    - Install Python 3.x: [Download Python](https://www.python.org/downloads/)
    
    - Install the PyAutoGUI and pandas libraries via pip:

    ```bash
    pip install pyautogui pandas
    ```

2. Run the Python script.

3. Make sure to adjust the file paths as needed:

    - Update the HTML file path in the `link` variable.
    - Ensure that the CSV file with the data is correctly specified.

### Step-by-Step Algorithm:

1. Opens the Microsoft Edge browser.
2. Loads a specific web page.
3. Reads data from a CSV file.
4. Fills form fields with data from the CSV file.
5. Submits the form automatically.

### Requirements:

- Python 3.x
- Installed Microsoft Edge browser
- Access to the PyAutoGUI and pandas modules

### Notes:

- This script has been tested in a Windows environment.
- Adjustments may be necessary depending on the specific dimensions and layout of the web form.
- It's important to understand the risks of automation and ensure that the usage is ethical and legal.

---


