# 📸 iCloud Photo Sync Tool

A Python-based tool that synchronizes photos from iCloud to local storage with intelligent deletion tracking. This tool ensures that locally deleted photos are not re-downloaded while never touching your iCloud photos.

## ✨ Features

- **🔄 Smart Sync**: Only downloads new photos that don't exist locally
- **🛡️ Deletion Protection**: Tracks locally deleted photos to prevent re-downloading
- **☁️ iCloud Safe**: Never deletes photos from your iCloud account
- **🎯 Idempotent**: Safe to run multiple times without duplicates
- **🖥️ Cross-Platform**: Works on Windows and Linux
- **📊 Logging**: Detailed console and file logging
- **🔧 Configurable**: Customizable sync directory and settings

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- iCloud account with Two-Factor Authentication enabled

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/icloud-photo-sync.git
   cd icloud-photo-sync
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure your settings:**
   ```bash
   cp .env.example .env
   # Edit .env with your iCloud credentials and sync directory
   ```

4. **Run the sync:**
   ```bash
   uv run icloud-photo-sync
   ```

## 📁 Project Structure

```
icloud-photo-sync/
├── src/
│   └── icloud_photo_sync/
│       ├── __init__.py
│       ├── main.py              # Entry point
│       ├── sync.py              # Core sync logic
│       ├── deletion_tracker.py  # Local deletion tracking
│       └── config.py            # Configuration management
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
├── pyproject.toml              # Project configuration
├── .env.example               # Environment template
└── README.md
```

## ⚙️ Configuration

### Option 1: Environment Variables (Traditional)

Create a `.env` file in the project root:

```env
# iCloud Credentials
ICLOUD_USERNAME=your.email@icloud.com
ICLOUD_PASSWORD=your-app-specific-password

# Sync Settings
SYNC_DIRECTORY=/path/to/your/photos
DRY_RUN=false
LOG_LEVEL=INFO
```

### Option 2: Keyring (Secure Storage)

For enhanced security, you can store your credentials in your system's credential store (Windows Credential Manager, macOS Keychain, Linux Secret Service). The application automatically detects keyring availability and uses the appropriate configuration class:

- **KeyringConfig**: Used when keyring is available - supports both environment variables and secure credential storage
- **EnvOnlyConfig**: Used when keyring is not available - only supports environment variables

1. **Store credentials securely:**
   ```bash
   uv run python manage_credentials.py
   ```

2. **Update your .env file to only include sync settings:**
   ```env
   # Sync Settings (credentials will be retrieved from keyring)
   SYNC_DIRECTORY=/path/to/your/photos
   DRY_RUN=false
   LOG_LEVEL=INFO
   ```

The application uses **polymorphism** to handle different credential storage strategies:
- First checks for credentials in environment variables
- If not found and keyring is available, retrieves them from your system's keyring
- On Windows: Uses Windows Credential Manager
- On macOS: Uses Keychain
- On Linux: Uses Secret Service

**Benefits of the polymorphic design:**
- 🔧 **Automatic fallback**: Seamlessly switches between keyring and environment-only modes
- 🔐 **Security first**: Credentials are encrypted by your operating system when using keyring
- 🚫 **No plain text passwords**: Keep sensitive data out of configuration files
- 🔄 **Transparent operation**: Same interface regardless of storage method
- 🔒 **OS integration**: Works with your system's native credential storage

## 🧪 Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/icloud_photo_sync

# Run linting
uv run ruff check .
uv run mypy src/
```

### Building Executables

```bash
# Install PyInstaller
uv add --dev pyinstaller

# Build for current platform
uv run pyinstaller icloud-photo-sync.spec
```

## 🛠️ How It Works

1. **Authentication**: Securely connects to iCloud using your credentials
2. **Photo Discovery**: Scans your iCloud photo library for all photos
3. **Local Check**: Compares with existing local files and deletion database
4. **Smart Download**: Downloads only new photos that haven't been deleted locally
5. **Tracking**: Updates deletion database for any locally missing photos

## 🔒 Security & Privacy

- **No Cloud Storage**: Your credentials and photos stay on your devices
- **App-Specific Passwords**: Uses iCloud app-specific passwords (recommended)
- **Local Database**: Deletion tracking stored locally in SQLite
- **No Data Sharing**: No data is sent to external services

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

- Python 3.9+
- iCloud account with Two-Factor Authentication
- Sufficient local storage for your photo library

## 🆘 Support

If you encounter issues:

1. Check the [Issues](https://github.com/your-username/icloud-photo-sync/issues) page
2. Review the logs in the `logs/` directory
3. Ensure your iCloud credentials are correct
4. Verify Two-Factor Authentication is enabled

## 🙏 Acknowledgments

- Built with [pyicloud](https://pypi.org/project/pyicloud/) for iCloud API access
- Dependency management by [uv](https://docs.astral.sh/uv/)
- Inspired by the need for safe, local photo backups