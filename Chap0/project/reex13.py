# 把python的功能引入脚本，argv是argument variable参数变量
from sys import argv

# 将argv解包unpack，把4个参数变量赋予单独的变量名
script，first，second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

# 运行不成功，说first到third未定义？？？
