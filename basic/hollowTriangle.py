'''
     *
    * *
   *   *
  *     *
 * * * * * 

'''

n = 5
for i in range(1,n+1):
    for j in range(0,i*2):
        print(" ", end = "")
        for k in range(0,i*2-1):
            print("*", end = "")
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


