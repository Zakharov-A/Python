# def route_info(route):
#     if ('distance' in route) and (type(route['distance']) == int):
#         return f"Distance to your destintion is {route['distance']}"
    
#     if ('speed' in route) and ('time' in route):
#         return f"Distance to your destination is {route['speed'] * route['time']}"

#     return "No distance info is available"




# print(route_info({'distance': 15}))    

# print(route_info({'speed': 20, 'time': 3}))

# print(route_info({'name': 'red', 'height': 40}))

# ----

def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        route_info =  f"Distance to your destintion is {route['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info = f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        route_info = "No distance info is available"
    return route_info



print(route_info({'distance': 15}))    

print(route_info({'speed': 20, 'time': 3}))

print(route_info({'name': 'red', 'height': 40}))