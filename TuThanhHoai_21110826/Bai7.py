n = float(input())
tongtien = 0
if 0 < n <= 50:
    tongtien = n * 1670
elif 51 <= n <= 100:
    tongtien = (n - 50) * 1734 + 50 * 1670
elif 101 <= n <= 200:
    tongtien = (n - 100) * 2014 + 50 * 1670 + 50 * 1734
elif 201 <= n <= 300:
    tongtien = (n - 200) * 2536 + 50 * 1670 + 50 * 1734 + 100 * 2014
elif 301 <= n <= 400:
    tongtien = (n - 300) * 2834 + 50 * 1670 + 50 * 1734 + 100 * 2014 + 100 * 2536
else:
    tongtien = (n - 400) * 2927 + 50 * 1670 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834

print("Số tiền điện cần thanh toán:", tongtien)
