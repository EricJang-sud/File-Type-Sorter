"""
File Sorter Script
Sorts all files in a given directory into category folders based on file extension.

Usage: python sort_files.py /path/to/directory
"""

import os
import sys
import shutil

CATEGORIES = {
    "Video": {
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v",
        ".mpg", ".mpeg", ".3gp", ".3g2", ".vob", ".ogv", ".ts", ".m2ts",
    },
    "Image": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff",
        ".tif", ".ico", ".heic", ".heif", ".raw", ".cr2", ".nef", ".psd",
        ".ai", ".eps", ".indd",
    },
    "PDF": {
        ".pdf",
    },
    "Document": {
        ".doc", ".docx", ".odt", ".rtf", ".txt", ".tex", ".wpd", ".pages",
        ".md", ".markdown", ".log", ".epub", ".mobi",
    },
    "Presentation": {
        ".ppt", ".pptx", ".odp", ".key", ".pps", ".ppsx",
    },
    "Data": {
        ".csv", ".tsv", ".xls", ".xlsx", ".ods", ".json", ".xml", ".yaml",
        ".yml", ".sql", ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",
        ".parquet", ".avro", ".hdf5", ".h5", ".sav", ".dta", ".rds", ".rdata",
    },
    "Audio": {
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".opus",
        ".aiff", ".alac", ".mid", ".midi",
    },
    "Archive": {
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz",
        ".tar.gz", ".tar.bz2", ".tar.xz", ".iso", ".dmg", ".cab", ".z",
    },
    "Code_Script": {
        ".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs", ".go", ".rs",
        ".rb", ".php", ".swift", ".kt", ".scala", ".r", ".m", ".h", ".hpp",
        ".html", ".htm", ".css", ".scss", ".sass", ".less", ".jsx", ".tsx",
        ".vue", ".sh", ".bash", ".zsh", ".bat", ".cmd", ".ps1", ".pl",
        ".lua", ".dart", ".asm", ".vb", ".vbs", ".coffee", ".groovy",
        ".makefile", ".cmake", ".dockerfile", ".tf", ".hcl",
    },
    "Executable": {
        ".exe", ".msi", ".app", ".apk", ".deb", ".rpm", ".bin", ".run",
        ".elf", ".com", ".out", ".dll", ".so", ".dylib", ".jar", ".war",
    },
}


def get_category(filename):
    """Determine the category for a file based on its extension."""
    name_lower = filename.lower()

    # Check for compound extensions like .tar.gz
    for ext in (".tar.gz", ".tar.bz2", ".tar.xz"):
        if name_lower.endswith(ext):
            return "Archive"

    # Check for extensionless files named like Makefile, Dockerfile
    base = os.path.basename(name_lower)
    if base in ("makefile", "dockerfile", "cmake"):
        return "Code_Script"

    _, ext = os.path.splitext(name_lower)
    if not ext:
        return "Other"

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    return "Other"


def sort_files(directory):
    """Sort all files in the given directory into category folders."""
    directory = os.path.abspath(directory)

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    # Collect the category folder names so we don't try to sort them
    category_folders = set(CATEGORIES.keys()) | {"Other"}

    # First pass: determine which categories are needed
    files_by_category = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Skip directories (including existing category folders)
        if os.path.isdir(item_path):
            continue

        # Skip this script itself if it's in the target directory
        if os.path.abspath(item_path) == os.path.abspath(__file__):
            continue

        category = get_category(item)
        files_by_category.setdefault(category, []).append(item)

    if not files_by_category:
        print("No files to sort.")
        return

    # Second pass: create folders only if needed and move files
    moved_count = 0
    for category, files in files_by_category.items():
        folder_path = os.path.join(directory, category)

        # Create folder only if it doesn't already exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {category}/")

        for filename in files:
            src = os.path.join(directory, filename)
            dst = os.path.join(folder_path, filename)

            # Handle name collisions
            if os.path.exists(dst):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dst):
                    dst = os.path.join(folder_path, f"{name}_{counter}{ext}")
                    counter += 1

            shutil.move(src, dst)
            print(f"  Moved: {filename} -> {category}/")
            moved_count += 1

    print(f"\nDone! Moved {moved_count} file(s) into {len(files_by_category)} category folder(s).")


if __name__ == "__main__":
    target_path = input("Enter the path to the directory to sort: ").strip()

    if not target_path:
        print("Error: No path provided.")
        sys.exit(1)

    sort_files(target_path)
