from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def startup_db():
    from models.residencia import ResidenciaBD
    database.connect()
    database.create_tables([ResidenciaBD])

def shutdown_db():
    database.close()