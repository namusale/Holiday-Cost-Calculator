''' This code works to calculate the total holiday cost based on destination hotel,plane and car rentals charges '''

# Information for Holiday Makers
print('---------------------------------------------------------------------------------------------------------')
print()
print( " Dear Holiday Maker, please choose the destination you are travelling to today. We have:")
print()
print('Barcelona  \t Paris  \t Florida  \t Vancouver \t Lisbon  \t Nairobi') 
print()
print('---------------------------------------------------------------------------------------------------------')
print()

#Destination list
destination_list = ['barcelona','paris','florida','vancouver','lisbon','nairobi']

# Flight destination user input
city_flight_raw = input('Please enter the city you are travelling to today. ')
city_flight = city_flight_raw.lower()

# User destination input check
city_status = False
for item in destination_list:
    if item == city_flight:
        city_status = True


# User info input for further information
if city_status == True:
    num_nights = int(input(f'How many night will you be spending in {city_flight}? '))
    rental_days = int(input('How many days will you be hiring a car? '))
else:
    print('')
    print(f' Sorry, We do not serve {city_flight} at the moment')
    print('')


# Hotel charge dictionary for different destinations
hotel_charge_dict = {'barcelona':50,'paris':90,'florida':80,'vancouver':84,'lisbon':45,'nairobi':30}

#Calculating the total hotel cost for each destination
def hotel_cost(num_nights):
    for item in hotel_charge_dict:
        if item == city_flight:
            return hotel_charge_dict[item]*num_nights

# Plane cost detailing for respective destinations
def plane_cost(city_flight):
    if  city_flight ==   'barcelona':
        flight_cost = 30
    elif   city_flight ==   'paris': 
        flight_cost = 20 
    elif   city_flight ==   'florida': 
        flight_cost = 178 
    elif city_flight == 'vancouver':
        flight_cost = 200   
    elif   city_flight ==   'lisbon': 
        flight_cost = 160 
    elif   city_flight ==   'nairobi': 
        flight_cost = 89
    return flight_cost    
    
# Car rental costs based on number of days car required
def car_rental(rental_days):
    daily_rental = 56.99
    return daily_rental * rental_days

# Total cost that the holiday for each destination
def holiday_cost(hotel_cost,plane_cost,car_rental):
    costs = hotel_cost(num_nights) + plane_cost(city_flight)+ car_rental(rental_days)
    return costs

# Printing total costs for each destination based on hotel,plane and car rentals
if(city_status == True):
    total_cost = holiday_cost(hotel_cost,plane_cost,car_rental)
    print('')
    print('')
    print('-------------------------------------Holiday Costs---------------------------------------------------------')
    print('')
    print(f'For your holiday in {city_flight}, it will  cost {total_cost }')
    print('')
    print('\t\t\t\t Details:')
    print('')
    print(f'Hotel Cost: {hotel_cost(num_nights)}\t\t Plane Cost: {plane_cost(city_flight)}\t\t Car Rentals: {car_rental(rental_days)} \t\t Total Cost: {total_cost}')
    print('-----------------------------------------------------------------------------------------------------------')