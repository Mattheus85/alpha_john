import os
import shutil

def organize_new_sounds(sound_dir="sounds"):
    if not os.path.exists(sound_dir):
        print(f"Directory {sound_dir} does not exist.")
        return

    for filename in os.listdir(sound_dir):
        if filename.endswith(".mp3"):
            asset_name = filename.replace('.mp3', '')
            file_path = os.path.join(sound_dir, filename)
            asset_dir = os.path.join(sound_dir, asset_name)

            if os.path.isdir(asset_dir):
                # Count existing files to determine next number
                existing_files = [f for f in os.listdir(asset_dir) if f.endswith(".mp3")]
                next_num = len(existing_files) + 1
                new_filename = f"{asset_name}_{next_num}.mp3"
                new_file_path = os.path.join(asset_dir, new_filename)

                # Move and rename the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {filename} to {new_file_path}")
            else:
                print(f"No directory found for {asset_name}")

if __name__ == "__main__":
    organize_new_sounds()
