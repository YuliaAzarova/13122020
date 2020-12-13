'''
1. Считаем длину текста
2. По очереди (в цикле) все буквы ставим на своё место
'''
shifr = 'вйшаенсутдьзнеармеочсут'
lenght = len(shifr)
original = [None] * lenght
y = z = 0
for x in range(lenght):
    print(x,y,z)
    if x % 2 == 0:
        original[y] = shifr[x]
        print(original)
        y += 1
    else:
        original[lenght-y] = shifr[x]
        print(original)
        z += 1
print(original)
myString = ''.join(original)
print(f'Итог:\nБыло шифр {shifr},\nя его разгадала и это: \n{myString}')