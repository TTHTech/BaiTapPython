####################
## Bài 3: perfect cube
####################
cube = 27
#cube = 8120601
for guess in range(cube+1):
   if guess**3 == cube:
       print("Cube root of", cube, "is", guess)
       # loops keeps going even after found the cube root