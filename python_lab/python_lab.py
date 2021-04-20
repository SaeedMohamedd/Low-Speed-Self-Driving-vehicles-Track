# Q1.
'''
try:
    from datetime import date
    age=int(input("enter your birthday year"))
    todays_date = date.today() 
    print("you are {} years old".format(todays_date.year -age))
except:
    print("invalid value,error")

    '''
#Q2

'''
try:
   
    trys =int(input("enter your number of tries"))
    sumition=0
    print(trys)
    for s in range(trys+1):
        sumition += s
    avr =sumition / trys
    print("the summof nature number from 1 to 50 = {}".format(sumition))
    print("Average of natural Number from 1 to 50= {}".format(avr))  

except:
    print("invalid value,error")

'''

#Q3.
'''
try:
    rows =int(input("enter pyramid high"))
    k=0
    for i in range(1,rows+1):
        for j in range(1,(rows-i)+1):
            print(end=" ")
        
        while k!=(2*i-1):
          print("*",end ="")
          k+=1

        k=0
        print()
        
except:
    print("invalid value,error")
'''

#Q4.
'''
try:
    num =int(input("enter num to check "))

    if num % 2 == 0 :
         print("{} is an even number ".format(num))
    else:
        print("{} is an odd number ".format(num))  
        
except:
    print("invalid value,error")
    
'''

#Q5.

'''
try:
    s =input("enter string  to remove vowels from it : ")
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for x in s.lower() :
        if x in vowels:
            s = s.replace(x, "")

    print("string with out vowels : {}".format(s))
        
except:
    print("invalid value,error")
    
'''

#Q6.
'''
try:
    l=['asa','dfsf','dsfdfs']
    File=open('test.txt','w')
    for e in l :
        File.write(e)
    File.close()
            

except:
     print("invalid value,error")

'''

#Q7.
'''
try:

    def sum_func(list):
        summ=0
        for x in list:
          summ+=x
        return summ
    l=[3,5,2]
    print(sum_func(l))    

except:
    print("invalid value,error")

'''

#Q8.
'''
try:

    def even_func(list):
        summ=[]
        for x in list:
          if(x%2==0):
             summ.append(x)
        print(summ)
    l=[3,5,2]
    even_func(l)  

except:
    print("invalid value,error")

'''
#Q9.
'''
try:
    class G_String:
        def __init__(self,strr):
            self.strr =''

        def get_string(self,s):
            self.strr=s

        def print_string(self):
            print(self.strr.upper())
            
    g=G_String("init from constructor")
    g.get_string("from_get")
    g.print_string()
except:
    print("invalid value,error")

'''
#Q10.
'''
try:
    class G_Speed_D_D:

        def __init__(self,distance,time):
            self.distance = distance
            self.time = time 

        def calc_speed(self,distance,time):
            
             return distance / time
            

        def calc_duration(self,speed,distance):
            return  distance / speed

    g=G_Speed_D_D(30,1)
    print("the speed is: {}  ".format(g.calc_speed(30,2)))
    print("the duration is: {}".format(g.calc_duration(60,120)))       
    
    
except:
    print("invalid value,error")
'''

#Q11.
'''
try:
    import numpy as np
    x =  np.arange(2, 11).reshape(3,3)
    print(x)

except:
     print("invalid value,error")

'''
#Q12.

'''
try:

    import numpy as np
    x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
    print("Original array:")
    print(x)
    print("Replace the negative values of the said array with 0:")
    x[x < 0] = 0
    print(x)
except:
    print("invalid value,error")

'''

#Q13.

'''
try:

    import numpy as np
    nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
    print("Original array:")
    print(nums)
    print("\nAfter partitioning on 4 the position:")
    print(np.partition(nums, 4))
except:
    print("invalid value,error")

'''

#Q14

'''
max_num=-1
min_num=None
num=0
while True:
    
    strr=input()
    if strr=='done':
        break
    try:
        num=int(strr)
    except:
        print("invalid input")
        continue
    if min_num is None:
        min_num = num 
    elif num < min_num :
        min_num=num
    elif num > max_num :
        max_num =num

print("max num id {}".format(max_num))
print("min nuber is {}".format(min_num))

'''

#Q15.

'''
try:

    file_name=input("enter file name  ")
    file=open(file_name,'r')
    for i in file:
      line=file.readline()
      print(line.upper())

except:
    print("invalid")

'''


#Q16.
'''
try:
    read_file = open("mbox-short.txt","r")
    count = 0
    for line in read_file:
        line = line.rstrip()
        if line == "": 
            continue
            
        words = line.split()
        if words[0] !="From": 
            continue
            
        print(words[1])
        count = count+1

    print ("there were", count, "lines in the file with From as the first word")     

except:
       print("invalid") 
       
'''


#Q17.

import time

# starting time
start = time.time()

# program body starts
for i in range(10):
    print(i)

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")