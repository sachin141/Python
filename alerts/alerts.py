import requests
import sys
from bs4 import BeautifulSoup

# GitHub repository information
owner = 'sachin141'
repo = 'python'
token = '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'

# Fetch code scanning alerts from GitHub
url = 'https://api.github.com/repos/sachin141/Python/code-scanning/alerts'
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'Bearer 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'
}
response = requests.get(url, headers=headers)
alerts = response.json()

# Print alerts to understand its structure
#print(alerts)

# Assume alerts is a list of dictionaries
high_alerts = [alert for alert in alerts if alert['tool'] == 'bandit' and alert['state'] == 'open']

# Function to fetch 'Likelihood of exploitability' from CWE website
def get_exploitability(cwe_id):
    cwe_url = f'https://cwe.mitre.org/data/definitions/{cwe_id}.html'
    response = requests.get(cwe_url)
    if response.status_code == 200:
        exploitability = response.text
        # Parse the HTML to extract the 'Likelihood of exploitability'
        soup = BeautifulSoup(exploitability, 'html.parser')
        likelihood_div = soup.find('div', {'id': 'pagebody'})
        exploitability_text = likelihood_div.find('p').text
        return exploitability_text
    else:
        return None

# Print vulnerabilities with severity High or above and 'Likelihood of exploitability' High or above
for alert in high_alerts:
    cwe_id = alert['rule_id']
    exploitability = get_exploitability(cwe_id)
    if exploitability and 'High' in exploitability:
        print(f"Severity: High, CWE ID: {cwe_id}, Exploitability: High")