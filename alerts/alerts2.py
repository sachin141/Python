from github import Github
import requests
from bs4 import BeautifulSoup
import re


g = Github('PAT')


repo = g.get_repo('sachin141/python')

# Get all code scanning alerts for the repository
alerts = repo.get_codescan_alerts()


print(alerts)
# Iterate over each alert
for alert in alerts:
    # Check if severity is High or above
    if alert.rule.severity in ['error', 'warning']:
        print("*********", alert.rule)
        # Extract CWE ID from the rule description
#        cwe_id_match = re.search(r'CWE-(\d+)', alert.rule.description)
##        if cwe_id_match:
#           cwe_id = cwe_id_match.group(0)
#            # Construct the URL for the CWE page
#            cwe_url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
#            # Fetch the CWE page
#            response = requests.get(cwe_url)
            # Parse the HTML
#            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the 'Likelihood of exploitability' section
#            likelihood_section = soup.find('div', id='likelihood_of_exploit')
#            if likelihood_section:
#                likelihood_text = likelihood_section.text.strip()
                # Check if 'Likelihood of exploitability' is High or above
#                if 'High' in likelihood_text or 'Very High' in likelihood_text:
                    # Print the vulnerability details
#                    print(f"Vulnerability: {alert.rule.description}")
#                    print(f"Severity: {alert.rule.severity}")
#                    print(f"CWE ID: {cwe_id}")
#                    print(f"Likelihood of exploitability: {likelihood_text}")
#                    print()
