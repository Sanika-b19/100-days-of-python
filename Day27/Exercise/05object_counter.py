# Exercise 5: Track Object Count Using Class Methods

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print(f"Number of instances created: {Counter.get_count()}")  # Output: Number of instances created: 3
