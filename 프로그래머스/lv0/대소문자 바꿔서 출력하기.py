str = input()
ans = ''
for i in str:
    if 65 <= ord(i) <= 90 :
        ans += i.lower()
    elif 97 <= ord(i) <= 122:
        ans += i.upper()
print(ans)
        