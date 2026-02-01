# Vaccine Analytics Mini Project

This repository contains a Streamlit app that demonstrates simple vaccine analytics and visualizations.

Files added

- [vaccine_analytics_website.py](vaccine_analytics_website.py) — main Streamlit app
- [requirements.txt](requirements.txt) — Python dependencies
- [Procfile](Procfile) — optional deployment entry for PaaS
- [.streamlit/config.toml](.streamlit/config.toml) — Streamlit runtime config

## Quick start (local)

1. Create a virtual environment and activate it.

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (cmd)
.\.venv\Scripts\activate.bat
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies and run the app:

```bash
pip install -r requirements.txt
streamlit run vaccine_analytics_website.py
```

## Deploy

- Streamlit Community Cloud: create a new app and point it at the repository and the `vaccine_analytics_website.py` file.
- Render/Heroku: use the `Procfile`. Ensure `requirements.txt` is present.

## Next steps

- Add interactivity (filters, sliders) to the Streamlit app.
- Add tests or CI for automated checks.
