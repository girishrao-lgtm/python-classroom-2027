'''
Classroom 10 — Case conversion and normalization
Concept: lower(), upper(), casefold(), and stripping whitespace.
'''
text = "  Python Deep Dive  "

print(f"Original = [{text}]")
print(f"Lower = [{text.lower()}]")
print(f"Upper = [{text.upper()}]")
print(f"Title = [{text.title()}]")
print(f"Strip = [{text.strip()}]")
print(f"Left strip = [{text.lstrip()}]")
print(f"Right strip = [{text.rstrip()}]")

a = "Straße"
b = "STRASSE"

print(a.lower() == b.lower())
print(a.casefold() == b.casefold())