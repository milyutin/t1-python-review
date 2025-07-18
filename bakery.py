class Cookie:
    def __init__(self, weight, volume, name, tastiness):
        self.weight = weight
        self.volume = volume
        self.name = name
        self.tastines = tastiness  

    def __repr__(self):
        return f'{self.name} (w={self.weight}, v={self.volume}, t={self.tastines})'

def compare_cookies(a, b):
    if a.tastines != b.tastines:
        return a.tastines - b.tastines
    elif a.weight != b.weight:
        return a.weight - b.weight
    elif a.volume != b.volume:
        return a.volume - b.volume
    return (a.name > b.name) - (a.name < b.name)

def collect_cookies(bakery):
    cookies = []
    # предположим, что bakery содержит список словарей
    for c in bakery:
        cookies.append(Cookie(
            c.get("weight"), 
            c.get("volume"), 
            c.get("name"), 
            c.get("tastiness")  
        ))
    return cookies

def do_compare(old_bakery, new_bakery):
    if old_bakery is None or new_bakery is None:
        return False

    old_cookies = collect_cookies(old_bakery)
    new_cookies = collect_cookies(new_bakery)

    old_cookies.sort(key=lambda x: compare_cookies(x, Cookie(0,0,'',0))) 
    new_cookies.sort(key=lambda x: compare_cookies(x, Cookie(0,0,'',0))) 

    i = j = 0
    diff = []

    while i < len(old_cookies) or j < len(new_cookies):
        if i >= len(old_cookies):
            diff.append((new_cookies[j], 2))
            j += 1
        elif j >= len(new_cookies):
            diff.append((old_cookies[i], 1))
            i += 1
        elif compare_cookies(old_cookies[i], new_cookies[j]) < 0:
            diff.append((old_cookies[i], 1))
            i += 1
        elif compare_cookies(new_cookies[j], old_cookies[i]) < 0:
            diff.append((new_cookies[j], 2))
            j += 1
        else:
            i += 1
            j += 1

    for cookie, bakery_number in diff:
        print(f'Bakery #{bakery_number} has a different cookie "{cookie.name}" '
              f'(weight={cookie.weight}, volume={cookie.volume}, tastiness={cookie.tastines})')

    if diff:
        return False
    return True
