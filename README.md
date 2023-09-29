# TripsDataChallenge

### Run without docker using venv

#####Requiremnts:
git, python, pip, PowerBI, postres, jupyther 

1) Open terminal/powershell end clone a repository:
    1) git clone https://github.com/ValentinPopov1989/TripsDataChallenge.git
    2) cd TripsDataChallenge
2) install libraries and package with solution
   1) python3 -m pip install pandas sqlalchemy psycopg2 python-dotenv
   2) python3 -m pip install -e .\trips_processor_package\
3) An instance of database Postgres is running as in .env 
   1) CREATE DATABASE trips_challenge ; 
4) A **complete test** of a solution package can be done:
   1) python3 .\trips_processor_package\trips_processor, after this run resul files will be prodused in **TripsDataChallenge\results**
5) Or single test python3 .\trips_processor_package\trips_processor\tests\test_q1.py

6) Open a dashboard.pbix and  in transform data tab modify **FilePath** parameter with current folder path. This will allow you to refresh sources files for visualization











1.
to install in developer mode: 
in the parent directory ‘trips_processor_package', run:
pip install -e ./

2.
change the path of the data file: 

3.
for a generic run: 
from the directory trips_processor_package: 
run the command: 
> python trips_processor
to run the code in the main module: a trips_processor for a chosen product (this runs the functions in NAME.py) 

4. to run a specific test: 
from the directory trips_processor_package: 
> python trips_processor/tests/NAME.py 
or 
> python trips_processor/tests/NAME2.py 