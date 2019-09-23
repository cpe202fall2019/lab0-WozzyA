def weight_on_planets():
   userInput = input("What do you weigh on earth? ")

   weightEarth = float(userInput)
   weightMars = weightEarth * 0.38
   weightJupiter = weightEarth * 2.34

   print("\nOn Mars you would weigh", weightMars, "pounds.\nOn Jupiter you would weigh", weightJupiter, "pounds.")

if __name__ == '__main__':
   weight_on_planets()
