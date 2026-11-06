# Asset Verify — QR Asset Verification & Management

Asset Verify is a Flask web app for tracking equipment, generating QR labels, and recording physical verification checks. Its code is arranged by feature so the team can find each part without searching through one large folder.

## Features

- Password-hashed sign-in, optional authenticator MFA, and administrator-managed technician permissions.
- Add, view, search, edit, and bulk import assets.
- Generate, download, print, and scan QR labels. QR image bytes are stored in MySQL.
- Record verification results and review the verification history.
- View database-backed counts and dashboard charts.

## Technologies

Python 3, Flask, Flask-SQLAlchemy, Flask-Login, MySQL/PyMySQL (SQLite for local development and automated checks), Werkzeug, PyOTP, qrcode/Pillow, Jinja templates, HTML, CSS, JavaScript, Chart.js, and html5-qrcode.

## Project structure

```text
QR-Asset-Verification/
├── app.py                         # App setup, shared extensions and CLI commands
├── back/
│   ├── features/                  # One folder per app feature
│   │   ├── assets/                # Asset routes, validation/service, QR generation
│   │   ├── authentication/        # Login, password and MFA routes
│   │   ├── access/                # Role and permission checks
│   │   ├── dashboard/             # Dashboard route and statistics
│   │   ├── history/               # Verification history route
│   │   ├── team/                  # Technician creation, access, deletion
│   │   ├── verification/          # Scanner pages and verification logic
│   │   └── demo/                  # Demo-data creation
│   ├── models/                    # Database tables/entities
│   ├── database/                  # Reference schema and SQL seed data
│   └── config/                    # Configuration reference
├── front/
│   ├── templates/                 # Jinja pages grouped by feature
│   └── static/                    # Shared styles and feature-specific scripts
├── docs/                          # Setup, architecture, and user guide
├── CODE_LINKS/                    # Quick code map for presenting the project
├── tests/                         # Automated checks
├── qr_codes/                      # Legacy QR files kept for database migration
├── requirements.txt
├── .env.example                   # Safe configuration template
└── START_ASSETVERIFY.bat          # Windows launcher
```

For an easy code tour, open [CODE_LINKS/README.md](CODE_LINKS/README.md). The architecture diagram is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Run on Windows

1. Install Python 3.10+ and MySQL 8 if you plan to use MySQL.
2. Open this folder in VS Code. In its terminal, create and activate a virtual environment, then install packages:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and replace the placeholders with your own values. Never commit `.env`. For local practice, you can use `DATABASE_URL=sqlite:///asset_verification.db`.
4. Initialize the database and administrator account:

   ```powershell
   flask --app app init-db
   ```

5. Start the app with `python app.py`, or double-click `START_ASSETVERIFY.bat`.
6. Open <http://127.0.0.1:5013> in Chrome or Edge.

See [docs/SETUP.md](docs/SETUP.md) for database setup and [docs/USER_GUIDE.md](docs/USER_GUIDE.md) for app usage. Use a unique secret key and strong administrator password; never use placeholder values with real data.

## Database commands

- `flask --app app init-db` creates the tables and initial administrator account.
- `flask --app app seed-demo` adds demo assets, checks, and QR images.
- `flask --app app migrate-qrs-to-db` imports legacy QR PNGs and generates missing labels.
- `flask --app app generate-qrs` creates QR images for assets that do not yet have one in MySQL.
- `flask --app app setup-demo` initializes the database and adds demo records.

The QR images are saved in the `asset_qr_codes.qr_image` database column. The `qr_codes/` folder remains so old local images can be imported during migration.

## Tests

The project has pytest checks that use a temporary SQLite database. Run `pytest` when you want to check the app; the checks do not modify the configured MySQL database.