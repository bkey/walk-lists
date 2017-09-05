from sqlalchemy import Column, VARCHAR, BIGINT, DATE, Integer

from db.postgresql_connector import Base


class VoterDim(Base):
    __tablename__ = 'voter_dim'

    voter_id = Column('voter_id', BIGINT, primary_key=True)
    person_key = Column('person_key', BIGINT) # foreign key references person_dim
    state_voter_ref = Column('state_voter_ref', VARCHAR(31))
    county_voter_ref = Column('county_voter_ref', VARCHAR(20))
    title = Column('title', VARCHAR(5))
    first_name = Column('first_name', VARCHAR(50))
    middle_name = Column('middle_name', VARCHAR(50))
    last_name = Column('last_name', VARCHAR(50))
    name_suffix = Column('name_suffix', VARCHAR(10))
    gender = Column('gender', VARCHAR(1))
    race = Column('race', VARCHAR(1))
    birthdate = Column('birthdate', DATE)
    birth_state = Column('birth_state', VARCHAR(2))
    registration_date = Column('registration_date', DATE)
    registration_status = Column('registration_status', VARCHAR(15))
    absentee_type = Column('absentee_type', VARCHAR(1))
    email = Column('email', VARCHAR(50))
    phone = Column('phone', VARCHAR(15))
    do_not_call_status = Column('do_not_call_status', VARCHAR(1))
    language_choice = Column('language_choice', VARCHAR(3))
    version = Column('version', Integer, nullable=False, default=0)
    valid_from = Column('valid_from', DATE)
    valid_to = Column('valid_to', DATE)

    def __repr__(self):
        return '<Voter(id={0}, name={1} {2})>'.format(self.voter_id,
                                                     self.first_name,
                                                     self.last_name)
