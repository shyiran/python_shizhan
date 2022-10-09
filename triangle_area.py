#通过用户输入三角形三边长度，并计算三角形的面积
a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
c = float(input("请输入第三个数："))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)
