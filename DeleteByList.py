import os
import shutil
directory = input("Songs folder?")

f = open('workfile', 'r')
dictionary = f.read().split('\n')

Beatmaps_Present = [(name[:name.index(' ')], name) for name in os.listdir(directory) if os.path.join(directory, name)]

print(dictionary)
print(Beatmaps_Present)

for number, name in Beatmaps_Present:
    if number not in dictionary:
        shutil.rmtree(os.path.join(directory, name), ignore_errors=True)
        print("deleted  {}".format(number))
    else:
        print("spared   {}".format(number))
