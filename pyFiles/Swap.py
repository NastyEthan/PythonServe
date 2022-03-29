def entry(age1,age2):    
    print(age1, age2) # pre-swap
    age1, age2 = age2, age1
    # print(age1, age2) # post-swap
    return age1, age2

def swap():
  age1 = int(input("select a number for age1:"))
  age2 = int(input("select a number for age2:")) 
  x,y=entry(age1,age2)
  print(x,y)

