from access_control_constants import AccessTypes, AccessObjects, AccessSubjects


class AccessControlMatrix:

    def __init__(self):
        """" Initialize the access control matrix with the appropriate subject, order, access type for the Finvest
        Holdings
        """
        self._matrix = {AccessSubjects.Clients: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                 AccessObjects.ClientInvestPortfolio: AccessTypes.Read,
                                                 AccessObjects.FinAdvisorContactDetails: AccessTypes.Read,
                                                 AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                 AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                 AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.PrivateConsumerInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                 AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.SystemDuringBusiness: AccessTypes.Read,
                                                 AccessObjects.SystemOutsideBusiness: AccessTypes.Read,
                                                 AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                 AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                 },
                        AccessSubjects.PremiumClients: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                        AccessObjects.ClientInvestPortfolio: AccessTypes.ReadWrite,
                                                        AccessObjects.FinAdvisorContactDetails: AccessTypes.Read,
                                                        AccessObjects.FinPlannerContactDetails: AccessTypes.Read,
                                                        AccessObjects.InvestAnalystContactDetails: AccessTypes.Read,
                                                        AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                        AccessObjects.PrivateConsumerInstruments: AccessTypes.NoPrivilege,
                                                        AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                        AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                        AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                        AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                        AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                        AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                        },
                        AccessSubjects.FinPlanners: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                     AccessObjects.ClientInvestPortfolio: AccessTypes.ReadWrite,
                                                     AccessObjects.FinAdvisorContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.FinPlannerContactDetails: AccessTypes.ReadWrite,
                                                     AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.MoneyMarketInstruments: AccessTypes.Read,
                                                     AccessObjects.PrivateConsumerInstruments: AccessTypes.Read,
                                                     AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                     AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                     AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                     },
                        AccessSubjects.FinAdvisors: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                     AccessObjects.ClientInvestPortfolio: AccessTypes.ReadWrite,
                                                     AccessObjects.FinAdvisorContactDetails: AccessTypes.ReadWrite,
                                                     AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.PrivateConsumerInstruments: AccessTypes.Read,
                                                     AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                     AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                     AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                     },
                        AccessSubjects.InvestAnalyst: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                       AccessObjects.ClientInvestPortfolio: AccessTypes.ReadWrite,
                                                       AccessObjects.FinAdvisorContactDetails: AccessTypes.NoPrivilege,
                                                       AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                       AccessObjects.InvestAnalystContactDetails: AccessTypes.ReadWrite,
                                                       AccessObjects.MoneyMarketInstruments: AccessTypes.Read,
                                                       AccessObjects.PrivateConsumerInstruments: AccessTypes.Read,
                                                       AccessObjects.DerivativesTrading: AccessTypes.Read,
                                                       AccessObjects.InterestInstruments: AccessTypes.Read,
                                                       AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                       AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                       AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                       AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                       },
                        AccessSubjects.TechSupport: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                     AccessObjects.ClientInvestPortfolio: AccessTypes.Read,
                                                     AccessObjects.FinAdvisorContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                     AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.PrivateConsumerInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                     AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                     AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                     AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                     AccessObjects.ReqClientAcc: AccessTypes.ReadWrite
                                                     },
                        AccessSubjects.Tellers: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                 AccessObjects.ClientInvestPortfolio: AccessTypes.Read,
                                                 AccessObjects.FinAdvisorContactDetails: AccessTypes.NoPrivilege,
                                                 AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                 AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                 AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.PrivateConsumerInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                 AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                 AccessObjects.SystemDuringBusiness: AccessTypes.Read,
                                                 AccessObjects.SystemOutsideBusiness: AccessTypes.NoPrivilege,
                                                 AccessObjects.ValidateInvestPortfolios: AccessTypes.NoPrivilege,
                                                 AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                 },
                        AccessSubjects.ComplianceOfficers: {AccessObjects.ClientAccBalance: AccessTypes.Read,
                                                            AccessObjects.ClientInvestPortfolio: AccessTypes.Read,
                                                            AccessObjects.FinAdvisorContactDetails: AccessTypes.NoPrivilege,
                                                            AccessObjects.FinPlannerContactDetails: AccessTypes.NoPrivilege,
                                                            AccessObjects.InvestAnalystContactDetails: AccessTypes.NoPrivilege,
                                                            AccessObjects.MoneyMarketInstruments: AccessTypes.NoPrivilege,
                                                            AccessObjects.PrivateConsumerInstruments: AccessTypes.NoPrivilege,
                                                            AccessObjects.DerivativesTrading: AccessTypes.NoPrivilege,
                                                            AccessObjects.InterestInstruments: AccessTypes.NoPrivilege,
                                                            AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                                                            AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                                                            AccessObjects.ValidateInvestPortfolios: AccessTypes.ReadWrite,
                                                            AccessObjects.ReqClientAcc: AccessTypes.NoPrivilege
                                                            }}

    def is_access_authorized(self, access_subject: AccessSubjects, access_object: AccessObjects,
                             requested_access_type: AccessTypes) -> bool:
        """ checks if the specified access subject, access object and access type is allowed based of the matrix

        :param access_subject: the user's role in the system
        :param access_object: the access object
        :param requested_access_type: the access type wanting to be allowed
        :return: true if the access type is allowed, false if access type is not allowed
        """
        actual_access_type = self._matrix.get(access_subject).get(access_object)

        if (actual_access_type is requested_access_type) or (
                actual_access_type is AccessTypes.ReadWrite and requested_access_type is AccessTypes.Read):
            return True
        else:
            return False

    def get_capabilities(self, access_subject: AccessSubjects) -> dict:
        """ Gets dictionary of access object and access type for a subject, where the access type is read or read and
        write

        :param access_subject: the user's role in the system
        :return: dictionary of access object and access type for a subject, where the access type is read or read and
        write
        """
        capabilities = {}
        access_object_type = self._matrix.get(access_subject)

        for access_object, access_type in access_object_type.items():
            if access_type is AccessTypes.ReadWrite or access_type is AccessTypes.Read:
                capabilities[access_object] = access_type

        return capabilities
