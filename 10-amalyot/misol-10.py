import os.path
import shutil
dest_path = r'C:\Python Project\pythonProject\.venv\Najotjon\11_18_2024 file\New\Solutions'
if os.path.exists(dest_path):
  print(dest_path)
source_path = r'C:\Python Project\pythonProject\venv\Najotion\11_16_2024 file\New\Solutions_1'
if os.path.exists(source_path):
   print(source_path)
try:
  copy_file = shutil.move(source_path, dest_path, copy_function=shutil.copytree)
  print("Fay nusxalandi: (copy_file)")
except FileNotFoundError as e:
  print(f"xatolik: {e}")
except Exception as e:
  print(f"boshqa xatolik: {e}")