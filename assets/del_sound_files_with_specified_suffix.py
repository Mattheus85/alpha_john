import os
import argparse

def remove_accidental_files(sound_dir="sounds", suffix="_3.mp3", dry_run=False):
    if not os.path.exists(sound_dir):
        print(f"Directory {sound_dir} does not exist.")
        return

    for asset_name in os.listdir(sound_dir):
        asset_dir = os.path.join(sound_dir, asset_name)
        if os.path.isdir(asset_dir):
            for filename in os.listdir(asset_dir):
                if filename.endswith(suffix):
                    file_path = os.path.join(asset_dir, filename)
                    if dry_run:
                        print(f"Would delete {file_path}")
                    else:
                        os.remove(file_path)
                        print(f"Deleted {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove files with specified suffix from sounds subdirectories.")
    parser.add_argument('--dry-run', action='store_true', help="Print files that would be deleted without deleting them.")
    args = parser.parse_args()
    remove_accidental_files(dry_run=args.dry_run)
