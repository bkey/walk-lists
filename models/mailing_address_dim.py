from sqlalchemy import Column, VARCHAR, BIGINT

from db.postgresql_connector import Base

class MailingAddresDim(Base):
    __tablename__ = 'mailing_address_dim'

    mailing_address_id = Column('mailing_address_id', BIGINT, primary_key=True)
    address_line1 = Column('address_line1', VARCHAR(110))
    address_line2 = Column('address_line2', VARCHAR(50))
    city = Column("city", VARCHAR(50))
    state = Column("STATE", VARCHAR(20))
    zip_code = Column("zip_code", VARCHAR(10))
    country = Column("country", VARCHAR(30))
    hashcode = Column("hashcode", BIGINT, nullable=False)

    def to_address_string(self):
        address_parts = \
            [address_part for address_part in
             [self.address_line1, self.address_line2, self.city, self.state, self.zip_code] if address_part]
        return " ".join(address_parts)

    def __repr__(self):
        return '<MailingAddres(id={0}, address={1} {2})>'.format(self.mailing_address_id,
                                                                 self.address_line1,
                                                                 self.address_line2)

