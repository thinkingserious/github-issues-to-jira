# Given the name of a SendGrid Github repository, this file will find all the issues and pull requests
import os
from github3 import login
from os.path import join, dirname
from dotenv import load_dotenv

class BadParams(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class GitHubIssues(object):
    
    """GitHub Issues & Pull Requests"""
    def __init__(self, **opts):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self._github_token = opts.get('github_token', None) or os.environ.get('GITHUB_TOKEN')
        if(self._github_token == None):
            raise BadParams("Please specify a GitHub token. (e.g. github_token=your_github_token) or use a .env file\n")
        self._github = login(token=self._github_token)
        self._issues = []
        self._pulls = []
    
    @property
    def github(self):
        return self._github
        
    @property
    def issues(self):
        return self._issues
        
    @issues.setter
    def issues(self, value):
        self._issues = value
    
    @property
    def pulls(self):
        return self._pulls
    
    @pulls.setter
    def pulls(self,value):
        self._pulls = value

    @property
    def pulls(self):
        return self._pulls
    
    def get_open_issues_and_pull_requests(self, repository=None, username="sendgrid", 
            milestone=None, state="open", assignee=None, mentioned=None, 
            labels=None, sort=None, direction=None, since=None, number=-1, etag=None):
        if(repository == None):
            raise BadParams("You must specify a repository, e.g. \"")
        repo = self.github.repository(username, repository)
        issues_and_pulls = repo.issues(milestone, state, assignee, mentioned, 
                labels, sort, direction, since, number, etag)
        issues = []
        pulls = []
        for x in issues_and_pulls:
            if "issues" in x.html_url:
                issue = {
                    "title": x.title,
                    "url": x.html_url
                }
                issues.append(issue)
            else:
                pull = {
                    "title": x.title,
                    "url": x.html_url
                }
                pulls.append(pull)
        self._issues = issues
        self._pulls = pulls
        return issues, pulls
        
    def create_csv(self, csv_header="Task Summary, Description, Story Points, AC, Epic Link\n"):
        csv = csv_header
        print self._issues
        for x in self._issues:
            csv = csv + '"' + x['title'] + '"' + "," + x['url'] + "\n" 
        for x in self._pulls:
            csv = csv + '"' + x['title'] + '"' + "," + x['url'] + "\n" 
        return csv
