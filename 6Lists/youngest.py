people = [
    ('Alice', 32),
    ('Bob', 51),
    ('Carol', 15),
    ('Dylan', 5),
    ('Erin', 25),
    ('Frank', 48)
]

'''
Finish this program, so that it loops through the list of tuples, and
prints "Youngest person: Dylan, 5 years old.
Have a think about how to approach this question.
- What kind of loop do I need? A count controlled loop?
- What value do I need to save if I find a younger person?
- What should I have left after the final loop?
'''


i = 0
youngest_age = people[0][1]
# we want the if statement inside to always activate so that our youngest age will be someone inside the list
# this is why we make our youngest age a really large number
# youngest_age = 9999999999999

# we want to also save the value of youngest person so we can print it later
youngest_person = 0
while (i < len(people)):
    current_person = people[i]
    current_age = current_person[1]
    #  if our current person has a smaller age than our current youngest age
    if current_age < youngest_age:
        # we update our youngest age to be correct because the current was younger than our one
        youngest_age = current_age
        # then we save that person into this youngest person value
        youngest_person = current_person

    i += 1

name = youngest_person[0]
age = youngest_person[1]
print(f"Youngest person: {name}, {age} years old")
