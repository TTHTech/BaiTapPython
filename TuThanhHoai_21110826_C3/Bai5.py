x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

ans = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i*j)
    ans.append(row)

for row in ans:
    print(row)