# L = [10,16,18]
# L.append(20)
# print(L)
#
# #L=L.append(L,20)
#
#
# x=17
# x.bit_length()
# print(bin(x)[2:])
# print(len(bin(x)[2:]))
#
# x=3+4j
# print(x.conjugate())

#def f(*,a=1, b=1, c=0):
    #print(a,b,c)

#f(b=3,a=2,c=-5)
#f(4,c=5)
#f(4,5,-2)
#f(a=4,c=8,b=5)


# def initialiazation(*,a=1,b=0,c=0):
#     if a==0:
#         print('a canot be equal to 0')
#         equation=('a':a,'b'=b,'c'=c,'root1'=None,'root2'=None)
#     compute_routes(equation)
#     return equati


from math import sqrt



class SecondOrderEquation:
    def __init__(self, *, a=1, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.root_1, self.root_2 = self._compute_roots()
        # 变量有前缀self的时候代表是当前class的一个attribute，没有这个前缀则是一个local variable

    def __repr__(self):
        return f'SecondOrderEquation({self.a}, {self.b}, {self.c})'

    def __str__(self):
        # __str__是print()函数会查询的method
        output_string = ''
        if self.a == 1:
            output_string = 'x^2'
        elif self.a == -1:
            output_string = '-x^2'
        else:
            output_string = f'{self.a}x^2'
        if self.b == 1:
            output_string += ' + x'
        elif self.b == -1:
            output_string += ' - x'
        elif self.b > 0:
            output_string += f' + {self.b}x'
        elif self.b < 0:
            output_string += f' - {-self.b}x'
        if self.c > 0:
            output_string += f' + {self.c}'
        elif self.c < 0:
            output_string += f' - {-self.c}'
        return output_string

    def _compute_roots(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta < 0:
            root_1, root_2 = None, None
        elif delta == 0:
            root_1 = -self.b / (2 * self.a)
            root_2 = root_1
        else:
            root_1 = (-self.b - sqrt(delta)) / (2 * self.a)
            root_2 = (-self.b + sqrt(delta)) / (2 * self.a)
        return root_1, root_2

    def get_roots(self):
        return self.root_1, self.root_2


SEO1 = SecondOrderEquation(a=1, b=-2, c=1)
print(SEO1)
SEO2 = SecondOrderEquation(a=-7, c=-4)
print(SEO2)
SEO3 = SecondOrderEquation()
print(SEO3)
SEO1, SEO2, SEO3

print(SecondOrderEquation.get_roots(SEO1))
print(SEO1.get_roots())
SEO1.a, SEO1.b, SEO1.c, SEO1.root_1, SEO1.root_2

