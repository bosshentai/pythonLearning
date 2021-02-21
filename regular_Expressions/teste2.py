import re


pattern = re.compile('"(^[a-zA-Z0-9_.+-]+Q[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"')
string = 'search inside of this text please!'

#print('search' in string)

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

print(b)
print(c)
print(d)
