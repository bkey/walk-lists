from models.voter_dim import VoterDim
from models.mailing_address_dim import MailingAddresDim
from models.voter_report_fact import VoterReportFact
from sqlalchemy import and_
import sqlalchemy


def get_voters_for_district(session, district_id, status="ACTIVE", party=1):
    # todo add filters like voted in last election, new voter etc
    # todo better handle party. 1 is Democratic party, 2 is Republican
    return session.query(
        sqlalchemy.func.lower(MailingAddresDim.address_line1),
        sqlalchemy.func.lower(MailingAddresDim.city),
        sqlalchemy.func.lower(MailingAddresDim.state),
        sqlalchemy.func.lower(MailingAddresDim.zip_code),
        sqlalchemy.func.array_agg(MailingAddresDim.address_line2),
        sqlalchemy.func.count("*")
    ).join(VoterReportFact).join(VoterDim).filter(
        and_(VoterReportFact.upper_house_dist_key == district_id,
             VoterReportFact.party_key == party,
             VoterDim.registration_status == status)).group_by(
        sqlalchemy.func.lower(MailingAddresDim.address_line1),
        sqlalchemy.func.lower(MailingAddresDim.city),
        sqlalchemy.func.lower(MailingAddresDim.state),
        sqlalchemy.func.lower(MailingAddresDim.zip_code)
    ).all()
