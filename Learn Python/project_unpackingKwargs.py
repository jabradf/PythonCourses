from nile import get_distance, format_price, SHIPPING_PRICES
from quiz_test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)

#result = calculate_shipping_cost([1,2], [3,4])
#print(result)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = distance / driver.speed
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None:
      #print("none, setting to", driver)
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      #print("found cheaper driver")
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  #print("driver type:",type(driver))
  #print("cheapest driver type:",type(cheapest_driver))
  return cheapest_driver_price, cheapest_driver 




# Test the function by calling 
'''class Driver:
  def __init__(self, speed, salary):
    self.speed = speed
    self.salary = salary
driver1 = Driver(4, 10)
driver2 = Driver(7, 20)
calculate_driver_cost(20, driver1, driver2)'''
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
  total_money_made = 0
  for trip in trips.values():
    trip_revenue = trip.cost - trip.driver.cost
    print(trip_revenue)
    total_money_made += trip_revenue
  return total_money_made


# Test the function by calling 
test_function(calculate_money_made)
