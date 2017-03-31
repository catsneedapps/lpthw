types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

bad_joke = x + y

print(bad_joke)


print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

z = f"Do you think the joke is funny? {hilarious}"
print(z)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
