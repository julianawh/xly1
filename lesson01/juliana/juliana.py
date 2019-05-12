# 乘法表
for j in range(1,10):
    for i in range(1,10):
        if i > j:
            continue
        print('  {} * {} = {}'.format(i,j,i*j),end="")
    print()

# 猜数游戏
import random
suiji = random.randint(0, 100)
print("随机数是{}".format(suiji))
for i in range(1, 7):
    num = int(input("请输入数字"))
    if suiji == num:
        print("猜对了")
        break
    elif suiji < num:
        print("大了")
    elif suiji > num:
        print("小了")
