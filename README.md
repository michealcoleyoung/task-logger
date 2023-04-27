# Task Logger

This is a command line application that helps users track the tasks they are working on, record the time they started and ended each task, and export the data to the clipboard.
Installation

To use this application, you will need to install Python and create a virtual environment. Then, you will need to install the necessary dependencies using pip.

    Install Python 3 from the official website.
    Open a terminal or command prompt and navigate to the directory where you want to store the application.
    Create a virtual environment by entering the following command: python -m venv venv. This will create a new directory called venv that contains a fresh installation of Python.
    Activate the virtual environment by entering the following command:

    On Windows: venv\Scripts\activate
    On macOS or Linux: source venv/bin/activate

    Install the dependencies by entering the following command: pip install pyperclip.

Usage

To use the application, open a terminal or command prompt and navigate to the directory where the application is stored. Then, activate the virtual environment by entering the command listed in the installation instructions.

To start tracking a new task, enter a brief description of the task when prompted. The application will record the start time of the task and wait for you to finish. When you are finished, press Enter to stop the timer and record the time worked on the task.

You can track as many tasks as you need, and the application will store all of the data in memory. To export the data to the clipboard, enter the command export data when prompted for a task description. The application will format the data and copy it to your clipboard, ready for pasting into another application.
