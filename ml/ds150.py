import os
import random
import shutil


def select_random_files(source_dir, target_dir, num_files=150):
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directories in the target directory
        for dir_name in dirs:
            source_sub_dir = os.path.join(root, dir_name)
            target_sub_dir = source_sub_dir.replace(source_dir, target_dir)
            os.makedirs(target_sub_dir, exist_ok=True)

        # Select and copy random files to the target directory
        random_files = random.sample(files, min(num_files, len(files)))
        for file_name in random_files:
            source_file = os.path.join(root, file_name)
            target_file = source_file.replace(source_dir, target_dir)
            shutil.copy2(source_file, target_file)


# Example usage
source_directory = 'dataset'
target_directory = 'dataset150'

select_random_files(source_directory, target_directory, num_files=150)
