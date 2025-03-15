# LibraryProject

# Security Enhancements

## HTTPS and Secure Redirects

- Enforced HTTPS with `SECURE_SSL_REDIRECT = True`
- Configured **HSTS** (Strict Transport Security) for better security.
- Enabled secure cookies for **session** and **CSRF protection**.
- Implemented security headers:
  - `X_FRAME_OPTIONS = "DENY"`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_BROWSER_XSS_FILTER = True`
- Updated **Nginx/Apache** configurations for HTTPS support.

## Deployment Notes

- SSL certificates must be properly installed.
- Ensure **DEBUG = False** in production.
