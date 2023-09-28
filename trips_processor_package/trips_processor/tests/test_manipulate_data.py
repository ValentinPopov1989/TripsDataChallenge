from trips_processor.data_processing import manipulate_data as md
from sqlalchemy import create_engine


def test_man_data():
    db_user = 'postgres'
    db_pwd = 'root'
    db_name = 'trips_challenge'
    db_host = 'localhost'
    db_port = '5433'

    # dialect+driver://username:password@host:port/database
    out_connection_str = "postgresql+psycopg2://" + db_user + ":" + db_pwd + "@" + db_host + ":" + db_port + "/" + db_name
    # conect to DB
    connIn = create_engine(out_connection_str)

    res=md.read_fromDB(connIn)

    r_writed=res.to_sql('trips_denorm', con=connIn, if_exists='replace', chunksize=1000, index=False)
    print("writed ",r_writed," records.")

if __name__ == '__main__':
    test_man_data()