# count
from itertools import count
c1 = count()
r1 = range(10)
print(f'c1', hasattr(c1, '__iter__'))
print(f'c1', hasattr(c1, '__next__'))
print(f'r1', hasattr(r1, '__iter__'))
print(f'r1', hasattr(r1, '__next__'))
