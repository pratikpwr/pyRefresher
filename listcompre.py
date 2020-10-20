# list comprehension

numbers = [1, 2, 3]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)

# this can be done in one line using list comprehension

nums = [1, 2, 3]
doubs = [num * 2 for num in nums]

print(doubs)

# if in list compre

friends = ['Rolf', 'Sam', 'Samantha', 'Sagar', 'Rick']
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

# list

friend2 = ['Rolf', 'Sam', 'Samantha', 'Sagar', 'Rick']
ss = [friend for friend in friend2 if friend.startswith('S')]

print(ss)
