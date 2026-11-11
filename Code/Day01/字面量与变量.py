#字面量写法
print(100)
print(3.14)
print(True)
print(False)
print("hello world")
print("----------")
print(None)

#布尔类型本质是整数类型

print(True + 1) #=2
print(False - 1) # = -1



#---------------------------
#python是动态类型语言，开发中推荐只存储一种数据类型的数据
num = 1114.1
print(num)

num = num + 1

print(num)

num = "ok"

print(num)


#案例
base = 20.7
incr = 50
print("未来第一个月的播放量为",base+incr)
print("未来第二个月的播放量为",base+incr*2)

#拓展
base,incr = 20.7,50

print("未来第一个月的播放量为",base+incr)
print("未来第二个月的播放量为",base+incr*2)




#案例
a = 20
b = 10
a,b = b,a
print(a,b)

n = a
a = b
b = n
print(a,b)


a = 100
b = 200
c = 300

a,b,c = c,a,b
print(a,b,c)

print(type(a))
