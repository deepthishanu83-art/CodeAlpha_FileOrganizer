import os
import shutil

def get_unique_filename(destination_folder, filename):
    """
    Generate a unique filename if the file already exists in the destination folder.
    Appends _1, _2, etc. to the filename until a unique name is found.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def main():
    print("=" * 40)
    print("        CODEALPHA FILE ORGANIZER")
    print("=" * 40)
    
    source_folder = input("Enter the path to the folder you want to organize: ").strip()
    
    if not source_folder:
        print("Error: Please provide a valid folder path.")
        return
        
    if not os.path.isdir(source_folder):
        print(f"Error: The folder '{source_folder}' does not exist.")
        return
        
    destination_folder_name = "organized_images"
    destination_folder = os.path.join(source_folder, destination_folder_name)
    
    # Automatically create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Created destination folder: '{destination_folder_name}'")
        except Exception as e:
            print(f"Error creating destination folder: {e}")
            return
            
    print(f"\nScanning '{source_folder}' for JPG files...")
    
    moved_count = 0
    try:
        # Scan files in the source folder
        for item in os.listdir(source_folder):
            item_path = os.path.join(source_folder, item)
            
            # Skip directories (including the destination folder itself)
            if os.path.isdir(item_path):
                continue
                
            # Check if the file is a JPG or JPG
            if item.lower().endswith('.jpg'):
                # Handle duplicate filenames safely
                unique_name = get_unique_filename(destination_folder, item)
                destination_path = os.path.join(destination_folder, unique_name)
                
                # Move the file
                shutil.move(item_path, destination_path)
                print(f"Moved: {item} -> {unique_name}")
                moved_count += 1
                
    except Exception as e:
        print(f"An error occurred while moving files: {e}")
        
    print("\n" + "=" * 40)
    if moved_count > 0:
        print(f"Organization complete! {moved_count} JPG file(s) moved to '{destination_folder_name}'.")
    else:
        print("No JPG files found to move.")
    print("=" * 40)

if __name__ == "__main__":
    main()
