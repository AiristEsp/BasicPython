import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month

date_of_birth = dt.datetime(
    year= 2004, 
    month= 12,
    day= 15
    )

print(date_of_birth)