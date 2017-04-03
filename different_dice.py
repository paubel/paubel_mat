from die import Die

import pygal

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []

for roll_num in range(500000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Resultatet av att kasta en D6 tärning och en D10 tärning 50 000 gånger"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Resultat"
hist.y_title = "Frekvensen av resultatet"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_D10_D6.svg')