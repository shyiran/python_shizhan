# 通过使用 if...elif...else 语句判断数字是正数、负数或零
num = float(input("输入一个数字: "))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

#   
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")

#
while True:
    try:
        # num=float(input('请输入一个数字：'))
        if num == 0:
            print('输入的数字是零')
        elif num > 0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')
