with open('mavis.txt', 'r', encoding='utf-8') as f:
    f.seek(53)
    print(f.read())