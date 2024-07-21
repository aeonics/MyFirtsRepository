"""The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

   Asks the user what their Earth weight is (as a float).
   Asks the user for a planet number (as an int).

Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:
destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14

If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'."""

weight_earth=float(input("¿Cual es tu peso en la tierra?: "))
planet=int(input("¿Que planeta escoges? 1 -7: "))
destination_weight = 0

if planet == 1:
  destination_weight=weight_earth * 0.38
  print("Tu peso en Mercurio seria: ",destination_weight)
elif planet == 2:
  destination_weight=weight_earth * 0.91
  print("Tu peso en Venus seria: ",destination_weight)
elif planet == 3:
  destination_weight=weight_earth * 0.38
  print("Tu peso en Marte seria: ",destination_weight)
elif planet == 4:
  destination_weight=weight_earth * 2.53
  print("Tu peso en Jupiter seria: ",destination_weight)
elif planet == 5:
  destination_weight=weight_earth * 1.07
  print("Tu peso en Saturno seria: ",destination_weight)
elif planet == 6:
  destination_weight=weight_earth * 0.89
  print("Tu peso en Urano seria: ",destination_weight)
elif planet == 7:
  destination_weight=weight_earth * 1.14
  print("Tu peso en Neptuno seria: ",destination_weight)
else:
  print("Invalid planet number")