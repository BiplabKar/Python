s = input()

res = ''
for i in range(len(s)):
    res = res + chr(ord('a')-ord(s[i])+ord('z'))

print(res)