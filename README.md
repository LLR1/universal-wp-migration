# Universal Work Package Migration Tool

A Python-based utility for extracting, transforming, and loading work packages between project management systems (e.g., OpenProject and Jira).

## Overview

This project allows you to migrate work packages from a source system to a target system using a simple Python script. The tool performs the following steps:
- **Extract:** Retrieve work packages from the source system using its API.
- **Transform:** Map and convert the data to the target system format using a YAML-based configuration.
- **Load:** Create issues in the target system (e.g., Jira) using its API.

## Features

- Extracts data via REST API with token-based authentication.
- Transforms data using a YAML-based mapping configuration.
- Loads data into the target system using the appropriate API.
- **Enhanced Logging:** Uses Python’s `logging` module for detailed logging of operations and errors.
- **Type Annotations:** Incorporates type hints for better code clarity and easier maintenance.
- **CSV Output:** Records successful and failed operations in a CSV file for audit and debugging purposes.
- Single-file version for quick prototyping and testing.
- Easy to extend for additional functionalities.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [PyYAML](https://pypi.org/project/PyYAML/)
- [jira](https://pypi.org/project/jira/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LLR1/universal-wp-migration.git
2. Navigate to the project directory:
   (git bash) cd universal-wp-migration
3. Install the required packages:
   (git bash) pip install -r requirements.txt

## Configuration
Before running the script, update the configuration parameters in the main() function or, preferably, use environment variables or a separate configuration file. 
Key parameters include:

- OPENPROJECT_API_URL: The URL for your OpenProject API endpoint.

- OPENPROJECT_TOKEN: The token for authentication with OpenProject.

- JIRA_SERVER: The URL for your Jira instance.

- JIRA_TOKEN: The token for authentication with Jira.

- Mapping YAML: A YAML string defining the mapping between OpenProject fields and Jira fields.

## Usage
Run the migration tool with the following command:
   (git bash) python your_script_name.py

The script will:

1. Extract work packages from OpenProject.

2. Transform the data based on the YAML mapping.
3. Create corresponding issues in Jira.

4. Log operations and errors via the logging module.

5. Save the results, including any errors, to an output.csv file.

## Improvements in This Version

- Logging: Replaced print statements with the logging module for more flexible and professional logging.

- Type Annotations: Added type hints to function signatures for improved readability and maintainability.

- Enhanced Error Handling: Implemented better error management for HTTP requests and Jira API interactions, including the use of response.raise_for_status().
- CSV Logging: The script now collects results (successful issue creations and errors) and writes them to a CSV file for easier debugging and audit trails.

- Code Structure: Refactored the code into modular functions, making it more maintainable and easier to extend.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
