import os
from django.core.management.utils import get_random_secret_key

# Twelve‑factor defaults: only set if not already provided externally
# DEV mode flag controls DEBUG in settings.py
os.environ.setdefault('DEV', '1')

# Cloudinary configuration (use your real credentials or override via env)
os.environ.setdefault(
    'CLOUDINARY_URL',
    'cloudinary://<your_api_key>:<your_api_secret>@dhhna0y51'
)

# SECRET_KEY: generate a secure random key only if none is set in the environment
os.environ.setdefault('SECRET_KEY', get_random_secret_key())

# DATABASE_URL for production: only if not already provided
os.environ.setdefault(
    'DATABASE_URL',
    'postgresql://neondb_owner:npg_KlRpLg4eP1Ys@ep-purple-wind-a2qd67lw.eu-central-1.aws.neon.tech/rinse_stamp_water_942885'
)
