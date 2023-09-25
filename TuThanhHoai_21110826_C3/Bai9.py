from operator import itemgetter

n = int(input("Nhập số lượng tuple:"))
data = []
for i in range(n):
    name = input(f"Nhập tên {i+1}: ")
    age = int(input(f"Nhập tuổi {i+1}: "))
    score = float(input(f"Nhập điểm {i+1}: "))
    data.append((name,age,score))
sorted_data = sorted(data , key = itemgetter(0,1,2))
for item in sorted_data:
    print("Tên: " + item[0] + ", Tuổi: " + str(item[1]) + ", Điểm: " + str(item[2]))