from github_connector import GitHubIssues
from jira_connector import JiraConnector

"""
repository = "sendgrid-python"

gh_client = SendGridGitHubIssues()
issues, pulls = gh_client.get_open_issues_and_pull_requests(repository)
print issues
print pulls
csv = gh_client.create_csv()
f1=open('./csv.txt', 'w+')
f1.write(csv)
"""

jira_client = JiraConnector()

"""
issues = jira_client.get_issues("elmer")
print issues

result = jira_client.add_comment("LIBS-146", "Testing Jira Connector Class")
print result

issue = jira_client.get_issue("LIBS-78")
print issue.fields.project.raw
print issue.fields.raw

"""

project = {'key': 'LIBS'}
summary = 'New issue from jira-python TEST'
description = 'Just testing, safe to delete'
issuetype = {'name': 'Task'}
new_issue = jira_client.create_issue(project, summary, description, issuetype)
