import cmath
num = float( input ('请输入一个数：'))
num_sqrt = num** 0.5
print('%0.3f的平方根为 %0.3f'%(num,num_sqrt))

num1 = float(input('请输入一个数：'))
num_sqrt1 = cmath.sqrt(num1)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num1 ,num_sqrt1.real,num_sqrt1.imag))
