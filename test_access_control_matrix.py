import unittest

from access_control_matrix import *


class TestAccessControlMatrix(unittest.TestCase):

    def test_is_access_authorized(self):
        """ Test the is_access_authorized method for AccessControlMatrix

        :return: None
        """
        access_control_matrix = AccessControlMatrix()

        # Test case 1, attempt read access for read permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Clients, AccessObjects.ClientAccBalance,
                                                            AccessTypes.Read)
        expected = True
        self.assertEqual(expected, actual)

        # Test case 2, attempt read and write access for read and write permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.FinPlanners,
                                                            AccessObjects.ClientInvestPortfolio,
                                                            AccessTypes.ReadWrite)
        expected = True
        self.assertEqual(expected, actual)

        # Test case 3, attempt no privilege access for no privilege permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Tellers,
                                                            AccessObjects.MoneyMarketInstruments,
                                                            AccessTypes.NoPrivilege)
        expected = True
        self.assertEqual(expected, actual)

        # Test case 4, attempt read access for read and write permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.FinPlanners,
                                                            AccessObjects.ClientInvestPortfolio,
                                                            AccessTypes.Read)
        expected = True
        self.assertEqual(expected, actual)

        # Test case 5, attempt read and write access for read permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Clients, AccessObjects.ClientAccBalance,
                                                            AccessTypes.ReadWrite)
        expected = False
        self.assertEqual(expected, actual)

        # Test case 6, attempt read access for no privilege permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Tellers,
                                                            AccessObjects.MoneyMarketInstruments,
                                                            AccessTypes.Read)
        expected = False
        self.assertEqual(expected, actual)

        # Test case 7, attempt read and write access for no privilege permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Tellers,
                                                            AccessObjects.MoneyMarketInstruments,
                                                            AccessTypes.ReadWrite)
        expected = False
        self.assertEqual(expected, actual)

        # Test case 8, attempt no privilege access for read permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.Tellers,
                                                            AccessObjects.ClientAccBalance,
                                                            AccessTypes.NoPrivilege)
        expected = False
        self.assertEqual(expected, actual)

        # Test case 9, attempt no privilege access for read and write permission
        actual = access_control_matrix.is_access_authorized(AccessSubjects.PremiumClients,
                                                            AccessObjects.ClientInvestPortfolio,
                                                            AccessTypes.NoPrivilege)
        expected = False
        self.assertEqual(expected, actual)

    def test_get_capabilities(self):
        """ Test the get_capabilities method for AccessControlMatrix

        :return: None
        """
        access_control_matrix = AccessControlMatrix()

        actual = access_control_matrix.get_capabilities(AccessSubjects.ComplianceOfficers)

        expected = {AccessObjects.ClientAccBalance: AccessTypes.Read,
                    AccessObjects.ClientInvestPortfolio: AccessTypes.Read,
                    AccessObjects.SystemDuringBusiness: AccessTypes.ReadWrite,
                    AccessObjects.SystemOutsideBusiness: AccessTypes.ReadWrite,
                    AccessObjects.ValidateInvestPortfolios: AccessTypes.ReadWrite,
                    }
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
