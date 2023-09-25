#cong nghe thong tin

val = input()
ans = ""
for index in val:
    if index not in  ans:
        ans += index
print(sorted(ans))
