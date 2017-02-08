# Python3变量定义####
#alt+cmmd+L 自动添加空格
######################################
# 1.0-字符串变量：用单引号或双引号都OK。
message = 'good thing'
message.title()  # 以首字母大写的方式先是每个单词。
message.upper()  # 全部大写
message.lower()  # 全部小写

print("hello," + message.title() + "!")  # 加号拼接字符串

print("\t goodbye!")  # 使用制表符(\t)添加空白
print("xiaoshuang:\t " + "\n\tmylover!")  # 使用换行符(\n) 换到下一行,"\n\t"换去下一行，并在下一行开头添加一个制表符。

message.rstrip()  # 删除右边空白
message.lstrip()  # 删除左边空白
message.strip()  # 删除两端空白

######################################
# 2.0-数字
2 + 3
2 * 3
2 ** 3  # 2 的三次方
import this  # python之禅

######################################
# 3.0-列表：由特定顺序的元素组成

bicycles = ['aa', 'aab', 'c', 'b', 4]
print(bicycles[0])  # 第一个元素
print(bicycles[-1])  # 最后一个元素

bicycles[-1] = '3'  # 修改
print(bicycles)
bicycles.append('bmw')  # 添加
print(bicycles)
bicycles.insert(2, 'bmw1')  # 在第2个位置添加bmw1
print(bicycles)
del bicycles[0]  # 删除语句
print(bicycles)
bicycles.pop()  # 使用pop()删除删除最后一个元素
print(bicycles)
bicycles.pop(1)  # 使用pop(i)删除索引为i的元素
print(bicycles)
bicycles.remove('b')  # 使用值来删除元素，如果有多个，则只删除第一个。

bicycles.sort()  # 按照字母顺序正序排列
bicycles.sort(reverse=True)  # 按照字母顺序倒序排列
print(bicycles)
print(sorted(bicycles))  # 不改变原始顺序，呈现顺序改变

len(bicycles)  # 计算列表长度

#  遍历整个列表
for bicycle in bicycles:
    print('\t' + str(bicycle.title()))

# 创建数值列表
for i in range(1, 6):
    print(i)  # 打印1到5数字

numbers = list(range(1, 6, 2))  # 使用list函数将range转化为列表
print(numbers)
max(numbers)
min(numbers)
sum(numbers)

# 列表解析[1.列表名，2.表达式定义列表中的值，3，for循环
squares = [value ** 2 for value in range(1, 10)]
print(squares)

# 切片操作

print(squares[0:4])  # 输出序号0-3个元素
print(squares[:4])  # 输出序号0-3个元素
print(squares[4:])  # 输出序号为5以后的元素
print(squares[-3:])  # 输出后三个元素

# 复制列表
squares2 = squares[:]

######################################
# 4.0-元组：一系列不可修改的元素组成。
dimensions = (200, 500)
## dimensions[0] = 2 ## 报错
print(dimensions[1])
dimensions = (3, 5)  # 修改元组，但无法修改其中元素
print(dimensions[0])

######################################
# 5.0-if语句

pc = ['intel', 'lenovo', 'mac', 'IBM']

for pci in pc:
    if pci == 'mac':
        print('the founder is Jobs!\n')
    elif pci == 'IBM':
        print("sorry,i don't know\t" + str(pci) + ".")
    else:
        print('oo')
######################################
# 6.0-字典
pc_a = {'name': 'intel', 'price': 10}
pc_b = {'name': 'mac', 'price': 100}

print(pc_a['name'])
print(pc_a['price'])

pc_a['product_year'] = '2017'  # 添加键－值对
pc_a['color'] = 'red'
print(pc_a)

pc = {}  # 创建一个空字典
pc['name'] = 'IBM'
pc['color'] = 'GREN'
pc['price'] = 500
print(pc)
del pc['price']  # 删除键－值
print(pc)
# 遍历键－值
for key, value in pc.items():
    print('\nkey:' + key)
    print('Value:' + value)

