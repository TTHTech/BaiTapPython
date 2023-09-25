s = input()
ans = 0
cnt = 0
for index in s:
    if index.isupper():
        ans = ans + 1
    else:
        cnt = cnt + 1
print("số chữ hoa:", ans)
print("số chữ thường", cnt)
