# 格式化字符 %s

# 把2这个字符串放入x这个字符串里
x = "There are %d kinds of people in the world" % 2
binary = "binary"
do_not = "do_not"
# 把多个字符串放入y这个字符串里
y = "Those who knows %s and those who %s." % (binary, do_not)

print (x)
print (y)

# print 的所有内容都要放在括号内， 打印和输入的结合
print ("I said %r." % x)
print ("I also said %s." % y)

haha = False
a = "Isn't that very normal? %r"

# 打印出逻辑词，中间的这个%，怎么作用相当于加号呢？因为在把字符串赋给a时，并未定义%的内容，在print函数里把它定义为haha
print (a % haha)

# 把两个字符串连在一起，但是这真的有实际的用处吗？为啥不直接写成一个？
w = "This is the left side of..."
e = "a string with a right side"
print (w + e)
