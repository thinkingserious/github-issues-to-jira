from app import SendGridGitHubIssues

repository = "sendgrid-python"

client = SendGridGitHubIssues()
issues, pulls = client.get_open_issues_and_pull_requests(repository)
print issues
print pulls
csv = client.create_csv()
f1=open('./csv.txt', 'w+')
f1.write(csv)