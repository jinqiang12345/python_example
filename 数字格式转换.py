import time
dec = int(input("请输入数字："))

print("十进制数为：", dec)
print("转换为二进制数为：", bin(dec))
print("转换为八进制数为：", oct(dec))
print("转换为十六进制数为：", hex(dec))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))