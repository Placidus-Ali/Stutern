import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


# Loading my csv file into my table
coursemates_info = pd.read_csv("coursemate.csv")

#check
print("Info loaded successfully")

#create engine connection
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/coursemate.db")

