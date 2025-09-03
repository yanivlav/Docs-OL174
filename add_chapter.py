import os
import subprocess

# --- הגדרות ---
docs_path = "docs"
index_file = os.path.join(docs_path, "index.rst")
github_remote = "git@github.com:yanivlav/Docs-OL174.git"

# --- קלט מהמשתמש ---
chapter_name = input("Enter new chapter filename (e.g., chapter3): ").strip()
chapter_title = input("Enter chapter title (Hebrew): ").strip()

chapter_file = os.path.join(docs_path, f"{chapter_name}.rst")

# --- בדיקה אם הפרק כבר קיים ---
if os.path.exists(chapter_file):
    print(f"❌ Error: {chapter_file} already exists.")
    exit(1)

# --- קבלת תוכן מהמשתמש ---
print("\nהדבק כאן את תוכן הפרק שלך. סיים עם EOF (Ctrl+D ב-Linux/macOS, Ctrl+Z ב-Windows):\n")
lines = []
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

chapter_content = f"{chapter_title}\n{'=' * len(chapter_title)}\n\n" + "\n".join(lines)

with open(chapter_file, "w", encoding="utf-8") as f:
    f.write(chapter_content)

print(f"\n✅ Chapter created: {chapter_file}")

# --- עדכון index.rst ---
with open(index_file, "r+", encoding="utf-8") as f:
    content = f.read()
    f.seek(0)
    if chapter_name not in content:
        content = content.replace(".. toctree::", f".. toctree::\n   {chapter_name}")
    f.write(content)

print(f"✅ index.rst updated with {chapter_name}")

# --- שמירת remote המקורי ---
result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
original_remote = result.stdout.strip()

try:
    # --- החלפת remote ל-GitHub ---
    subprocess.run(["git", "remote", "set-url", "origin", github_remote], check=True)

    # --- Git add, commit, push ---
    commit_message = f"Add new chapter {chapter_name}"
    subprocess.run(["git", "add", chapter_file, index_file], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

    print("✅ Push to GitHub done.")

finally:
    # --- החזרת remote המקורי ---
    subprocess.run(["git", "remote", "set-url", "origin", original_remote], check=True)
    print("✅ Original remote restored.")
