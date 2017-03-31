my_name = 'Amanda Moore'
my_height = 64.5 # inches
my_weight = 105 # pounds
my_eyes = 'hazel'
my_teeth = 'white'
my_hair = 'brown'

print("Let's talk about %s." % my_name)
print("She's %s inches tall." % my_height)
print("She's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print("Her teeth are usually %s depending on the coffee." % my_teeth)

def ceil(x):
    n = int(x)
    return n if n-1 < x <= n else n+1

print(ceil(my_height))

# This next line is supposed to be tricky!
print("If I add %r and %d I get %d." % (round(my_height), my_weight, round(my_height) + my_weight))
