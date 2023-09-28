from trips_processor.data_processing import manipulate_data as md


def question1(connIn,denormData=None):
    print("Show the total number of trips for people who went to grocery grouped by travel method and level of urbanization across all the years")
    if(denormData is None):
        trips_denorm=md.read_fromDB(connIn)
    else:
        trips_denorm=denormData

    trips_denorm_grossery = trips_denorm[trips_denorm['motive'] == 'Shopping, groceries, funshopping.']
    res = trips_denorm_grossery.groupby(['Periods', 'mode', 'level_urbanization'])['Trip in a year'].sum().reset_index()
    print(res.to_string())
    return res


def question2(connIn,denormData=None):
    print("Show the users in west Netherlands who travelled the most by bike (in terms of kms) to go to work.")
    if(denormData is None):
        trips_denorm=md.read_fromDB(connIn)
    else:
        trips_denorm=denormData

    trips_wn = trips_denorm[trips_denorm['area'] == "West-Nederland (LD)"]
    trips_wn = trips_wn.groupby(['UserId', 'mode', 'motive'])['Km travelled in a year'] \
        .sum().reset_index(name="Tot_Km") \
        .sort_values(['UserId', 'mode', 'Tot_Km'], ascending=False)

    # print(trips_wn.to_string())

    trips_wn = trips_wn.groupby('UserId').first()
    trips_wn = trips_wn[
        (trips_wn['mode'] == "Bike") & (trips_wn['motive'] == "Travel to/from work, (non)-daily commute")]

    print(trips_wn.to_string())
    return trips_wn




def question3(connIn,denormData=None):
    print("Taking the top 8 users above 35 years old who travel the most km by bike, show the 3 least common motives of travel in year 2022")
    if(denormData is None):
        trips_denorm=md.read_fromDB(connIn)
    else:
        trips_denorm=denormData

    trips_sr = trips_denorm[trips_denorm['population'] == "Population: 36 years old or older"]

    trips_sr = trips_sr.groupby(['UserId', 'mode'])['Km travelled in a year'] \
        .sum().reset_index(name="Tot_Km") \
        .sort_values(['UserId', 'mode', 'Tot_Km'], ascending=False)

    # print(trips_sr.to_string())

    trips_sr = trips_sr.groupby('UserId').first().reset_index()

    trips_sr = trips_sr[(trips_sr['mode'] == "Bike")] \
        .sort_values(['Tot_Km'], ascending=False) \
        .head(8)

    bike_trips = trips_denorm[(trips_denorm['Periods'] == "2022")]
    bike_trips = bike_trips.groupby(['UserId', 'motive'])['Trip in a year']\
        .sum().reset_index(name="tot_trips")\
        .sort_values(['UserId', 'tot_trips'], ascending=True)

    bike_trips = bike_trips.groupby('UserId').head(3)

    # itended among bike trips otherwise we should consider all trips (trips_denorm)
    bike_trips = bike_trips[bike_trips['UserId'].isin(trips_sr['UserId'].tolist())]

    print(bike_trips.to_string())
    return bike_trips


def question4(connIn,denormData=None):
    print("Taking the top 10 people who took the least number of kms to atend education/courses, show for every year the average number of trips made by these users.")
    if(denormData is None):
        trips_denorm=md.read_fromDB(connIn)
    else:
        trips_denorm=denormData

    trips_edu = trips_denorm.groupby(['UserId', 'motive'])['Km travelled in a year'] \
        .sum().reset_index(name="Tot_Km") \
        .sort_values(['UserId', 'Tot_Km'], ascending=True)

    trips_edu = trips_edu[(trips_edu['motive'] == "Attending education/courses") & (trips_edu['Tot_Km'] != 0)] \
        .sort_values(['Tot_Km'], ascending=True) \
        .head(10)

    users_top10 = trips_denorm[trips_denorm['UserId'].isin(trips_edu['UserId'].tolist())]

    users_top10 = users_top10.groupby(['UserId', 'Periods'])['Trip in a year'] \
        .mean().reset_index(name="mean_trips") \
        .sort_values(['UserId', 'Periods'], ascending=True)


    print(users_top10.to_string())

    return users_top10