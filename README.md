# Chapter Manager

The **Chapter Manager** script allows contributors to easily manage documentation chapters in the `docs/` folder.

## Features
- **Add new chapters**  
- **Edit existing chapters**  
- **Delete chapters**  
- **List all chapters**  
- Automatically updates `index.rst`  
- Commits and pushes changes to GitHub  

## Usage

### Python
Run the script with Python:
```bash
python chapter_manager.py

Windows EXE

If you have the EXE:
Release is available.


Linux EXE / Shell
If you have the Linux binary or shell script:
./chapter_manager

Instructions

Select an action from the menu:

Add a chapter

Edit a chapter

Delete a chapter

List all chapters

Exit

When adding or editing a chapter:

Enter the chapter title

Paste the content line by line

Finish with a line containing only EOF ctrl+z and press enter

The script automatically:

Creates or updates .rst files in docs/

Updates index.rst

Performs git commit and git push

Notes

Make sure your GitHub remote is configured correctly.

Ensure Python is installed for .py usage, or use

You
