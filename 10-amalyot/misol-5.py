import os

my_cws =os.getcwd()
new_dir ='solutions'
path = os.path.join(my_cws, new_dir)
os.mkdir(path)
print(os.listdir())