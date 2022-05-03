import databases
import sqlalchemy
from decouple import config


DATABASE_URL = f"postgresql://" \
               f"{config('DB_USER')}:" \
               f"{config('DB_PASSWORD')}@" \
               f"{config('DB_HOST')}:" \
               f"{config('DB_PORT')}/" \
               f"{config('DB_NAME')}"


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


