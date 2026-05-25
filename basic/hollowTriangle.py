'''
     *
    * *
   *   *
  *     *
 * * * * * 

'''

n = 5
for i in range(n,-1,-1):
    print(" " * i, end = "")
    for j in range(n-i):
        print("* ", end = "")

    print()



'''

    *
   * *
  * * *
 * * * *
* * * * *

'''
n = 5
for i in range(n,-1,-1):
    print(" " * i, end = "")
    for j in range(n-i):
        print("*", end = " ")

    print()


