import pygal
from die import Die

# Create a D6.
die_1 = Die(6)
die_2 = Die(6)

numb_times = 100000

# Make some rolls, and store results in a list.
results = []

for roll_num in range(numb_times):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Resultatet av att kasta två D"+str(die_1.num_sides)+" tärningar "+ str(numb_times) +" gånger. Multiplicerat"
hist.x_labels = [x for x in range(2, max_result+1)]
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Resultat"
hist.y_title = "Frekvensen av resultatet"

hist.add('D'+str(die_1.num_sides)+' + D'+str(die_1.num_sides), frequencies)
hist.render_to_file('dice_visual_multi.svg')