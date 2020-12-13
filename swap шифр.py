s = 'етивафла в ми еынжолоповиторп ан ястюянем ывкуб шабта ерфиш в'
for key in range(1,27):
    ans = ''
    for elem in s:
        x = ord(elem) - key
        if x < ord('a'):
            x += 26
        ans += chr(x)
    print(ans)