
list_of_square=[]
for a in range(0,32):
    for b in range(0,32):
        if (a*b) <=999:
            if a*a+b*b <= 999 and a*a+b*b>=100 :
                list_of_square.append(a * a + b * b)
list_of_square=sorted(list_of_square)
list_of_square=list(set(list_of_square))

list_lk_abc=[]
for a in range(len(list_of_square)):
    if (list_of_square[a]+1) in list_of_square and (list_of_square[a]+2) in list_of_square:
        list_lk_abc.append(list_of_square[a])

list_lk_abc=sorted(list_lk_abc)



def find(k):
    for d in range(0,32):
        for e in range(0,32):
            if d*d+e*e==k :
                return d,e
#找出k=a^2+b^2的a&b

list_want=[]
def find2(k):
    for d in range(0,32):
        for e in range(0,32):
            if d*d+e*e==k :
                tuple_want=(d,e)
                list_want.append(tuple_want)
                del tuple_want
                #把分解出来的两个放d&e里面
    if len(list_want)==1:

        d=list_want[0][0]
        e=list_want[0][1]
        del list_want[:]
        if d>e:
            d,e=e,d
        return d,e
    else:
        del list_want[0]
        d=list_want[0][0]
        e=list_want[0][1]
        del list_want[:]
        if d>e:
            d,e=e,d
        return d,e



tuplex=()
tupley=()
tuplez=()

for a in range(len(list_lk_abc)):
    x = list_lk_abc[a]
    y = x+1
    z = y+1

    tuplex = find2(x)
    tupley = find2(y)
    tuplez = find2(z)
    num1 = tuplex[0]
    num2 = tuplex[1]
    num3 = tupley[0]
    num4 = tupley[1]
    num5 = tuplez[0]
    num6 = tuplez[1]
    print(f'({x}, {y}, {z}) (equal to ({num1}^2+{num2}^2, {num3}^2+{num4}^2, {num5}^2+{num6}^2)) is a solution.')

    del tuplex
    del tupley
    del tuplez








