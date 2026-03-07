from app.core.database import engine, Base
from app.models import user
    

# import models so SQLAlchemy registers them

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()