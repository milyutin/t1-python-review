def res():
    data = [
        {"name": "Hotel A", "stars": 4, "rooms": [{"capacity": 2}, {"capacity": 3}]},
        {"name": "Hostel B", "stars": 2, "rooms": [{"capacity": 1}, {"capacity": 1}, {"capacity": 2}]},
        {"name": "Apart C", "stars": 3, "rooms": []},
        {"name": "Hotel D", "stars": 5, "rooms": [{"capacity": 4}, {"capacity": 1}]}
    ]

    result = {
        hotel["name"]: sum(
            room["capacity"]
            for room in hotel["rooms"]
            if room["capacity"] > 1
        )
        for hotel in data
        if hotel["stars"] >= 3 and hotel["rooms"]
    }
