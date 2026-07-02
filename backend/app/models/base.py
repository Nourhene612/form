try:
    from sqlalchemy.orm import DeclarativeBase
except ImportError:  # SQLAlchemy 1.4 fallback
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
else:
    class Base(DeclarativeBase):
        pass