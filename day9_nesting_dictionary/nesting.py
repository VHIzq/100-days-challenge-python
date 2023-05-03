
""" nesting a list in a dictionary """

travel_log = {
    'France': {'cities_visited': ['Paris', 'Graccilly', 'Dijon'], 'total_visits': 12},
    'Japan': {'cities for go': ['Tokyo', 'Shibuya', 'Akihabara', 'Fuji'], 'dlls_spend': 8000},
    'Germany': ['Dusseldorf', 'Stuttgart', 'Berlin']
}

""" nesting dictionary in a list """
travel_log = [
    {'country': 'France', 'cities_visited': [
        'Paris', 'Graccilly', 'Dijon'], 'total_visits': 12},
    {'country': ' Japan', 'cities_travel': [
        'Tokyo', 'Shibuya', 'Akihabara', 'Fuji'], 'dlls_spend': 8000},
    {'country': 'Germany', 'cities_work': [
        'Dusseldorf', 'Stuttgart', 'Berlin']}
]
