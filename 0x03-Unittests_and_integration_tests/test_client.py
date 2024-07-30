#!/usr/bin/env python3
""" Github client"""
import unittest
from urllib import response
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.Testcase):
    """
    Test the GithubOrgClient class methods
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        Args:
            org (str): organisation's name
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        Test TestGithubOrgClient's _public_repos_url method works
        as expected.
        """
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            test_repo_url = test_org._public_repos_url
            self.assertEqual(test_repo_url, m.return_value.get('repos_url'))
            m.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_repo):
        """
        Test GithubOrgClient's public_repos method
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as m:

            test_client = GithubOrgClient('holberton')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            m.assert_called_once()



    
    """ a class that test github client """
    @patch("client.GithubOrgClient._public_repos_data",
           return_value=public_repos_fixture)
    def test_public_repos(self, mock_repos: MagicMock) -> None:
        """Test public repos """
        client: GithubOrgClient = GithubOrgClient('test_org')
        result: List[str] = client.public_repos()
        expected_result: List[str] = [
            repo['name'] for repo in public_repos_fixture]
        self.assertEqual(result, expected_result)

    @patch('client.GithubOrgClient._public_repos_data',
           return_value=public_repos_fixture)
    def test_public_repos_with_license(self, mock_repos: MagicMock): -> None:
        """ test public repos with license """
        client: GithubOrgClient = GithubOrgClient("test_org")
        result: List[str] = client.public_repos(license='apache-2.0')
        self.assertEqual(result, expected_repos_with_apache_license)


if __name__ == "__main__":
    """ if name is main run the unittest """
    unittest.main()
