
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
