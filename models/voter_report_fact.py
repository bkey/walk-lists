from sqlalchemy import Column, VARCHAR, BIGINT, DATE, Integer, ForeignKey

from db.postgresql_connector import Base


class VoterReportFact(Base):
    __tablename__ = 'voter_report_fact'

    # todo many of these columns are foreign keys referencing tables not currently being used
    voter_report_id = Column('voter_report_id', BIGINT, primary_key=True)
    voter_report_date = Column('voter_report_date', DATE)
    date_key = Column('date_key', Integer, nullable=False)
    report_status = Column('report_status', VARCHAR(45))
    reporter_key = Column('reporter_key', Integer)
    voter_key = Column('voter_key', BIGINT, ForeignKey('voter_dim.voter_id'))
    household_key = Column('household_key', BIGINT)
    mailing_address_key = Column('mailing_address_key', BIGINT,
                                 ForeignKey('mailing_address_dim.mailing_address_id'))
    social_media_account_key = Column('social_media_account_key', Integer)
    party_key = Column('party_key', Integer)
    precinct_key = Column('precinct_key', Integer)
    county_key = Column('county_key', Integer)
    ward_key = Column('ward_key', Integer)
    congressional_dist_key = Column('congressional_dist_key', Integer)
    county_district_key = Column('county_district_key', Integer)
    state_key = Column('state_key', Integer)
    lower_house_dist_key = Column('lower_house_dist_key', Integer)
    upper_house_dist_key = Column('upper_house_dist_key', Integer)
    unified_school_dist_key = Column('unified_school_district_key', Integer)
    staffer_key = Column('staffer_key', Integer)
    campaign_key = Column('campaign_key', Integer)

    def __repr__(self):
        return '<VoterReportFact(id={0})>'.format(self.voter_report_id)

