import json
import unittest

from main.git_crawler import GitCrawler
from test.base import PyGithubTestCase

"""
class TestUser(PyGithubTestCase):

    def test_username(self):
        user = GitCrawler("octocat")._getting_user()

        with open('./user.json', 'rb') as f:
            expected_body = json.load(f)

        self.assertEqual(user.login, expected_body['login'])  # Tr


    def test_org(self):
        org_details = git_crawler.GitCrawler("OSGeo")._getting_organisation_details()
        sample = git_crawler.GitCrawler("OSGeo")._getting_organisation_details()

        with open('./org.json', 'rb') as f:
            expected_body = json.load(f)
            #repos = int(org_details["number of repositories"][0])

        print(org_details)
        print(sample)
        #self.assertEqual(34, sample)  # Tr
        """


class TestUser1(unittest.TestCase):
    def test_user_name(self):
        user = GitCrawler("sadaffgh")._getting_user()
        self.assertEqual(user.login, 'sadaffgh')

