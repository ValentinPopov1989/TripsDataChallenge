from trips_processor.data_processing import read_data as rd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def test_read_data():
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_pwd = os.getenv("DB_PWD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    dir_path = os.getenv("DATA_DIR")

    # dialect+driver://username:password@host:port/database
    out_connection_str = "postgresql+psycopg2://" + db_user + ":" + db_pwd + "@" + db_host + ":" + db_port + "/" + db_name
    # conect to DB
    connOut = create_engine(out_connection_str)

    rd.readFiles(dir_path, connOut)


if __name__ == '__main__':
    test_read_data()