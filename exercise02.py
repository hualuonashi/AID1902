"""
在控制台中获取小时，分钟，秒，计算总秒数
"""

int_hour = int(input("请输入小时数："))
int_min = int(input("请输入分钟数："))
int_s = int(input("请输入秒数："))

result = int_hour * 60 * 60 + int_min * 60 + int_s
print(result)