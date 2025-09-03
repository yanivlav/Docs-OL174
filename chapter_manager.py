import os
import subprocess

# תיקיית docs יחסית לסקריפט/EXE
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
INDEX_FILE = os.path.join(DOCS_DIR, "index.rst")


def list_chapters():
    chapters = [f for f in os.listdir(DOCS_DIR) if f.endswith(".rst") and f != "index.rst"]
    if not chapters:
        print("No chapters found.")
    else:
        print("Chapters:")
        for i, chapter in enumerate(chapters, 1):
            print(f"{i}) {chapter}")
    return chapters


def update_index():
    chapters = [f for f in os.listdir(DOCS_DIR) if f.endswith(".rst") and f != "index.rst"]
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(".. toctree::\n   :maxdepth: 2\n\n")
        for chapter in sorted(chapters):
            f.write(f"   {chapter}\n")


def git_commit_push(message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
    except subprocess.CalledProcessError as e:
        print("Git operation failed:", e)


def add_chapter():
    title = input("Enter chapter title: ").strip()
    filename = title.replace(" ", "_") + ".rst"
    path = os.path.join(DOCS_DIR, filename)

    print("Enter chapter content. End with a line containing only EOF:")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    update_index()
    git_commit_push(f"Add chapter: {title}")
    print(f"Chapter '{title}' added successfully.")


def edit_chapter():
    chapters = list_chapters()
    if not chapters:
        return
    choice = int(input("Select chapter to edit: ")) - 1
    path = os.path.join(DOCS_DIR, chapters[choice])

    print("Enter new content. End with EOF:")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    update_index()
    git_commit_push(f"Edit
