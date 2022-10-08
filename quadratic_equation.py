import cmath

a = float(input('请输入第一个数：'))
b = float(input('请输入第二个数：'))
c = float(input('请输入第三个数：'))

d = b ** 2 - 4 * a * c

sol1 = (-b + cmath.sqrt(d)) / 2 * a
sol2 = (-b - cmath.sqrt(d)) / 2 * a

print('结果为 {0} 和 {1}'.format(sol1, sol2))
