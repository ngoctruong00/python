# cac kieu du lieu - data type
# int : 1,2,2...
# float: 1.2,2.3,...
# string: "dao ngoc truong",....
# bool: true,false

# INPUT: nhập 1 chuỗi vào
# input_name = input("nhap ten cua ban")
# print(" ten cua ban la:", input_name)

# các phép toán cở bản: +,-,*,/,chia lấy dư %

# Conditional Operations toán tử điều kiện cơ bản
# ==;!=;>=;<=;<;>
# print(ord(a)) in mã asciII 

# if/else/elif
name = input("name: ")
if name == " thanh ":
    print(" thanh ")
else: 
    print(" khong ") 
    

# list/tuples
list_test = ["Thanh", 3261, True]
print(len(list_test)) # in độ dài của mảng
# append() thêm 1 phần từ vào cuối mảng
# clear() xóa tất cả các phần từ trong mảng
# copy() sao chép 1 mảng
# count() trả về số phần tử có giá trị chỉ định
# extend() thêm nhiểu phần từ và mảng vào cuối mảng hiện tại
# pop() xóa phần từ
#  tuple là 1 dạng kiểu list nhưng không thể thêm hay xóa phần từ
# có thể thêm list trong list
x = list_test[:] # [:] để không tham chiếu với list_test 


# for loop and while loop
for i in range(2,10,2): # loop từ 2 đến 10 với khoảng cách là 2
    print(i)
#  while
i = 0
while i < 10:
    print(i)
    i += 1


# set kiểu dữ liệu giống với list
s = set((1,2,3,4,4))
# 1 số kiểu set methođs được tích hợp sẵn
# s.add(3) thêm phần tử 3 và set
# s.difference(a) tìm phần từ khác nhau giữa s và a
# 1 số chức năng khác như là copy(),discard(),...
print(0 in s) # xem 0 có trong set hay không có true không false
 
 
# kiểu dữ liệu dictionary 
a = {} # dict có 2 giá trị key : value
a = {'key': 1}
a[2]  = 8
del x['key'] # xóa key tên key trong set
for key, value in a.items():
    print(key, value)



# function
def func():
    print("adb") #function in adb
func()

def funcc(x, y):
    return x  + y; x*y;
print(funcc(9,7)[0]) # in ra giá trị x+y 
res1, res2 = funcc(9,7) # in ra giá trị res1 = x + y và res2 = x*y


#  tham số mặc định và tham số bắt buộc
def func(x, y, z):
    print(x,y,z)
# nếu def func(z,y,z) thì z ở đây là tham số bắt buộc
# nếu def func(z,y,z= none) thì z ở đây là tham số mặc định
# positional arguments
func(1, 6, 9) # theo thứ tự đã khai
# keyword arguments
func(y = 8; z = 10; x = " hello ") # không cần theo thứ tự truyền vào
# *args// list tham số
def fun(x, y, *args): 
    print(x, y)
    for x in args:
        print(x)
fun(1,2, 88, "thanh", "hello", True) # đây không phải là tham số bắt buộc
# **kwarg
def fun(x, y, *args): 
    print(x, y)
    for x in args:
        print(x)
fun(1,2, 88, "thanh", "hello", True)



#List Comprehension(bao quát về list): giúp lấy ra 1list phần tử mong muốn
#new_list[<action> for <item> in <iterator> if <some condition>]
hello = "Hello World"
# dùng for
for x in hello:
    print(x)
    
# dùng list
print(char for char in hello)
print(number for number in range(0,10) if number % 2 == 1)
list_price = [100,120,200,300]
VAT = 0.08
def price_product(price):
    return price*(1+VAT)
print([price_product(price) for price in list_price])


#lamda : small(one line) anonymous function - ham an danh
#lambda arguments: expresion
test_lambda = lambda x : x + 48
print(test_lambda(69))
list_sample = [-1,-5,-6,7,0,2,3,4,1]
print(sorted(list_sample)) #in ra sort từ lớn đến bé
print(sorted(list_sample,key = lambda x : abs(x))) #in ra sort tri tuyet doi
list_coordidate = [(0,4),(-5,7),(7,10),(1,5)]
print(sorted(list_coordidate)) #in ra sorted theo phan tu dau tien
print(sorted(list_coordidate, key = lambda x : x[1]))



#map (func,object): transform object with function
list_temp  = [7,8,9,12]
def sum(x):
    return x + 2
print(list(map(sum,list_temp))) #in ra mang da duoc coong

print(list(map(lambda x : x * 2,list_temp)))


# filter (func,object): filter object with function

print(list(filter(lambda x : x % 2 == 1,list_temp)))
list1 = [x for x in list_temp if x % 2 == 1]
print(list1)

#reduce(func,object): return single value,, func get 2 arg
from functools import reduce
print((reduce(lambda x,y : x if x < y else y),list_temp)) # so sanh fan tu cuar mang in ra gias tri nho nhat


# string