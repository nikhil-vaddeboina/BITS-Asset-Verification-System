# Asset Verify — QR Asset Verification & Management

Asset Verify is a Flask web app for tracking equipment, generating QR labels, and recording physical verification checks.

## Features

- Password-hashed sign-in, optional authenticator MFA, and administrator-managed technician permissions.
- Add, view, search, edit, delete, and bulk import assets.
- Generate, download, print, and scan QR labels. QR image bytes are stored in MySQL.
- Record verification results and review the verification history.
- View database-backed counts and dashboard charts.

## Technologies

Python 3, Flask, Flask-SQLAlchemy, Flask-Login, MySQL/PyMySQL (SQLite for local development and automated checks), Werkzeug, PyOTP, qrcode/Pillow, Jinja templates, HTML, CSS, JavaScript, Chart.js, and html5-qrcode.

## Project structure

The source code is organized into `back/` (routes, models, services, database and configuration), `front/` (templates and static assets), `docs/` (setup and project guides), `tests/`, and `qr_codes/` (legacy QR files for migration).

## Run on Windows

1. Install Python 3.10+ and MySQL 8 if you plan to use MySQL.
2. Create and activate a virtual environment, then install packages:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and replace the placeholders with your own values. Never commit `.env`. For local practice, use `DATABASE_URL=sqlite:///asset_verification.db`.
4. Initialize the database: `flask --app app init-db`.
5. Start the app with `python app.py` or `START_ASSETVERIFY.bat`.
6. Open http://127.0.0.1:5013.

See `docs/SETUP.md` and `docs/USER_GUIDE.md` for more details. Use a unique secret key and strong administrator password; never use placeholder values with real data.

## Database commands

- `flask --app app init-db` creates the tables and initial administrator account.
- `flask --app app seed-demo` adds demo assets, checks, and QR images.
- `flask --app app migrate-qrs-to-db` imports legacy QR PNGs and generates missing labels.
- `flask --app app generate-qrs` creates QR images for assets that do not yet have one in MySQL.
- `flask --app app setup-demo` initializes the database and adds demo records.

QR image bytes are saved in the `asset_qr_codes.qr_image` database column.