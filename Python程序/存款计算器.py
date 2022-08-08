#存款计算器.py
money=eval(input("你要存入多少钱？"))
rate=0.03

total_1 = money * (1+rate)
total_2 = total_1 * (1+rate)
total_3 = total_2 * (1+rate)

print("你的存款本金是：",money)
print("一年后的总和是：",total_1)
print("两年后的总和是：",total_2)
print("三年后的总和是：",total_3)
