from jira import JIRA
import os
from os.path import join, dirname
from dotenv import load_dotenv

class JiraConnector(object):
    
    """SendGrid GitHub Issues & Pull Requests"""
    def __init__(self, **opts):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self._username = opts.get('username', None) or os.environ.get('JIRA_USERNAME')
        self._password = opts.get('password', None) or os.environ.get('JIRA_PASSWORD')
        if(self._username == None or self._password == None):
            raise BadParams("Please specify your Jira username and password. (e.g. username=your_jira_username) or use a .env file\n")
        self._jira = JIRA('https://jira.sendgrid.net' , 
            basic_auth=(self._username, self._password))
        self._issues = []
            
    @property
    def jira(self):
        return self._jira
    
    @property
    def issues(self):
        return self._issues
    
    def get_issue(self, issue_id):
        issue = self.jira.issue(issue_id)
        return issue
    
    def get_issues(self, userid):
        self._issues = self.jira.search_issues('assignee=' + userid)
        return self.issues
        
    def add_comment(self, issue_id, comment):
        issue = self.jira.get_issue(issue_id)
        result = self.jira.add_comment(issue, comment)
        return result
        
    def create_issue(self, project_key, summary, description, issuetype):
        new_issue = self.jira.create_issue(project=project_key, summary=summary, description=description, issuetype=issuetype)