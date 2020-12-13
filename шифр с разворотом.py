s = 'етивафла в ми еынжолоповиторп ан ястюянем ывкуб шабта ерфиш в'
answer = ''
for i in range(0, len(s), 2):
    if len(s) % 2 == 0:
        answer += s[i + 1] + s[i]
    else:
        answer += s[i]

print(answer[::-1])