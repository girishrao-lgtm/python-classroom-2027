'''
Exercise 13 — Custom Collection with Iteration Support
'''
class StudentCollection:

    def __init__(self):
        self._students = []

    def add(self, student):
        self._students.append(student)

    def __len__(self):
        return len(self._students)

    def __getitem__(self, index):
        return self._students[index]

    def __contains__(self, student):
        return student in self._students


collection = StudentCollection()

collection.add("Alice")
collection.add("Bob")
collection.add("Charlie")

print(len(collection))
print(collection[0])
print("Bob" in collection)

for student in collection:
    print(student)