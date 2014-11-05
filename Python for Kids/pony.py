class pony:
    name = "Princess Celestia"
    def walk(self):
        print("See?  I am walking. -says " + self.name)


p = pony()
print(p.name)
p.walk()
t = p
t.name = "Derpy"
print(p.name)
p.walk()
