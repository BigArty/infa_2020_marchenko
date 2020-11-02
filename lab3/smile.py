class NPC:
    a = 10

    def __init__(self, behavior=0):
        self.behavior = behavior

    def smile(self):
        self.behavior = 10

    def ping(self):
        self.behavior -= 1

    def bark(self, times):
        for _ in range(times):
            print("Bark!")


wolf = NPC(5)
wolf2 = NPC(5)
print(wolf.a)
NPC.a -= 1
print(wolf2.a)
print(wolf.a)
print(type(NPC.ping))
