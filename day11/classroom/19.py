'''
Example 19 — Function Composition and Pipelines
'''

from functools import reduce


def strip_text(text):
    return text.strip()

def lowercase(text):
    return text.lower()

def replace_spaces(text):
    return text.replace(" ", "_")

def compose(*functions):

    def composed(value):
        return reduce(
            lambda result, func: func(result),
            reversed(functions),
            value
        )

    return composed

normalize = compose(
    replace_spaces,
    lowercase,
    strip_text
)

print(normalize("  Hello Python World  "))