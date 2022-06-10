from cs50 import SQL

# connect to database
#db = SQL('sqlite:///project.db')
#db = SQL('sqlite:///project_cascade.db')
db = SQL('sqlite:///project_noforeign.db')

# places where that polices work
PLACES = [
    'tainan',
    'taipei',
    'kaohsiung',
    'taoyuan'
]

PLACEOFOCCUR = [place.upper() for place in PLACES]

# to store and update globle variables from request
tmp_data = {}
