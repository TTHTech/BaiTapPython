list = []
a,b = 0 ,1
n = int(input("Nhập số phần tử Fibonacci: "))
for i in range(n + 1):
    list.append(a)
    a,b = b, a+b
print("Dãy Fibonacci:", ', '.join(map(str, list)))