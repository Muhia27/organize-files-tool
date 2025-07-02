# organize-files-tool

A Python CLI tool that organizes files in a folder by their extension.

---

## Features

- Move files by extension (e.g., `.txt`, `.jpg`, `.pdf`)
- Automatically creates folders
- Logs every move (with timestamp)
- Supports CLI usage with flags

---

## Installation

```bash
git clone https://github.com/Muhia27/organize-files.git
cd organize-files-tool
pip install .

organize-files -s <source_folder> -e <.ext1> <.ext2> ... [-l <logfile>]

##Requirements

Python 3.6+

colorama (auto-installed via pip)
