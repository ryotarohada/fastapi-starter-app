from sqlalchemy import text
from db.session import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Hello, World!'"))
    print(result.scalar())
