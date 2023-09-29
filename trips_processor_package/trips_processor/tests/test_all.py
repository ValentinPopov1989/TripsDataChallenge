from trips_processor.data_processing import get_trip_anasysis as ta
from trips_processor.data_processing import manipulate_data as md
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def test_all():
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_pwd = os.getenv("DB_PWD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    res_dir = os.getenv("RESULT_DIR")

    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
        print("created folder", res_dir)

    # dialect+driver://username:password@host:port/database
    out_connection_str = "postgresql+psycopg2://" + db_user + ":" + db_pwd + "@" + db_host + ":" + db_port + "/" + db_name
    # conect to DB
    connIn = create_engine(out_connection_str)
    trips_denorm = md.read_fromDB(connIn)


    res = ta.question1(connIn=None,denormData=trips_denorm)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q1.csv'), index=False, encoding='utf-8')

    res = ta.question2(connIn=None,denormData=trips_denorm)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q2.csv'), index=False, encoding='utf-8')

    res = ta.question3(connIn=None,denormData=trips_denorm)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q3.csv'), index=False, encoding='utf-8')

    res = ta.question4(connIn=None,denormData=trips_denorm)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q4.csv'), index=False, encoding='utf-8')


if __name__ == '__main__':
    test_all()