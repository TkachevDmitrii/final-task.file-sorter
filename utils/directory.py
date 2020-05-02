import os
import shutil


# Функция замены директории файла
def move_to(s_dir, d_dir, old_file_name, new_file_name, artist, album):
    old_path = os.path.join(s_dir, old_file_name)
    new_path = os.path.join(d_dir, artist, album, new_file_name)
    return shutil.move(old_path, new_path)

