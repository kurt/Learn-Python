

iterable_value = "Noodles"
iterable_obj = iter(iterable_value)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break
print("\n")
# ---------------------------
# Example 2
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x

for i in Test(20):
    print(i)
print("\n")
# ---------------------------
# Example 3
print("List Iteration")
lista = ["Time", "for", "tea"]
for i in lista:
    print(i)


 


