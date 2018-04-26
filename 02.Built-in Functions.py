#1.abs(x)函数,返回传入参数的绝对值
#abs(-100)

#2.all(iterable)函数,如果传入的可迭代对象的元素都不为空，则返回True，
# m=(1,2,3)
# l=[0,1,2,3]
# print(all(m))
# print(all(l))

#3.any(iterable)函数，如果传入的可迭代对象不为空，则返回True，和all的区别在于all（）代表对象内的元素，any（）函数代表的是传入的对象本身
# d={}
# l=[0,1,2,3]
# print(any(d))
# print(any(l))

#4.ascii(obj)函数，返回一个可打印的对象字符串方法表示，如果是非ascii字符就会输出\x，\u等字符，与python2中的repr（）函数一样
# print(ascii('china'))		#输出‘china’
# print(ascii('中国'))      #输出'\u4e2d\u56fd'

#5.bin(x)函数，将一个int整数类型转换为一个以‘0b’为前缀的二进制字符串类型
#print(bin(5))				#输出0b101
#如果参数x不是一个整数，则想必须定义一个__index__(),并且方法返回值必须为整数
# class A:
	# def __index__(self):
		# return 3
# a = A()
# print(bin(a))

#6.bool([x])函数，返回一个布尔值，若传入参数为空返回False,参数可传入数字，字符串，列表，元祖，字典
# print(bool(123))
# print(bool([ ]))

#7.bytearray([source[,encoding[,errors]]])函数，返回一个新的字节数组，当三个参数都没有的情况下，返回长度为0的字节数组，当参数为字符串时，encoding参数也必须提供
# s = bytearray('中国','utf8')
# print(s)					#输出bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')
#当参数为数字时，返回这个数字所指定长度的空字节数组
# s = bytearray(3)
# print(s)					#输出bytearray(b'\x00\x00\x00')
