'''
Stretch 20 — Minimum Window Containing All Required Characters
A security scanner receives a long string and a set of required characters. Find the shortest contiguous substring containing every required character with its required frequency.

Example: ADOBECODEBANC with pattern ABC produces BANC.
'''

text = input("Enter text: ")
pattern = input("Enter required pattern: ")

if not pattern:
    print("Pattern cannot be empty")

else:
    required = {}

    for ch in pattern:
        required[ch] = required.get(ch, 0) + 1

    window = {}

    formed = 0
    required_types = len(required)

    left = 0

    best_length = float("inf")
    best_start = 0

    for right in range(len(text)):

        ch = text[right]

        window[ch] = window.get(ch, 0) + 1

        if ch in required and window[ch] == required[ch]:
            formed += 1

        while formed == required_types:

            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_start = left

            left_char = text[left]
            window[left_char] -= 1

            if left_char in required:  # noqa: SIM102
                if window[left_char] < required[left_char]:
                    formed -= 1

            left += 1

    if best_length == float("inf"):
        print("No valid window found")

    else:
        answer = text[best_start:best_start + best_length]

        print(f"Minimum window = {answer}")
        print(f"Window length = {best_length}")