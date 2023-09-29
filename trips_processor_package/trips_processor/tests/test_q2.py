from trips_processor.data_processing import get_trip_anasysis as ta
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def test_q2():
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

    res = ta.question2(connIn)
    print(res.shape)
    res.to_csv(os.path.join(res_dir, 'q2.csv'), index=False, encoding='utf-8')


if __name__ == '__main__':
    test_q2()