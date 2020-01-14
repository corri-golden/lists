planet_list = ["Mercury", "Mars"]
#mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto
#apprend
planet_list.append("Jupiter")
planet_list.append("Saturn")




#extend
planet_list2 = ["Jupiter", "Saturn"]
planet_list.extend(planet_list2)
#or
planet_list.extend(["Jupiter", "Saturn"])



#insert
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.insert(10, "Pluto")



#slice
rocky_planets = planet_list[0:4]


#remove
planet_list.remove("Pluto")
print(planet_list)













# del planet_list[6]
# print(planet_list)