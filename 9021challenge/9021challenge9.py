import sys
#CODE BY XINCHEN WANG FOR 9021

min_i = 10
max_i = 76
max_j = 87
max_k = 98
i=0
j=0
k=0



product_digits=[]
product=0
# def find(i, j, k):
#     product = i * j * k
#     for a in range(1, 7):
#         if product > 0:
#             product_digits.append(product % 10)
#             product = product // 10
#     if sorted(product_digits)==sorted(used_digits):
#         del product_digits[:]
#         del used_digits[:]
#         return True
#     else:
#         del product_digits[:]
#         del used_digits[:]
#         return False

used_digits_i= []
used_digits_j= []
used_digits_k= []
#每次使用前把上一次用来记录数字的列表清空
for i in range(min_i, max_i + 1):
    if (i // 10) != (i % 10):
        del used_digits_i[:]
        used_digits_i.append(i // 10)
        used_digits_i.append(i % 10)
        for j in range(i+1, max_j + 1):
            if (j // 10) != (j % 10) and (j // 10) not in used_digits_i and (j % 10) not in used_digits_i:
                del used_digits_j[:]
                used_digits_j=used_digits_i.copy()
                used_digits_j.append(j // 10)
                used_digits_j.append(j % 10)
                for k in range(j + 1, max_k + 1):
                    if (k // 10) != (k % 10) and (k // 10) not in used_digits_j and (k % 10) not in used_digits_j:
                        del used_digits_k[:]
                        used_digits_k=used_digits_j.copy()
                        used_digits_k.append(k//10)
                        used_digits_k.append(k%10)
                        product=i*j*k
                        for a in range(1,9):
                            if product>=1 and (product%10) not in product_digits:
                                product_digits.append(product%10)
                                product=product//10
                        if sorted(product_digits)==sorted(used_digits_k):
                            print(f'{i} x {j} x {k} = {i*j*k} is a solution.')
                            del product_digits[:]
                            del used_digits_k[:]
                        else:
                            del product_digits[:]
                            del used_digits_k[:]

















