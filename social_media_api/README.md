# Social Media API

## Setup

1. Clone the repo
2. Create virtual environment & install dependencies
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## Features

- User Registration
- Token-based Login
- User Profile (with followers and profile pictures)

## Endpoints

- `POST /api/accounts/register/`
- `POST /api/accounts/login/`
- `GET /api/accounts/profile/`
