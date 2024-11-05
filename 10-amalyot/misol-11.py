import os
folder_path = 'C:\Men_bekorchiman'
try:
    os.makedirs(folder_path)
    print(f"{folder_path} papkasi muvaffaqiyatli yaratildi.")
except FileExistsError:
    print(f"{folder_path} papkasi allaqachon mavjud.")
except Exception as e:
    print(f"Xato: {e}")