from github import Github
import sys


g = Github('PAT')


repo = g.get_repo('sachin141/python')

# Get all code scanning alerts for the repository
alerts = repo.get_codescan_alerts()
print(alerts)
# Filter alerts for Bandit scans with severity 'High' or above
bandit_high_or_above_alerts = [alert for alert in alerts]
print(bandit_high_or_above_alerts)


# Print the details of Bandit high or above alerts
for alert in bandit_high_or_above_alerts:
    print(alert.rule.description)
    print(alert.created_at)
    print(alert.rule.severity)
    print(alert.html_url)
    print("---------------")