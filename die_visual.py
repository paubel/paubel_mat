import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []

for roll_num in range(100000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Resultatet av att kasta 1000 tärningar"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Resultat"
hist.y_title = "Frekvensen av resultatet"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')