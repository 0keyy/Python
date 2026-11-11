# print("hello")
# print(type("hello"))
# print(type("3.14"))
# print(type("10"))
# print(type(True))
# print(type(False))
# print(type(None))


num = -100
print(type(num))
print(isinstance(num,int))



#字符串
s1 = "hello"
s2 = "hell" \
"o"
s3 = 'hello'

s4 = """
1
2
3
4
"""
print(s1,s2,s3,s4)
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))


#定义字符串 
msg = 'it\' is very importent'




#字符串拼接
s1 = "人生苦短" "我用python"  "ok"
print(s1)
msg1 = "人生苦短"
msg2 = "我用Mac"
print("我说：" + msg1 + msg2)


name = "yz"
age = 18 
prof = "物联网工程"
hobby = "game"

print("大家好我是" + name + "今年" + str(age) + "专业是" + prof + "爱好是" + hobby)



name2 = "123"

# print("我是%s" % name2)


#%格式化

name = "yz"
age = 18 
prof = "物联网工程"
hobby = "game"

# print("大家好我是%s今年%s专业是%s爱好是%s" % (name,age,prof,hobby) )

#f-string 推荐写法
name = "yz"
age = 18 
prof = "物联网工程"
hobby = "game"

print(f"大家好我是{name}今年{age}专业是{prof}爱好是{hobby}")


#format
name = "yz"
age = 18 
prof = "物联网工程"
hobby = "game"

# print("大家好我是{}今年{}专业是{}爱好是{}".format(name,age,prof,hobby) )