# 通过用户输入两个变量，并相互交换
x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

# x,y = y,x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
