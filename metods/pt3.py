import sys
import os


arg = sys.argv
qtd = len(arg)

if qtd <= 1:
    print(': (')

so = False
if '-a' in arg:
    so = True

for file in os.listdir('.'):
    if so:
        if os.path.isfile(file)
        print(file)

sys.exit()
