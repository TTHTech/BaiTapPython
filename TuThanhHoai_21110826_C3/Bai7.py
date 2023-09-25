n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []
for i in range(n):
    inp = int(input())
    arr.append(inp)
print("Sắp xếp tăng dần: ", sorted(arr))
arr.sort(reverse=True)
print("Sắp xếp giảm dần:", arr)