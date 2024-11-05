import os
import shutil
dest_path = os.getcwd()
if os.path.exists(dest_path):
 print(dest_path)
source_path = r'C:\Python Project\pythonProject\.venv\Najotjon\11_10_2024 file\misol-5.py'
if os.path.exists(source_path):
  print(source_path)
try:
  copy_file = shutil.copy2(source_path, dest_path)
  print(f"Fayl nusxalandi: {copy_file}")
except FileNotFoundError as e:
  print(f"Xatolik: {e}")
except Exception as e:
  print(f"Boshqa xatolik: {e}")