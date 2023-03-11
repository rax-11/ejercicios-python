lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kenny", "yoshi", "Andre", "Nico", "Eri"]
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(3, "Kelly")
print(friends)

friends.remove("Andre")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kenny"))

print(friends.index("Eri"))

print(friends.count("yoshi"))

friends.remove(4)
print(friends)
friends.remove(8)
print(friends)
friends.remove(15)
print(friends)
friends.remove(16)
print(friends)
friends.remove(23)
print(friends)
friends.remove(42)
print(friends)

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)


friends.clear()
print(friends)

