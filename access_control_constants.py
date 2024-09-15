from enum import Enum


class AccessTypes(Enum):
    """ Represent the 3 different access types within the access matrix

    """
    Read = "Read"
    ReadWrite = "Read and Write"
    NoPrivilege = "No Privilege"


class AccessObjects(Enum):
    """ Represent the access objects of the system, which are the different permissions in the system

    """
    ClientAccBalance = "Client Account Balance"
    ClientInvestPortfolio = "Client Investment Portfolio"
    FinAdvisorContactDetails = "Financial Advisor Contact Details"
    FinPlannerContactDetails = "Financial Planner Contact Details"
    InvestAnalystContactDetails = "Investment Analyst Contact Details"
    MoneyMarketInstruments = "Money Market Instruments"
    PrivateConsumerInstruments = "Private Consumer Instruments"
    DerivativesTrading = "Derivatives Trading"
    InterestInstruments = "Interest Instruments"
    SystemDuringBusiness = "System During Business Hours"
    SystemOutsideBusiness = "System Outside Business Hours"
    ValidateInvestPortfolios = "Validate Investment Portfolios"
    ReqClientAcc = "Request Client Account"


class AccessSubjects(Enum):
    """ Represents the access subjects of the system, which are the different roles a user can have

    """
    Clients = "Client"
    PremiumClients = "Premium Client"
    FinPlanners = "Financial Planner"
    FinAdvisors = "Financial Advisor"
    InvestAnalyst = "Investment Analyst"
    TechSupport = "Technical Support"
    Tellers = "Teller"
    ComplianceOfficers = "Compliance Officer"
