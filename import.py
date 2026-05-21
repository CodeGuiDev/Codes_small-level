import sys

import modulos

print('qual o nome deste modulo', __name__)
print(*sys.path, sep='\n')