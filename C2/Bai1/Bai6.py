####################
## Bài 6: while loops
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that.
## Hint: use a counter
###################
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
   n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")

n = 0
while n < 5:
   print(n)
   n = n+1

#  nếu nhập right or Right sẽ in ra ký tự đặc biệt và còn lại sẽ in ra 0-->4