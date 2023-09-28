from trips_processor.data_processing import get_trip_anasysis as ta
from sqlalchemy import create_engine
import os

def test_q4():
    res_dir = r'C:\Users\Valentin Popov\conda_projects\res'
    db_user = 'postgres'
    db_pwd = 'root'
    db_name = 'trips_challenge'
    db_host = 'localhost'
    db_port = '5433'

    # dialect+driver://username:password@host:port/database
    out_connection_str = "postgresql+psycopg2://" + db_user + ":" + db_pwd + "@" + db_host + ":" + db_port + "/" + db_name
    # conect to DB
    connIn = create_engine(out_connection_str)

    res = ta.question4(connIn)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q4.csv'), index=False, encoding='utf-8')


if __name__ == '__main__':
    test_q4()