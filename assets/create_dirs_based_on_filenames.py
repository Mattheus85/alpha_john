import os
import shutil

def organize_sounds(sound_dir="sounds"):
    # Ensure the sounds directory exists
    if not os.path.exists(sound_dir):
        print(f"Directory {sound_dir} does not exist.")
        return

    # Iterate through files in sounds/
    for filename in os.listdir(sound_dir):
        if filename.endswith(".mp3"):
            # Get the base name (e.g., 'a' from 'a.mp3')
            asset_name = filename.replace('.mp3', '')
            file_path = os.path.join(sound_dir, filename)

            # Create subdirectory for the asset
            asset_dir = os.path.join(sound_dir, asset_name)
            os.makedirs(asset_dir, exist_ok=True)

            # New file name (e.g., 'a_1.mp3')
            new_filename = f"{asset_name}_1.mp3"
            new_file_path = os.path.join(asset_dir, new_filename)

            # Move and rename the file
            shutil.move(file_path, new_file_path)
            print(f"Moved {filename} to {new_file_path}")

if __name__ == "__main__":
    organize_sounds()
