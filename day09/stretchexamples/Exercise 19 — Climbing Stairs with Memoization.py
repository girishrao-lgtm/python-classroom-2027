'''
Exercise 19 — Climbing Stairs with Memoization
'''
def climb_stairs(n):
    memo = {}

    def solve(steps):
        if steps <= 1:
            return 1

        if steps in memo:
            return memo[steps]

        memo[steps] = solve(steps - 1) + solve(steps - 2)

        return memo[steps]

    return solve(n)


for n in [2, 3, 5, 10, 20]:
    print(n, climb_stairs(n))

    