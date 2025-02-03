""" 
square  pattern
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * *  
* * * * * *  
"""

# for i in range(0,6):
#     for j in range(0,6):
#         print('*',end=' ')
#     print()
    
"""
square hallow pattern  
* * * * * * 
*         *
*         *
*         *
*         *
* * * * * *
"""
# for i in range(0,6):
#     for j in range(0,6):
#         if i==0 or  i==5 or j==0 or j==5:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
Right half-pyramid
* 
* *
* * *
* * * *
* * * * *
'''
# input=int(input("enter number:"))
# for i in range(1,input):
#     for j in range(0,i):
#         print('*',end=' ')
#     print()
    


'''
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end=' ')
#     print()


'''
reverse right half pyramis
* * * * * 
* * * * 
* * * 
* * 
* 
'''
# for i in range(1,6):
#     for j in range(i,6):
#         print('*',end=' ')
#     print()
    
#2nd approach
# for i in range(1,6):
#     for j in range(0,6):
#         if j<=5-i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

    
  
'''
left half pyramid
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * *
'''  
# for i in range(0,6):
#     for j in range(0,6):
#         if i>=5-j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
reverse left-half pyramid
* * * * * * 
  * * * * *
    * * * *
      * * *
        * *
          *
'''
# for i in range(0,6):
#     for j in range(0,6):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


'''  
k pattern
* * * * * 
* * * *
* * *
* *
*
* *
* * *
* * * *
* * * * *
'''

# for i in range(1,6):
#     for j in range(i,6):
#         print('*',end=' ')
#     print()
# for i in range(2,6):
#     for j in range(0,i):
#         print('*',end=' ')
#     print()

'''
* * * * * * 
  * * * * *
    * * * *
      * * *
        * *
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
'''
# for i in range(0,6):
#     for j in range(0,6):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# for i in range(1,6):
#     for j in range(0,6):
#         if i>=5-j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



for i in range(0,6):
    for j in range(0,i+1):
        print('*',end=' ')
    print()
for i in range(1,6):
    for j in range(i,6):
        print('*',end=' ')
    print()



