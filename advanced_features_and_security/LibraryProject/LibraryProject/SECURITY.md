# Django Security Best Practices

## 1️⃣ Configured Security Settings in `settings.py`

- `DEBUG = False` (Disabled in production)
- `SECURE_BROWSER_XSS_FILTER = True` (XSS protection)
- `X_FRAME_OPTIONS = 'DENY'` (Clickjacking prevention)
- `CSRF_COOKIE_SECURE = True` (CSRF protection)
- `SESSION_COOKIE_SECURE = True` (Secure cookies)
- `SECURE_HSTS_SECONDS = 31536000` (HSTS enabled)

## 2️⃣ CSRF Protection

- All forms use `{% csrf_token %}`.

## 3️⃣ SQL Injection Prevention

- Used Django ORM for safe queries.
- Validated user input.

## 4️⃣ Content Security Policy (CSP)

- Enforced CSP in middleware.

## 5️⃣ Testing

- Tested with different users and attempted XSS/CSRF attacks.
