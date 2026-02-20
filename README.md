# File Sorter by File Type

A Python automation tool that sorts all files in a given directory into category folders based on file extension.

<p align="center">
  <img src="assets/Before_After_File Extension Sorter.png" width="700" alt="Before and After Comparison">
</p>
<p align="center">
  Image credit: ChatGPT
</p>


## 1. Problem

Over time, folders like **Downloads**, **Desktop**, or shared drives become cluttered with hundreds of unsorted files — documents mixed with videos, spreadsheets buried alongside installers, and code files scattered everywhere. Manually organizing them is tedious, error-prone, and time-consuming. Worse, this clutter makes it difficult to spot files that shouldn't be there, such as unexpected executables or unfamiliar archive files that could pose a security risk.

## 2. Solution

**File Sorter** is a single Python script (`sort_files.py`) that organizes every file in a target directory into one of **11 category folders** based on its file extension:

| Category | Example Extensions |
|---|---|
| **Video** | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm` |
| **Image** | `.jpg`, `.png`, `.gif`, `.svg`, `.psd` |
| **PDF** | `.pdf` |
| **Document** | `.docx`, `.txt`, `.md`, `.epub`, `.rtf` |
| **Presentation** | `.pptx`, `.ppt`, `.key`, `.odp` |
| **Data** | `.csv`, `.xlsx`, `.json`, `.sql`, `.parquet` |
| **Audio** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| **Archive** | `.zip`, `.rar`, `.7z`, `.tar.gz`, `.iso` |
| **Code_Script** | `.py`, `.js`, `.html`, `.sh`, `.java` |
| **Executable** | `.exe`, `.msi`, `.apk`, `.dll`, `.bin` |
| **Other** | Any file type not listed above |

### Key Features

- **Smart folder creation** — Category folders are only created when matching files exist. No empty folders are generated. Pre-existing folders are reused without duplication.
- **100+ recognized extensions** — Covers the most common file types across all categories, including compound extensions like `.tar.gz`.
- **Collision handling** — If a file with the same name already exists in the destination folder, the script automatically appends a counter (e.g., `report_1.pdf`) to avoid overwriting.
- **Self-aware** — The script skips itself if it is located inside the target directory.
- **Zero dependencies** — Uses only Python standard libraries (`os`, `sys`, `shutil`). No installation of third-party packages required.

## 3. Impact

### Before
```
Downloads/
├── budget_2025.xlsx
├── holiday_photo.jpg
├── setup.exe
├── meeting_notes.docx
├── podcast_ep12.mp3
├── project.tar.gz
├── dashboard.py
├── mystery_file.xyz
└── presentation_final.pptx
```

### After
```
Downloads/
├── Data/
│   └── budget_2025.xlsx
├── Image/
│   └── holiday_photo.jpg
├── Executable/
│   └── setup.exe
├── Document/
│   └── meeting_notes.docx
├── Audio/
│   └── podcast_ep12.mp3
├── Archive/
│   └── project.tar.gz
├── Code_Script/
│   └── dashboard.py
├── Other/
│   └── mystery_file.xyz
└── Presentation/
    └── presentation_final.pptx
```

### Anomaly & Suspicious File Detection

An often-overlooked benefit of automated sorting is **visibility**. Once files are organized, unusual items stand out immediately:

- **Unexpected executables** (`.exe`, `.bin`, `.msi`) appearing in a folder that should only contain documents may indicate malware or unauthorized software.
- **Unfamiliar archive files** (`.zip`, `.rar`) from unknown sources become easy to spot and investigate.
- **Files landing in "Other"** deserve attention — unrecognized extensions may be renamed/disguised files or corrupted downloads.

By sorting first, you create a clean baseline that makes anomalies far easier to detect.


## 4. Skills Demonstrated

| Skill | How It's Applied |
|---|---|
| **Python fundamentals** | File I/O, control flow, string manipulation, functions |
| **Standard library usage** | `os` for path handling, `shutil` for file operations, `sys` for exit codes |
| **Data structure design** | Dictionary mapping categories to extension sets for O(1) lookups |
| **Edge case handling** | Filename collisions, compound extensions (`.tar.gz`), extensionless files, self-skipping |
| **Clean code practices** | Modular functions, docstrings, clear variable naming, two-pass logic (scan then act) |
| **User input validation** | Graceful handling of empty input and invalid directory paths |
| **Security awareness** | Architecture that surfaces suspicious files through categorization |


## 5. How to Run

### Prerequisites

- **Python 3.6+** installed on your system. No third-party packages needed.

### Steps

**1. Download the script**

Save `sort_files.py` to any location on your computer.

**2. Open a terminal** (Command Prompt, PowerShell, or Terminal)

**3. Run the script**

```bash
python sort_files.py
```

**4. Enter the path** when prompted

```
Enter the path to the directory to sort: /Users/yourname/Downloads
```

**5. Review the output**

The script will print each action it takes:

```
Created folder: Image/
  Moved: holiday_photo.jpg -> Image/
Created folder: Document/
  Moved: meeting_notes.docx -> Document/
Created folder: Executable/
  Moved: setup.exe -> Executable/

Done! Moved 9 file(s) into 6 category folder(s).
```

### Platform Compatibility

| OS | Path Example |
|---|---|
| **Windows** | `C:\Users\YourName\Downloads` |
| **macOS** | `/Users/YourName/Downloads` |
| **Linux** | `/home/yourname/Downloads` |


> **Tip:** Run the script periodically on your Downloads folder to keep it organized and quickly spot anything that doesn't belong.

---

## 📞 Author

1. **Author:** Eric Jang
2. **Email:** thericman05@gmail.com
3. **LinkedIn:** Connect me [www.linkedin.com](https://www.linkedin.com/in/eric-jang666/)

---

**⭐ If you find this useful, please consider starring the repository!**
