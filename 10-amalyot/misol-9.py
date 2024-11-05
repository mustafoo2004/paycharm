import os
import shutil
path_file = r'C:\Python Project\pythonProject\.venv\Najotjon\11_18_2024 file\hew Solutions\Solutions_1'
if os.path.exists(path_file):
    print(path_file)
try:
  print(path_file)
  shutil.rmtree(path_file)
  print(f"Katalog o chirildi.")
except FileNotFoundError as e:
  print (f"Xatolik: {e}")
except Exception as e:
  print(f"Boshqa xatolik: {e}")
