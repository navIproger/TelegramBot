from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Pair(Base):
    __tablename__ = 'pairs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    day_of_week = Column(Integer)
    number_of_pair = Column(Integer)
    position_of_week = Column(Integer)
    pair_id = Column(Integer, ForeignKey('pairs.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    sub_group = Column(String)
    type_of_pair = Column(String)
    audience = Column(String)
    time_start = Column(String)
    time_end = Column(String)

    group = relationship('Group', back_populates='schedules')
    pair = relationship('Pair', back_populates='schedules')
    teacher = relationship('Teacher', back_populates='schedules')


Group.schedules = relationship('Schedule', order_by='Group.id')
Pair.schedules = relationship('Schedule', order_by='Pair.id')
Teacher.schedules = relationship('Schedule', order_by='Teacher.id')

engine = create_engine('sqlite:///schedule_db.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

