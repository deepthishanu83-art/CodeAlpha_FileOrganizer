# CodeAlpha File Organizer

## Project Description
A Python automation script designed to organize messy folders by finding all `.jpg` or `.JPG` image files in a specified source folder and automatically moving them into a dedicated `organized_images` subfolder. 

## Problem Being Solved
When working with files downloaded from the internet, transferred from cameras, or generated over time, folders often become cluttered with various file types. This script provides an automated solution to sort out image files (specifically JPGs) from other documents and files, saving time and keeping directories clean.

## Features
- **User Input:** Prompts the user to enter the source folder path dynamically.
- **Automatic Folder Creation:** Creates an `organized_images` folder inside the source folder if it does not already exist.
- **File Filtering:** Specifically identifies files ending in `.jpg` and `.JPG`.
- **Safe Moving:** Moves files without altering files inside the destination folder recursively.
- **Duplicate Handling:** Safely handles duplicate filenames by appending a number (e.g., `photo_1.jpg`) to avoid overwriting existing files.
- **Graceful Error Handling:** Handles missing folders, empty folders, and invalid inputs gracefully.
- **Summary Report:** Displays exactly how many JPG files were successfully found and moved.

## Technologies/Concepts Used
- **Python 3**
- `os` module: Used for navigating directories, checking paths, creating folders, and finding file extensions.
- `shutil` module: Used for moving files from the source path to the destination path.

## How the Automation Works
1. The program starts and asks the user for a folder path.
2. It verifies if the provided folder path is valid and exists.
3. It checks for the existence of an `organized_images` folder and creates one if necessary.
4. It iterates over all items in the source folder.
5. If an item is a file (not a directory) and ends with `.jpg` (case-insensitive), it checks if a file with the same name already exists in the destination.
6. If a duplicate exists, it renames the incoming file (e.g., `image_1.jpg`) to ensure no data is lost.
7. It moves the file into the `organized_images` folder.
8. Upon completion, it outputs a summary indicating how many files were moved.

## Folder Structure
```text
project_root/
│
├── file_organizer.py      # The main Python automation script
├── README.md              # Project documentation
└── demo_files/            # (Optional) Folder to test the script
    ├── document.txt       # Should not be moved
    ├── notes.pdf          # Should not be moved
    ├── photo1.jpg         # Should be moved
    └── photo2.jpg         # Should be moved
```

## How to Run the Program
1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command:
   ```bash
   python file_organizer.py
   ```
5. When prompted, enter the path of the folder you wish to organize. You can test it by providing the path to the `demo_files` folder.

## Sample Output
```text
========================================
        CODEALPHA FILE ORGANIZER
========================================
Enter the path to the folder you want to organize: demo_files
Created destination folder: 'organized_images'

Scanning 'demo_files' for JPG files...
Moved: photo1.jpg -> photo1.jpg
Moved: photo2.jpg -> photo2.jpg

========================================
Organization complete! 2 JPG file(s) moved to 'organized_images'.
========================================
```

---
**CodeAlpha Task 3**  
*Internship Project: File Organizer Automation*
