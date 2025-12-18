Here's your complete markdown file content:

```markdown
# Notes App – Local Setup Guide

No jargon. No guessing. Clear paths for Windows, Linux, and macOS.

This guide helps you run the Notes App locally on your own computer. You do not need deployment, servers, or hosting.

## What you need before starting

### Basic requirements (all systems)

- A computer
- Internet connection
- Python installed (version 3.9 or higher)
- VS Code or any code editor
- Basic terminal usage (we guide you)

## Step 1: Check Python installation

### Windows

Open Command Prompt (cmd) and run:

```
python --version
```

If it does not work, try:

```
py --version
```

If Python is not installed, install it and check "Add Python to PATH" during install.

### Linux / macOS

Open Terminal and run:

```
python3 --version
```

If not installed:

- Linux: install via your package manager
- macOS: install using system installer or package manager

## Step 2: Get the project files

Create a folder anywhere on your computer. Example: `note_app`

Inside that folder, make sure you have:

```
note_app/
├── app.py
├── database_setup.py
├── templates/
│   ├── login.html
│   └── notes.html
└── static/
    └── (optional files)
```

Open this folder in VS Code.

## Step 3: Open terminal in VS Code

In VS Code, press `Ctrl + `` (backtick) to open the terminal.

Make sure the terminal opens inside the project folder. You should see something like:

```
note_app>
```

## Step 4: Create a virtual environment

Virtual environment keeps project libraries separate.

### Windows (CMD)

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

You should now see `(venv)` at the start of your terminal line.

### Linux / macOS

```
python3 -m venv venv
```

Activate it:

```
source venv/bin/activate
```

You should now see `(venv)` at the start of your terminal line.

## Step 5: Install required library

This project uses Flask.

```
pip install flask
```

Check installation:

```
python -c "import flask; print('Flask installed')"
```

## Step 6: Create the database

**IMPORTANT:** Run this once only.

```
python database_setup.py
```

This will create `notes.db` in your project folder.

If you skip this step, login and notes will not work.

## Step 7: Run the application

Start the server:

```
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

## Step 8: Open the app in browser

Open any browser and go to:

```
http://127.0.0.1:5000
```

## Step 9: How to use the app

- Open the website
- Click Sign up
- Create an account
- Login
- Write notes
- Logout
- Login again — notes stay saved

That means everything is working.

## How to stop the app

In the terminal, press `Ctrl + C`.

## How to exit virtual environment

Run:

```
deactivate
```

Or just close the terminal.

## Common problems and fixes

### (venv) not showing

It may still be active. Run:

```
where python   (Windows)
which python   (Linux/macOS)
```

If it points to venv, you are safe.

### Flask not found

Run:

```
pip install flask
```

### Database error

Delete `notes.db` and run:

```
python database_setup.py
```

### Page not loading

- Make sure `app.py` is running
- Make sure URL is correct: `http://127.0.0.1:5000`

## What this project teaches you

- Backend with Python
- Flask routing
- Authentication
- Sessions
- Database usage
- Real full-stack flow
- Professional local setup

This is not a toy project. This is how real applications start.
```

Copy this entire content and save it as `README.md` or `SETUP_GUIDE.md` in your project folder.
