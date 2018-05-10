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
#当参数为实现了buffer接口的object对象时，将以只读方式将字节读取到数组后返回
#当参数是一个可迭代对象，那么这个元素必须符合0-255之间
#bytearray([1,2,3])

#8.bytes([source[,encoding[,errors]]])函数，返回一个新的不可修改的字节数组，每个元素必须在0-225之间，与bytearray具有相同的行为，区别在于不可修改，参数为字符串，整数，对象，可迭代对象

#9.callable(object)函数，检测对象是否可被调用
# print(callable(callable))			#True
# print(callable(19))				#False
#类对象都是可调用的对象，类的实例对象是否可调用，取决于类是否定义了__call__方法
# class A:
	# pass
# # print(callable(A))				#True
# a = A()
# # print(callable(a))				#False
# a()									#报错
# class B:
	# def __call__(self):
		# print('instances are callable now.')
# print(callable(B))				#True
# b = B()
# print(callable(b))				#True
# b()	

#10.chr()函数,返回整形参数值所对应的Unicode字符的字符串表示,它的功能与ord（）函数相仿，传入的参数范围必须在0-1114111（十六进制为0x10FFFF）之间，否则将报错
# print(chr(98))						#‘b'
#print(chr('a'))					#报错
# print(type(chr(98)))				#<class 'str'>

#11.classmethod(function)函数，装饰器函数，用来表示一个方法为类方法,类方法第一个参数为类对象参数，在方法被调用时自动将类对象传入
# class C:
	# @classmethod
	# def f(cls,arg1):
		# print(cls)
		# print(arg1)
# print(C.f)
# c=C()
# print(c.f)
# class F(C):
	# pass
# print(F.f)

#12.compile(source,filename,mode,flags=0,dont_inherit=False,optimize=-1)函数，将source编译为代码或AST对象，代码对象能够通过exec语句来执行或者eval（）进行求值，source为需要动态执行的代码段，filename为代买文件名，mode制定代码编译的种类，可以指定exec，eval，single，当source包含流程语句时，mode为exec，当source中包含一个简单的求值表达式，mode为eval，当source包含交互式命令，mode为single
#流程控制
# code1 = 'for i in range(10):print(i)'
# compile1 = compile(code1, '', 'exec')
# exec(compile1)
#简单表达式
# code2 = '1+2+3+4+5'
# compile2 = compile(code2, '', 'eval')
# print(eval(compile2))
#交互式命令
# code3 = 'name = input("please input your name:")'
# compile3 = compile(code3, '', 'single')
# exec(compile3)
# print(name)

#13.complex([real[,imag]])函数，返回一个负数。有两个参数
#当两个参数都不提供时，返回复数0j
# a = complex()
# print(a)		
#当参数为字符串时，此字符串需是一个能表示复数的字符串
# a = complex('1+3j')
# print(a)
#当参数为int或float时，第二个参数可为空，如果有第二个参数，第二个参数也需要为int或float
# a = complex(3, 4)
# print(a)

#14.delattr(object,name)函数，用来删除指定对象的指定名称的属性，和setattr函数作用相反
class A:































