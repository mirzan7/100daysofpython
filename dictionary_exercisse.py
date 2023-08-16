    
travel_log = [
    {
        "country":"france",
        "visits" : 12,
        "cities" : ["paris","lille","dijon"]
    },
    {
        "country":"germany",
        "visits":5,
        "cities":["berlin","hamburg","stittgart"]
    }
] 
def add_new_country(name,visit,cities_visited):
    new_travel_log = {
        "country":name,
        "visits":visit,
        "cities":cities_visited
    }
    travel_log.append(new_travel_log)

add_new_country("russia",2,["moscow","saint peres","namougrgiv"])
print(travel_log)