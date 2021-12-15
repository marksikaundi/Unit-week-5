def subroutine( n ):
    while n > 0:
        print (n,)
        n = n - 1

n = 2
n = n + 5
print(n)

##############################

bruce = 5
print (bruce,)
bruce = 7
print (bruce)

#####################

n = 10
while n != 1:
    print (n,)
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1

#############################
    n = 10000
count = 0
while n:
    count = count + 1
    n = n // 10
print (count)

##################################
def subroutine( n ):
    while n > 0:
        print (n,)
        n = n - 1