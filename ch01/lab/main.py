import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", "$", cost_per_week, type(cost_per_week))

classes_per_week = 3
cost_per_class = cost_per_week / classes_per_week
var = cost_per_class
print("Cost per class:", "$", cost_per_class, type(cost_per_class))

#Part B
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
var = Months
print(random.choice(Months))
print("The number of weeks: 16", type(weeks))
print("The number of classes: 5", type(classes))
print("The tuition: $6000", type(tuition))