# TripsDataChallenge

### Run with docker 

#####Requiremnts:




### Run without docker 

#####Requiremnts:
git, python, pip, PowerBI, postres, jupyther 

1) Open terminal/powershell end clone a repository (main branch used as production):
    > git clone -b main https://github.com/ValentinPopov1989/TripsDataChallenge.git
    > 
    > cd TripsDataChallenge
2) install libraries and package with solution
   >python3 -m pip install pandas sqlalchemy psycopg2 python-dotenv
   > 
   > python3 -m pip install -e .\trips_processor_package\
3) An instance of database Postgres is running as in .env 
   > CREATE DATABASE trips_challenge ; 
4) A **complete test** of a solution package can be done:
   > python3 .\trips_processor_package\trips_processor,
   > 
   > after this run resul files will be prodused in **TripsDataChallenge\results**
5) Or single test 
   >python3 .\trips_processor_package\trips_processor\tests\test_q1.py

6) Open a dashboard.pbix and  in transform data tab modify **FilePath** parameter with current folder path. This will allow you to refresh sources files for visualization
