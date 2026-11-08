'''
Exercise 17 — Generate All Subsets
'''

def generate_subsets(numbers):
    result = []
    current = []

    def backtrack(index):
        if index == len(numbers):
            result.append(current.copy())
            return

        backtrack(index + 1)

        current.append(numbers[index])
        backtrack(index + 1)
        current.pop()

    backtrack(0)

    return result


numbers = [1, 2, 3]

for subset in generate_subsets(numbers):
    print(subset)