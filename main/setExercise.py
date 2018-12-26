s1 = set((1, 2, 3, 2))
print(s1)
s2 = set({1: "good", 2: "bad"})
print(s2)
s1.add((1, 2))
print(s1)
s1.update({4: "good", 5: "bad"})
s1.update("bad")
print(s1)

s3 = set((1, 2, 3))
s4 = set((1, 2, 4))
a1 = s3 & s4
print(a1)