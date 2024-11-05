import os
s = os.getcwd()
print(s)
try:
    os.chdir(s+r'\solutions')
    s= os.getcwd()
    print(s)
except:
    print('Bunday yol mavjud emas')