# # 占位符，%s字符串，%d数字，%f浮点数
# print('Hello,%s'%'world')				#Hello,world
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print("%2d-%02d"%(3,1))                 # 3-01
# print('%.2f' % 3.1415926)				#3.14
# # format会用传入的参数依次替换字符串内的占位符{0}，{1}...
# print('Hello,{0}成绩提升了{1:.1f}%'.format('小明',17.125))

# # list是种有序的集合
# classmates = ['Michael', 'Bob', 'Tracy']
# # len（）函数可以获得lisit的个数
# print(len(classmates))
# # 用索引来访问list中每个位置的元素，索引从0开始
# print(classmates[0])				
# # 可以用[-1]做索引，取得最后一个元素，以此类推，可以用[-2]取倒数第二个...
# print(classmates[-1])
# # list是个有序列表，所以可以用append（）函数追加元素到末尾
# classmates.append('Adam')
# print(classmates)
# # 可以用insert（）函数添加元素到指定位置，如索引1的位置，也就是第二位
# classmates.insert(1, 'Jack')
# print(classmates)
# # pop（）方法可以删除list末尾的元素
# classmates.pop()
# print(classmates)       #'Adam'就被删掉了
# # pop(i)可以删除索引为i的元素
# classmates.pop(1)
# print(classmates)		#'Jack'被删除掉了
# # 直接赋值可以替换元素
# classmates[1] = 'Sarah'
# print(classmates)		#‘Bob’被替换为了‘Sarah’
# # list数据类型可以不痛，也可以嵌套
# L = ['Apple', 123, True]
# s = ['python', 'java', ['asp', 'php'], 'scheme']

# # tuple元祖和list列表类似，但是元祖不能被修改，它没有append(),insert()...等方法
# t = (1, 2)
# t = ('Michael', 'Bob', 'Tracy')
# t = ()
# # 当只有一个元素时，不能定义成（1），要写成（1，），不然就是定义了一个数字而不是元祖
# t = (1, )

#练习：请用索引取出下面list的指定元素：
# L = [
    # ['Apple', 'Google', 'Microsoft'],
    # ['Java', 'Python', 'Ruby', 'PHP'],
    # ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

#条件判断
# age = 3
# if age>=18:
	# print("Your age is", age)
	# print("adult")
# elif age>=6:
	# print("teenager")
# else:
	# print("kid")
#input()的返回值是str，不能和整数相比，必须转化为int（）类型	
# s = input("birth:")
# birth=int(s)
# if birth<200:
	# print('00前')
# else:
	# print('00后')
	
# 练习

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
# height = float(input("请输入您的身高："))
# weight = float(input("请输入您的体重："))
# bmi = float(weight/(height**2))
# if bmi < 18.5:
	# print("过轻")
# elif bmi <25 and bmi >18.5:
	# print("正常")
# elif bmi <28 and bmi >25:	
	# print("过重")
# elif bmi <32 and bmi >28:	
	# print("肥胖")
# else:	
	# print("严重肥胖")

#循环,for x in ...把每个元素带入x循环
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
	# print(name)
#range()函数可以生成一个整数序列，list（）函数可以把他转换为列表
#list(range(5))
#0到100 的累加
# sum = 0
# for x in range(101):
	# sum = sum+x
# print(sum)
#while循环
# sum = 0
# n = 99
# while n>0:
	# sum = sum+n
	# n=n-2
# print(sum)
# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
#L = ['Bart', 'Lisa', 'Adam']
# for x in L:
	# print("Hello,",x)
# n = 0
# while n<len(L):
	# print("Hello,",L[n])
	# n= n+1
#break跳出while循环
# n=1
# while n<=100:
	# if n>10:
		# break
	# print(n)
	# n=n+1
# print('END')
#continue跳出本次循环，开始下次循环
# n = 0
# while n<100:
	# n=n+1
	# if n%2 == 0:
		# continue
	# print(n)

#dict字典，键值对，无序的
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 67










