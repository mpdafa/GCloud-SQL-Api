from odps import ODPS

# Replace with your Alibaba Cloud MaxCompute credentials
ACCESS_ID = 'your_access_id'
ACCESS_KEY = 'your_access_key'
PROJECT_NAME = 'your_project_name'
ENDPOINT = 'your_endpoint'

# Create a MaxCompute instance
odps = ODPS(ACCESS_ID, ACCESS_KEY, PROJECT_NAME, ENDPOINT)

# Define the table you want to query
table_name = 'dana_dw_ops.vw_ods_flux_ex_serial'

# Query data from the table
with odps.execute_sql(f'SELECT transaction_id FROM {table_name}') as reader:
    for record in reader:
        print(record)



from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your Google Cloud SQL database connection details
DB_USER = 'db_user'
DB_PASSWORD = 'db_password'
DB_NAME = 'db_name'
DB_INSTANCE = 'db_instance_connection'

# Create an engine for the database
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@127.0.0.1/{DB_NAME}?unix_socket=/cloudsql/{DB_INSTANCE}"
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define a model using SQLAlchemy
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Create tables if they do not exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Perform database operations
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()

# Query data from the database
users = session.query(User).all()
for user in users:
    print(f"User {user.id}: {user.username}, {user.email}")

# Close the session
session.close()        