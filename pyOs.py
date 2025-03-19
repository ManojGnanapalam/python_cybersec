import os

pwd = os.getcwd()
print(pwd)

list_directory = os.listdir(pwd)
for directory in list_directory:
    print('[+]',directory)


for root, directories, files in os.walk('.',topdown=False):
    for file_entry in files:
        print('[+]',os.path.join(root,file_entry))

    for name in directories:
        print('[++]',name)



from collections import Counter

counts = Counter()

for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension]+=1

for extension, count in counts.items():
    print(f"{extension:8}{count}")
    
