def veggies_and_dips(veg_count, dip_count):
    print(f"You have {veg_count} varieties of veggies!")
    print(f"You have {dip_count} delicious dips!")
    print("Man, that's enough for a party!\n")

print("We can just give the function numbers directly:")
veggies_and_dips(20,15)

print("Or, we can use variables from our script:")
num_of_veggies = 10
num_of_dips = 5

veggies_and_dips(num_of_veggies,num_of_dips)

print("We can even do math inside too:")
veggies_and_dips(4 + 3, 5 % 3)

print("And we can combine the two, variables and math:")
veggies_and_dips(num_of_veggies + 50, num_of_dips + 100)
