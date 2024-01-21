from db import Schedule, Group


def get_all_schedule(session):
    return session.query(Schedule).all()


def get_schedule_by_group(session, group):
    return session.query(Schedule).join(Group).filter(Group.name == group).all()
