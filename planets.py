def weight_on_planets():
   weightEarth = raw_input("What do you weigh on earth? ")
   weightMars = weightEarth * 0.38
   weightJupiter = weightEarth * 2.34

   print "On Mars you would weigh ", weightMars, " pounds."
   print "On Jupiter you would weigh ", weightJupiter, " pounds."

if __name__ == '__main__':
   weight_on_planets()
