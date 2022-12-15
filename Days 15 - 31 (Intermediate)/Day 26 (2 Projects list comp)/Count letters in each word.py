sentence = "What is the Airspeed Velocity of a Unladen Swallow"

words = [word for word in sentence.split(' ')]
count_dict = {word:len(word) for word in words}

print(count_dict)

