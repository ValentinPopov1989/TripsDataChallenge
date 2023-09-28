from trips_processor.data_processing import read_data as rd
from sqlalchemy import create_engine

def test_read_data():
    # folder path
    dir_path = r'C:\Users\Valentin Popov\conda_projects\data'
    db_user = 'postgres'
    db_pwd = 'root'
    db_name = 'trips_challenge'
    db_host = 'localhost'
    db_port = '5433'

    # dialect+driver://username:password@host:port/database
    out_connection_str = "postgresql+psycopg2://" + db_user + ":" + db_pwd + "@" + db_host + ":" + db_port + "/" + db_name
    # conect to DB
    connOut = create_engine(out_connection_str)

    rd.readFiles(dir_path, connOut)


if __name__ == '__main__':
    test_read_data()