'''
Created on 2018年4月13日
@author: rocky.wang
'''
import re

pattern = r'is'
string = "This is a apple"
match = re.findall(pattern, string)
print(match)


# 特殊字元要加 \
# [\^$.|?*+()

# 1+2=3

string = "1+2=3"
pattern = r'1\+2=3'
match = re.findall(pattern, string)
print(match)


# 任意字元 .
pattern = r'a.man'
string = "I'm a man"
match = re.findall(pattern, string)
print(match)

pattern = r'.a'
string = "banana"
match = re.findall(pattern, string)
print(match)


# 多個字元
pattern = r'[aA]'
string = "A apple"
match = re.findall(pattern, string)
print(match)

pattern = r'[aeiou]'
string = "There is a apple"
match = re.findall(pattern, string)
print(match)

# 多個字元 - 連續
pattern = r'[a-z]' # 等同 [abcdefghijklmnopqrstuvwxyz]
string = "There is a apple"
match = re.findall(pattern, string)
print(match)

pattern = r'[a-zA-Z]'
string = "I'am 20 years old."
match = re.findall(pattern, string)
print(match)

pattern = r'[5-8]' # 等同 [5678]
string = "0980987163"
match = re.findall(pattern, string)
print(match)

# 多個字元 - ^ 不是 xx
pattern = r'[^a]' # not a 的其他字元
string = "There is a Apple 123"
match = re.findall(pattern, string)
print("------------------")
print(match)
print("------------------")

pattern = r'[^0-9]'
string = "I'am 20 years old."
match = re.findall(pattern, string)
print(match)


# 多個字元縮寫
# \d - digit [0-9]
# \w - word [A-Za-z0-9_]
# \s - space [\n\r\t]

pattern = r'\we'
string = "There is a apple"
match = re.findall(pattern, string)
print(match)

pattern = r'\d\d' # 其實等於 \d{2} 
string = "I'am 20 years old."
match = re.findall(pattern, string)
print(match)

# 多個字元縮寫 non
# \D - non-digit [^\d]
# \W - non-word [^\w]
# \S - non-space [^\s]

pattern = r'\W' 
string = "I'am 20 years old."
match = re.findall(pattern, string)
print(match)

string = "1+2=3"
pattern = r'\D' # 等同 r'[^\d]'
match = re.findall(pattern, string)
print(match)

pattern = r'android|and' # 最正確的版本，比較精準的放前面，注意不要有空白
string = "iOS and android"
match = re.findall(pattern, string)
print(match)




