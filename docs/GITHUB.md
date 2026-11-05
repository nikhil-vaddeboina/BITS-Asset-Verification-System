# GitHub and secret-handling notes

- Commit `.env.example`, but never commit `.env`.
- Keep database passwords, secret keys, MFA encryption keys, and real user data out of Git.
- The `qr_codes/` PNGs are retained in this package because the app documents a legacy QR migration command. Review them before publishing if they encode real asset identifiers.
- Local databases, Python environments, test caches, and backup archives are excluded by `.gitignore`.
