class Factorial():
  def __init__(self):
      self.fac = 1 # sets 1 as start
  def __call__(self, n):
      if n < self.fac:
          return self.fac
      else:
        sol = n * self(n - 1) # factorial part
      return sol

def factors():
  num = int(input("Enter a number to factor: "))
  print('The factors of', num, 'are:')
  for i in range(1, num+1):
      if(num % i) == 0:
          print(i, end=' ')
  print()

class factors2():
  def __init__(self):
    print("1", end=" ") # 1 will always be a factor
  def __call__(self, n):
    for i in range(2,n + 1): # Check for factors after 1
      if n % i == 0:
        print(i, end=" ")
    print()
          

def ftester():
  # Create instance of factorial object
  fac = Factorial()
  try:
    x = int(input("Enter number to take factorial of "))
    print(fac(x))
  except:
    print("Something went wrong")

def testerfOOP():
  try:
    x = int(input("Enter a number to factor: "))
    fO = factors2()
    print(fO(x))
  except:
    print("Something went wrong")
