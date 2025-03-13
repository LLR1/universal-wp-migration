import requests
import yaml
from jira import JIRA
import csv

def get_work_packages(api_url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{api_url}/work_packages', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('work_packages', [])
    else:
        raise Exception("Error fetching work packages: " + response.text)

def load_mapping_from_string(mapping_str):
    return yaml.safe_load(mapping_str)

def transform_package(work_package, mapping):
    transformed = {}
    for source_field, target_field in mapping.items():
        transformed[target_field] = work_package.get(source_field)
    return transformed

def create_issue(jira_server, jira_token, issue_data):
    options = {"server": jira_server}
    jira = JIRA(options, token_auth=jira_token)
    issue = jira.create_issue(fields=issue_data)
    return issue

def write_data_to_csv(data, filename):
    if not data:
        print("No data to write.")
        return

    headers = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Data successfully written to {filename}")

def main():
    OPENPROJECT_API_URL = "https://your-openproject-instance/api/v3"
    OPENPROJECT_TOKEN = "your_openproject_token"
    JIRA_SERVER = "https://your-jira-instance.atlassian.net"
    JIRA_TOKEN = "your_jira_token"
    
    mapping_yaml = (
        "subject: summary\n"
        "description: description\n"
    )
    mapping = load_mapping_from_string(mapping_yaml)
    
    # Extract work packages from the source system.
    work_packages = get_work_packages(OPENPROJECT_API_URL, OPENPROJECT_TOKEN)

    csv_data = []
    
    # Process each work package and create corresponding issues in Jira.
    for wp in work_packages:
        issue_data = transform_package(wp, mapping)
        try:
            issue = create_issue(JIRA_SERVER, JIRA_TOKEN, issue_data)
            print(f"Successfully created issue: {issue.key}")
        except Exception as e:
            print(f"Error creating issue: {e}")

    write_data_to_csv(csv_data, "output.csv")

if __name__ == "__main__":
    main()
