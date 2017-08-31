from models.voter_dim import VoterDim
from models.mailing_address_dim import MailingAddresDim
from models.voter_report_fact import VoterReportFact
from sqlalchemy import and_


def get_voters_for_precinct(session, precinct_id, status="ACTIVE", party=1):
    # todo add filters like voted in last election, new voter etc
    # todo better handle party. 1 is Democratic party, 2 is Republican
    return session.query(MailingAddresDim).join(VoterReportFact).join(VoterDim).filter(
        and_(VoterReportFact.precinct_key == precinct_id,
             VoterReportFact.party_key == party,
             VoterDim.registration_status == status)).all()
