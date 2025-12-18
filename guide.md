# Note App Setup Guide

A simple Flask-based note-taking application with user authentication and SQLite database.

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning)

## 🚀 Quick Start

### 1. Download/Clone the Project

**Option A: Download ZIP**
- Download the project files to your desired directory

**Option B: Clone with Git**
```bash
git clone <repository-url>
cd note_app
```

### 2. Setup Instructions by Operating System

## 🪟 Windows Setup

### Method 1: Using Command Prompt
```cmd
# Navigate to project directory
cd path\to\note_app

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

### Method 2: Using PowerShell
```powershell
# Navigate to project directory
cd path\to\note_app

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If execution policy error occurs, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

## 🍎 macOS Setup

### Using Terminal
```bash
# Navigate to project directory
cd /path/to/note_app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

### Using Homebrew (if Python not installed)
```bash
# Install Python via Homebrew
brew install python

# Then follow the steps above
```

## 🐧 Linux Setup

### Ubuntu/Debian
```bash
# Update package list
sudo apt update

# Install Python and pip (if not installed)
sudo apt install python3 python3-pip python3-venv

# Navigate to project directory
cd /path/to/note_app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

### CentOS/RHEL/Fedora
```bash
# For CentOS/RHEL
sudo yum install python3 python3-pip

# For Fedora
sudo dnf install python3 python3-pip

# Navigate to project directory
cd /path/to/note_app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

### Arch Linux
```bash
# Install Python
sudo pacman -S python python-pip

# Navigate to project directory
cd /path/to/note_app

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Setup database
python database_setup.py

# Run the application
python app.py
```

## 🔧 Alternative Setup Methods

### Using requirements.txt (Recommended)

Create a `requirements.txt` file:
```txt
Flask==2.3.3
```

Then install dependencies:
```bash
# After activating virtual environment
pip install -r requirements.txt
```

### Using Docker

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install flask
RUN python database_setup.py

EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t note-app .
docker run -p 5000:5000 note-app
```

## 🌐 Accessing the Application

1. After running `python app.py`, you'll see output like:
   ```
   * Running on http://127.0.0.1:5000
   ```

2. Open your web browser and navigate to:
   - `http://localhost:5000` or
   - `http://127.0.0.1:5000`

3. Create an account or login to start using the note app

## 📁 Project Structure

```
note_app/
├── app.py              # Main Flask application
├── database_setup.py   # Database initialization script
├── templates/
│   ├── Login.html      # Login/Signup page
│   └── Notes.html      # Notes dashboard
├── static/
│   └── style.css       # Additional styles (optional)
└── notes.db           # SQLite database (created after setup)
```

## 🔍 Troubleshooting

### Common Issues

**1. Python not found**
- Ensure Python is installed and added to PATH
- Try `python3` instead of `python` on macOS/Linux

**2. Permission denied (Linux/macOS)**
- Use `sudo` for system-wide installations
- Or use virtual environments (recommended)

**3. Flask not found**
- Ensure virtual environment is activated
- Reinstall Flask: `pip install flask`

**4. Database errors**
- Delete `notes.db` file and run `python database_setup.py` again
- Check file permissions

**5. Port already in use**
- Change port in `app.py`: `app.run(debug=True, port=5001)`
- Or kill the process using port 5000

### Virtual Environment Issues

**Windows PowerShell execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Deactivate virtual environment:**
```bash
deactivate
```

## 🔒 Security Notes

- Change the `secret_key` in `app.py` for production use
- Use environment variables for sensitive data
- Consider using a more robust database for production
- Implement proper password validation
- Add HTTPS in production

## 🚀 Production Deployment

### Using Gunicorn (Linux/macOS)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Waitress (Windows)
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

## 📝 Features

- User registration and authentication
- Secure password hashing
- Personal note creation and management
- Note deletion functionality
- Responsive web interface
- Session management

## 🛠 Development

To modify the application:

1. **Backend changes**: Edit `app.py`
2. **Frontend changes**: Edit HTML templates in `templates/`
3. **Database changes**: Modify `database_setup.py` and recreate database
4. **Styling**: Edit CSS in templates or `static/style.css`

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify virtual environment is activated
4. Check Python and Flask versions compatibility

---

**Happy note-taking! 📝**