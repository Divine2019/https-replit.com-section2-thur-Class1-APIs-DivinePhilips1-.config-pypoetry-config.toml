import requests

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiNzFjOThhMjUxNDFiZTY0MmQzODFlOTBjNWZjZTc0NWEwNGUxNzJkZjM5N2EzZmYyZTYyYWFiZjJhZmEyOGFlMGI0NTY5NmU1ZmRhZmE1ZGYiLCJpYXQiOjE2NzM1NDQzNTksIm5iZiI6MTY3MzU0NDM1OSwiZXhwIjoxNzA1MDgwMzU5LCJzdWIiOiIxOTU5NyIsInNjb3BlcyI6W119.k7tW7FEwtt6jwGxYqVCkr8J3fjUB1X1rCa7ZDwAkwBVCox0oNTk1TWtKklgy2QlSOkorzpZ9jpc4J5Tdwne1nQ" #https://www.goflightlabs.com/

URL = "https://app.goflightlabs.com/routes?access_key=" + API_KEY


def get_flights_response(dept, arr):
  """
  Make an API Call to get the flights from dest to arr
  Arguments:
      dept: a string : the departure city code e.g. IST
      arr: a string : the destination city code e.g. LOS
  Returns:
      True of False
  """
  url = f"{URL}&departureIata={dept}&arrivalIata={arr}&departureDate=2023-01-13"

  #====YOUR CODE HERE #######
  request = requests.get(url)
  requ_json = request.json()
  ##########################
  a = type(requ_json)
  print(a)
  return requ_json
  


def get_flights(dest, arr):
  """
  Make an API Call to get the flights from dest to arr
  Arguments:
      dept: a string : the departure city code e.g. IST
      arr: a string : the destination city code e.g. LOS
  Returns:
      List of flight information
  """

  url = f"{URL}&departureIata{dest}&arrivalIata{arr}&departureDate=2023-01-13"

  #====YOUR CODE HERE #######
  request = requests.get(url)
  requ_json = request.json()
  ##########################
  a = type(requ_json)
  print(a)
  