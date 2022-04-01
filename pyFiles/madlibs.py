def madlibs():
  animal = input("Enter an animal: ")
  person = input("Enter a person: ")
  object = input("Enter an object: ")                                                    

  if animal <= "":
    print("Please enter an animal")
  if person <= "":
    print("Please enter a person")
  if object <= "":
    print("Please enter an object")

  print("The " + animal + " and the " + person + " went to the park in a bright blue " + object + ".")

  
