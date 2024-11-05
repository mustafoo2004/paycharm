import os
path = os.getcwd()
s = os.path.normcase(path)
print(s)
s = os.path.normcase('c:/users/user/python')
print(s)