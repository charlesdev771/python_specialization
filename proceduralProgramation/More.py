from itertools import zip_longest
from itertools import combinations
from itertools import groupby
lisT = [1,2,3]
print(hasattr(lisT, '__iter__'))
print(hasattr(lisT, '__next__'))

for v in lisT:
    print(v)

citys = ['aa', 'bb']

estates = ['aaa', 'bbb']

citis_stats = zip_longest(citys, estates, fillvalue="Test")
print(list(citis_stats))

for grupo in combinations(citys, 2):
    print(grupo)
