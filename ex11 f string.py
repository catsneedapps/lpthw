print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("So you're {age} old, {height} tall, and {weight} heavy.".format(age=age, height=height, weight=weight))

print("So you're {} old, {} tall, and {} heavy.".format(age,height,weight))
