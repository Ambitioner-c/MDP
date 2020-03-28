# ****************************************************************************************
# 输出希腊字母，及对应的ASCII字符
n = 0
for i in range(945, 970):
    print(chr(i), i, end='|')

    n += 1
    if n % 8 == 0:
        print('\n')

# 将参数存在dict中
greek_litter = dict()

greek_litter['α'] = 0.5
greek_litter['γ'] = 0.5
print('参数字典：', greek_litter)
