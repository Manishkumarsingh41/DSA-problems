class MyHashSet:

    def __init__(self):
        # bool array banaya
        self.set = [False] * 1000001

    def add(self, key):
        # key ko add kiya
        self.set[key] = True

    def remove(self, key):
        # key ko remove kiya
        self.set[key] = False

    def contains(self, key):
        # key check kiya
        return self.set[key]