# 遍历键
for key in pc.keys():
    print('\nkey:' + key)

# 遍历值
for value in pc.values():
    print('\nvalue:' + value)

# 嵌套
pc2 = [pc_a, pc_b]

######################################
# 7.0-用户输入和while循环

message = input("input the age:")

# while 循环
count = 1
while count <= 5:
    print(count)
    count += 1

######################################
# 8.0-函数

def greet_user(names):
    """参数为列表"""
    for name in names:
        print("hello, " + name.upper() + "!")


usernames = ['xiaowang', 'zhang', 'li']
greet_user(usernames)  # 调用


# a.在函数中修改列表

def print_model(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印后，将其移到列表completed_models
    :param unprinted_designs: 将打印的设计
    :param completed_models: 完成的设计
    :return: 无
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


unprinted_designs = ['iphone case', 'robot pendant']
completed_models = []
print_model(unprinted_designs, completed_models)

# b.禁止函数修改列表
print_model(unprinted_designs[:], completed_models)  # 传递列表的副本即可。


# c.传递任意数量的实参
def make_pizza(*topping):
    print(topping)
# b.禁止函数修改列表
print_model(unprinted_designs[:], completed_models)  # 传递列表的副本即可。


# c.传递任意数量的实参
def make_pizza(*topping):
    print(topping)


make_pizza('a', 'b', 'c')
make_pizza('q')

#d.结合使用位置实参和任意数量实参
def make_pizza2(size,*toppings):
    print("\nMaking a "+str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print("\n-"+topping)

make_pizza2(14,"mushrooms")


# e.使用任意数量的关键词实参
def build_profile(first, last, **user_info):
    """
    有时候预先不知道传递给函数会是什么样的信息，在这种情况下，可将函数编写成能够接受任意数量的键－值对，
    调用语句提供多少就接受多少。
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

######################################
# 9.0-导入模块

# a.导入整个模块

# 要让函数是可导入的，先创建模块，模块是以扩展名.py(pizza.py)的文件，包含要导入到程序中的代码。
# import pizza （幕后复制pizza.py的代码）

# b.导入特定的函数
# from model_name import func1,func2,func3
# from model_name import *
# c.使用as给函数指定别名
# from model_name import func1 as func_alias

# d.使用as给模块指定别名
# import model_name as model_alias

########################################
# 10.0-类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """"初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over !")


# 10.1-继承
class old_Dog(Dog):
    """生成一条老狗"""

    def __init__(self, name, age):
        super().__init__(name, age)


# 生成一个栗子
my_olddog = old_Dog('ahuang', 15)

my_olddog.sit()

# 10.2-导入类
# from  类的文件名 import class1,class2

########################################
# 11.0-文件和异常

# a-读取文本字符串，python将其中的文本都解读为字符串
# 读取整个文件
with open("pi_digits") as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
filename = 'pi_digits'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# b-读取CSV文件
import csv

filename = '/Users/zhangfangli/Documents/cmmt.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    cmmt_months = []
    for row in reader:
        cmmt_months.append(float(row[1]))

        #  print(cmmt_months)
import random

max_cmmt = []
for value in range(0, len(cmmt_months)):
    max_cmmt.append(cmmt_months[value] + 30 * random.random())

print(max_cmmt)
print(cmmt_months)
from matplotlib import pyplot as plt

fig = plt.figure(dpi=128, figsize=(6, 3))
plt.plot(cmmt_months[1:20], c='red')
plt.plot(max_cmmt[1:20], c='blue')
plt.fill_between(range(0, 19), cmmt_months[1:20], max_cmmt[1:20], alpha=0.5)
plt.title("the reviews of MT's customers about company", fontsize=10)
plt.xlabel('', fontsize=10)
plt.ylabel("months", fontsize=10)
plt.show()

# c-写入文件
filename='programming.txt'
with open(filename,"w") as file_object:
    file_object.write("hello world")
