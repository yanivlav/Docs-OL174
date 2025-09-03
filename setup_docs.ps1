# --- יצירת venv אם לא קיים ---
if (!(Test-Path "venv")) {
    python -m venv venv
    Write-Host "✅ Virtual environment created."
}

# --- הפעלת venv ---
& .\venv\Scripts\Activate.ps1

# --- התקנת pip אם חסר ---
python -m ensurepip --upgrade

# --- עדכון pip והתקנת תלות ---
pip install --upgrade pip
pip install sphinx sphinx_rtd_theme

# --- הרצת add_chapter.py ---
python add_chapter.py
