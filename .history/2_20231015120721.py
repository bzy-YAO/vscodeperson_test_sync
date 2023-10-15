import re

str = 'this is @ bu yaoshi 222dakldsa--..sdakl'
r = re.findall('@[^#].*', str)
print(r)