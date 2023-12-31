from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""

for item in landmark_choices.keys():
  landmark_string += (f"{item}: {landmark_choices[item]}\n")

stations_under_construction = []
#print(landmark_string)

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that landmark wasn't found.")
    start_point = get_start()

def get_end():
  end_point_letter = input("Where are you going to? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that landmark wasn't found.")
    end_point = get_end()

def set_start_and_end(start_point, end_point):
  if start_point is not None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      end_point = get_end()
    else:
      print("Unrecognised input, try again!")
      start_point, end_point = set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()

  return start_point, end_point

def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == 'y':
    print(landmark_string)

def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  if shortest_route:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    show_landmarks()
    new_route(start_point, end_point)

def get_active_stations():
  updated_metro = vc_metro
  for station_UC in stations_under_construction:
    for current_station, neighboring_stations in vc_metro.items():
      if current_station != station_UC:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([])
  return updated_metro




def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for s_station in start_stations:
    for e_station in end_stations:
      metro_system = get_active_stations() if stations_under_construction else vc_metro

      if len(stations_under_construction)>0:
        # get shortest route, but check if a route exists, using DFS!
        possible_route = dfs(metro_system, s_station, e_station)
        # check next station with a continue
        if possible_route is None:
          return None

      route = bfs(metro_system, s_station, e_station)
      if route is not None:
        routes.append(route)
  if routes:
    shortest_route = min(routes, key=len)
    return shortest_route

def goodbye():
  print("Thanks for using SkyRoute!")

#print(set_start_and_end("here", None))
#print(get_route('Marine Building', 'Granville Street'))

# item 43
stations_under_construction.append('Renfrew')
stations_under_construction.append('Rupert')
#print(get_active_stations())

skyroute()


