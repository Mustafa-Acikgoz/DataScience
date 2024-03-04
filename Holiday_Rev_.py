def hotel_cost(num_nights):
    hotel_cost_ = int(cities[city][0] * num_nights)
    return hotel_cost_

def plane_cost(city):
    plane_cost=int(cities[city][1])
    return plane_cost
def car_rental(rental_days):
    car_rent = int(cities[city][2] * rental_days)
    return car_rent  

def holiday_cost(city, num_nights, rental_days):
    flight = plane_cost(city)
    car_rent = car_rental(rental_days)
    hotel_cost_ = hotel_cost(num_nights)
    total = flight + car_rent + hotel_cost_
    return total

loop_ = True
#"{city":[Hotel Day Rate, Flight,Car Rental Day Rate]}
cities = {"London": [100, 40, 25], "Paris": [120, 50, 45]}

print("Available cities:")
for city_ in cities.keys():
    print(city_)

city = input("Where do you want to go? ")
while loop_:
    if city in cities:
        loop_ = False
    else:
        print("Please choose a city from the list.")
        city = input("Where do you want to go? ")

num_nights = int(input("How many nights do you want to stay? "))
rental_days = int(input("How many days do you want to rent a car? "))

total = holiday_cost(city, num_nights, rental_days)
print("Total cost for your trip:", total)