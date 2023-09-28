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