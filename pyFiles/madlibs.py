def madlibs():
  animal = input("Enter an animal: ")
  person = input("Enter a person: ")
  vehicle = input("Enter a vehicle: ")                                                    

  if animal <= "":
    print("Please enter an animal")
  if person <= "":
    print("Please enter a person")
  if vehicle <= "":
    print("Please enter a vehicle")

  print("The " + animal + " and the " + person + " went to the park in a bright blue " + vehicle + ".")

  
