import os

class Secrets:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "local-development-key-change-me"
    )

    DATABASE_URI = os.environ.get(
        "DATABASE_URI",
        "sqlite:///site.db"
    )

    EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS", "")
    PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
