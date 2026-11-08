'''
Exercise 16 — Paginated API Result Generator
'''

def fetch_page(page_number):
    pages = {
        1: [101, 102, 103],
        2: [104, 105, 106],
        3: [107, 108],
        4: []
    }

    print("Fetching page:", page_number)

    return pages.get(page_number, [])


def paginated_records():
    page = 1

    while True:
        records = fetch_page(page)

        if not records:
            break

        yield from records

        page += 1


for record in paginated_records():
    print("Record:", record)