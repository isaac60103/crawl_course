import re
 
pattern='abc'
string='123321 abc abc abc'
match = re.findall(pattern,string)
print(match)


pattern = "a+b*c"
string = 'aabc, ac, aabbccc abb, dd'
match = re.findall(pattern, string)
print(match)

pattern = "a*b+c"
string = 'abbbbc, bc, bcccc,c, acc'
match = re.findall(pattern, string)
print(match)

pattern = "[0-9]+"
string = 'there are 77 apples, 110 bananas, and 5 pineapples'
match = re.findall(pattern, string)
print(match)


pattern = "[1-3]+"
string = 'abc123, aaabbcc111123, aaa123333bbccc, 1222223'
match =re.findall(pattern, string)
print(match)


pattern = "[dor]mit"
string = 'admit, commit, emit, omit, permit'
match = re.findall(pattern, string)
print(match)

pattern = "isa{2,5}c"
string = 'These are my friends kevin, andy, isaac, isac, isaaaac, isaaac,and maggie'
match = re.findall(pattern, string)
print(match)

pattern = "[A-Z]+[a-z]"
string = 'ABi, BBc, CNn, ai, be, cd'
match = re.findall(pattern, string)
print(match)

pattern = "\..{3}\."
string = 'www.yahoo.com.tw , www.ntu.edu.tw , www.test.gov.tw'
match = re.findall(pattern, string)
print(match)

pattern = "I have a dream|I don't have to work"
string = 'I have a dream that I don\'t have to work'
match = re.findall(pattern, string)
print(match)

pattern = "([A-Za-z0-9._]+@[A-Za-z.]+(com|edu))"
string = 'isaac60103@gmail.com, isaac60103@hotmail.com, kevin@yahoo.com'
match = re.findall(pattern, string)
print(match)


