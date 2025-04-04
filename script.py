import requests
import yaml
from jira import JIRA
import csv
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_work_packages(api_url: str, token: str) -> List[Dict[str, Any]]:
    """
    Retrieves work packages from the given API endpoint using the provided token.
    """
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{api_url}/work_packages', headers=headers)
    response.raise_for_status()  # Raises an exception if the response status is not 200
    data = response.json()
    return data.get('work_packages', [])

def load_mapping_from_string(mapping_str: str) -> Dict[str, str]:
    """
    Loads the field mapping configuration from a YAML string.
    """
    return yaml.safe_load(mapping_str)

def transform_package(work_package: Dict[str, Any], mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Transforms a work package using the provided mapping.
    """
    transformed = {}
    for source_field, target_field in mapping.items():
        transformed[target_field] = work_package.get(source_field)
    return transformed

def create_issue(jira_server: str, jira_token: str, issue_data: Dict[str, Any]) -> Any:
    """
    Creates an issue in Jira using the provided issue data.
    """
    options = {"server": jira_server}
    jira = JIRA(options, token_auth=jira_token)
    issue = jira.create_issue(fields=issue_data)
    return issue

def write_data_to_csv(data: List[Dict[str, Any]], filename: str) -> None:
    """
    Writes the provided data to a CSV file.
    """
    if not data:
        logging.info("No data available to write to CSV.")
        return

    headers = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    logging.info(f"Data successfully written to {filename}")

def main() -> None:
    # Configuration
    OPENPROJECT_API_URL = "https://your-openproject-instance/api/v3"
    OPENPROJECT_TOKEN = "your_openproject_token"
    JIRA_SERVER = "https://your-jira-instance.atlassian.net"
    JIRA_TOKEN = "your_jira_token"
    
    mapping_yaml = (
        "subject: summary\n"
        "description: description\n"
    )
    mapping = load_mapping_from_string(mapping_yaml)
    
    try:
        work_packages = get_work_packages(OPENPROJECT_API_URL, OPENPROJECT_TOKEN)
    except Exception as e:
        logging.error(f"Error fetching work packages: {e}")
        return

    csv_data = []
    
    # Process each work package and create corresponding issues in Jira
    for wp in work_packages:
        issue_data = transform_package(wp, mapping)
        try:
            issue = create_issue(JIRA_SERVER, JIRA_TOKEN, issue_data)
            logging.info(f"Successfully created issue: {issue.key}")
            # Append created issue data for CSV logging
            csv_data.append({
                "issue_key": issue.key,
                **issue_data
            })
        except Exception as e:
            logging.error(f"Error creating issue: {e}")
            # Save data even if an error occurs for debugging purposes
            csv_data.append({
                "issue_key": None,
                **issue_data,
                "error": str(e)
            })

    write_data_to_csv(csv_data, "output.csv")

if __name__ == "__main__":
    main()
