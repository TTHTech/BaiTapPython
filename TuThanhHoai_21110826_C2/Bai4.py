

s = input()
ans = 0
cnt = 0
for index in s:
    if index.isalpha():
        ans = ans + 1
    else:
        cnt = cnt + 1
print("số ký tự", ans)
print("ký tự số", cnt)
