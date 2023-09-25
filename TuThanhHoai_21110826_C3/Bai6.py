n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []
for i in range(n):
    inp = int(input())
    arr.append(inp)

cnt = 0
for inp in arr:
    if inp % 2 == 0:
        print("số chẵn là: ", + inp)
        cnt+=1
print("số lượng số chẵn: ", + cnt)