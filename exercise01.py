"""
交换变量
"""

str_number01 = input("请输入第一个变量：")
str_number02 = input("请输入第二个变量：")
temp = str_number01
str_number01 = str_number02
str_number02 = temp
print("第一个变量是：" + str_number01)
print("第二个变量是：" + str_number02)
