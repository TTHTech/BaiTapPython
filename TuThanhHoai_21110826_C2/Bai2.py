# 2.Viết chương trình nhập vào một chuỗi và in ra màn hình chuỗi đó dưới dạng chữ in hoa.
# Chương trình cho phép người dùng nhập nhiều lần đế khi nào người dùng nhập chữ ‘end’ thì ngưng.


mylist = []
print('Nhập "end" khi muốn dừng')
while True:
    val = input('Nhập chuỗi: ')
    if val == 'end':
        print('Kết thúc')
        break
    mylist.append(val.upper())
print(mylist)
