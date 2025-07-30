# Email Setup Guide

This guide explains how to configure email functionality for the contact form.

## Quick Setup

1. **Copy the environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Choose your email provider and update `.env`:**

### Gmail (Recommended)
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
CONTACT_EMAIL=your-email@gmail.com
```

**Important:** Use an App Password, not your regular Gmail password:
1. Enable 2-factor authentication on your Google account
2. Generate an App Password: https://support.google.com/accounts/answer/185833
3. Use the 16-character app password in the `.env` file

### Outlook/Hotmail
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USERNAME=your-email@outlook.com
SMTP_PASSWORD=your-password
CONTACT_EMAIL=your-email@outlook.com
```

### Yahoo Mail
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
SMTP_USERNAME=your-email@yahoo.com
SMTP_PASSWORD=your-app-password
CONTACT_EMAIL=your-email@yahoo.com
```

### Custom SMTP Server
```env
SMTP_SERVER=your-smtp-server.com
SMTP_PORT=587
SMTP_USERNAME=your-username
SMTP_PASSWORD=your-password
CONTACT_EMAIL=your-email@yourdomain.com
```

## How It Works

1. **Contact Form Submission:** When someone fills out the contact form on your website
2. **Email Generation:** The system creates a nicely formatted HTML email
3. **SMTP Sending:** Email is sent via your configured SMTP server
4. **Fallback:** If email fails, the form still shows success (graceful degradation)

## Security Notes

- ✅ The `.env` file is already in `.gitignore` - it won't be committed to git
- ✅ Use app passwords instead of regular passwords when possible
- ✅ The email function includes error handling and fallbacks
- ✅ Form includes CSRF protection

## Testing

To test the email functionality:
1. Configure your `.env` file
2. Run the Flask app: `python app.py`
3. Go to `/contact` and submit a test message
4. Check your configured email inbox

## Troubleshooting

**Email not sending?**
- Check your SMTP credentials in `.env`
- Verify your email provider allows SMTP
- For Gmail, ensure you're using an App Password
- Check the Flask console for error messages

**Still having issues?**
- The form will still work - it just falls back to showing a success message
- Users can always email you directly at the address shown
- Consider using a service like SendGrid for production

## Production Deployment

For production, set environment variables on your server instead of using a `.env` file:
```bash
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SMTP_USERNAME=your-email@gmail.com
export SMTP_PASSWORD=your-app-password
export CONTACT_EMAIL=your-email@gmail.com
```