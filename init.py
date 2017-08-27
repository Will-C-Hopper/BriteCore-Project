from sqlalchemy import *

db = create_engine('sqlite:///data.db')

db.echo = False

metadata = BoundMetaData(db)

users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('username', String),
    Column('name', String),
    Column('password', String),
)
users.create()

clients = Table('clients', metadata,
    Column('client_id', Integer, primary_key=True),
    Column('name', string),
)
clients.create()

requests = Table('requests', metadata,
    Column('request_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('Title', String),
    Column('Description', String),
    Column('Date', String),
    Column('Priority', Integer),
    Column('Area', String),
)
requests.create()

u = users.insert()
u.execute({'username': 'ADMIN', 'name': 'John Doe', 'password': ADMIN},
          {'username': 'admin', 'name': 'John Doe', 'password': admin})
          
s = users.select()
rs = s.execute()
