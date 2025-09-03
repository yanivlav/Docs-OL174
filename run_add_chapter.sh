#!/bin/bash

# --- בדיקה אם Python3 מותקן ---
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found! Please install Python3."
    exit
fi

# --- יצירת virtual environment אם לא קיים ---
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# --- הפעלה ---
source venv/bin/activate

# --- התקנת תלות אם צריך ---
pip install --upgrade pip
pip install sphinx sphinx_rtd_theme

# --- הרצת הסקריפט add_chapter.py ---
python3 add_chapter.py
