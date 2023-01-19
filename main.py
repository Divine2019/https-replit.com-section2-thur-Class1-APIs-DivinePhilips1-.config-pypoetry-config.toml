from api import get_flights_response

dept_city_code = "IST"
arr_city_code = "LOS"

#get flights from dept city to arr city
response = get_flights_response(dept_city_code, arr_city_code)
print(response)
