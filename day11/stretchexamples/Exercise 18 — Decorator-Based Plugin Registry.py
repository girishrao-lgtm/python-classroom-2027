'''
Exercise 18 — Decorator-Based Plugin Registry
'''
plugins = {}

def register(name):

    def decorator(func):
        plugins[name] = func
        return func

    return decorator

@register("csv")
def export_csv(data):
    return ",".join(map(str, data))

@register("text")
def export_text(data):
    return " ".join(map(str, data))

@register("json")
def export_json(data):
    import json
    return json.dumps(data)

data = [10, 20, 30]

for name, plugin in plugins.items():
    print(name, plugin(data))