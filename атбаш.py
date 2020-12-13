s = ''
for i in range(ord('а'), ord('я')+1):
    s += chr(i)
t = s[::-1]

slovo = 'етивафла в ми еынжолоповиторп ан ястюянем ывкуб шабта ерфиш в'
answer = ''
for elem in slovo:
    x = s.find(elem)
    answer += t[x]
print(answer)