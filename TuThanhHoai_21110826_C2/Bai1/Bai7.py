####################
## Bài 7: for loops
####################
for n in range(5):
   print(n)
# in số từ 0--> 4
mysum = 0
for i in range(10):
   mysum += i
print(mysum)
# cộng số từ 0-->9
mysum = 0
for i in range(7, 10):
   mysum += i
print(mysum)
# cộng số từ i = 7 đến 10 tương đương các số 7 8 9
mysum = 0
for i in range(5, 11, 2):
   mysum += i
   if mysum == 5:
       break
       mysum += 1
print(mysum)
# nếu bằng 5 chương trình in ra và kết thúc