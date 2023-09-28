import pandas as pd

def toFloat(x):
  try:
      return float(x)
  except:
      return None

def read_fromDB(connIn):
    population = pd.read_sql("SELECT * FROM population", con=connIn)
    region = pd.read_sql("SELECT * FROM region", con=connIn)
    travel_mode = pd.read_sql("SELECT * FROM travel_mode", con=connIn)
    travel_motives = pd.read_sql("SELECT * FROM travel_motives", con=connIn)

    #clean trips
    trips = pd.read_sql("SELECT * FROM trips", con=connIn)
    trips = trips.drop(trips.columns[[0]], axis=1)
    trips['Periods'] = trips['Periods'].str.slice(stop=4)

    urbanization_level = pd.read_sql("SELECT * FROM urbanization_level", con=connIn)
    urbanization_level = urbanization_level.drop(urbanization_level.columns[[0]], axis=1)

    #merge data
    region_ul = pd.merge(region, urbanization_level, how="left", left_on='region', right_on='provinces')
    trips_denorm = pd.merge(trips, travel_mode, how="left", left_on='TravelModes', right_on='code')
    trips_denorm = pd.merge(trips_denorm, travel_motives, how="left", left_on='TravelMotives', right_on='code',
                            suffixes=('', '_travel_motives'))
    trips_denorm = pd.merge(trips_denorm, region_ul, how="left", left_on='RegionCharacteristics', right_on='code',
                            suffixes=('', '_region'))
    trips_denorm = pd.merge(trips_denorm, population, how="left", left_on='Population', right_on='code',
                            suffixes=('', '_population'))

    #change data types
    trips_denorm['Trip in a year'] = trips_denorm['Trip in a year'].apply(toFloat)
    trips_denorm['Km travelled in a year'] = trips_denorm['Km travelled in a year'].apply(toFloat)
    trips_denorm['Hours travelled in a year'] = trips_denorm['Hours travelled in a year'].apply(toFloat)

    print(trips_denorm.shape)
    return trips_denorm

