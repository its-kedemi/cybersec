# Cybersecurity Awareness Demo

A Streamlit landing page for an authorised phishing-awareness presentation. It displays an animated falling-binary background and reveals a short training message.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
```

Activate the environment, then install and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Visit https://share.streamlit.io/ and sign in with GitHub.
3. Create an app from this repository, select the branch, and set the main file path to `app.py`.
4. Deploy and test the generated URL.

## Awareness exercise safety

- Use only with appropriate organisational approval and agreed recipients.
- Do not collect passwords or other sensitive information.
- Use a fictional, approved sender identity; do not impersonate a real colleague or customer.
- The page itself does not collect form submissions or credentials.
- A public deployment stays available until you take it offline or delete the deployment.

## Odoo inquiry email template

See `templates/odoo_inquiry_email.html` for an example message to adapt for an approved simulation. The GoPhish `{{.URL}}` variable is intended to be rendered by GoPhish.
