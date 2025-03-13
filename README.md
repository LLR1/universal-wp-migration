# Universal Work Package Migration Tool

A Python-based utility for extracting, transforming, and loading work packages between project management systems (e.g., OpenProject and Jira).

## Overview

This project allows you to migrate work packages from a source system to a target system using a simple Python script. The tool performs the following steps:
- **Extract:** Retrieve work packages from the source system using its API.
- **Transform:** Map and convert the data to the target system format.
- **Load:** Create issues in the target system (e.g., Jira) using its API.

## Features

- Extracts data via REST API with token-based authentication.
- Transforms data using a YAML-based mapping configuration.
- Loads data into the target system using the appropriate API.
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
