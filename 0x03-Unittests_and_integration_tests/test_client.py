#!/usr/bin/env python3
""" Github client"""
import unittest
from unittest.mock import patch, MagicMock
from fixtures import public_repos_fixtures, expected_repos_with_apache_license
from client import GithubOrgClient


class TestGithubOrgClient(unittest.Testcase):
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
    unittest.main()
