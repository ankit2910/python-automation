# Platform Automation & CI Validation

This repository demonstrates a Python-based automation project integrated with GitHub Actions CI.
The goal of this project is to perform platform-level validations and fail the pipeline early if
configuration or integration issues are detected.

## What This Project Does

- Validates presence of required repository files before deployment
- Performs API health checks using REST calls
- Automatically runs validations on every push and pull request
- Fails the CI pipeline if any validation does not pass

## Tech Stack

- Python 3.11
- GitHub Actions
- Linux (GitHub-hosted runner)
- REST APIs

## How CI Works

1. Code is pushed to the repository
2. GitHub Actions workflow is triggered
3. Python environment is set up
4. Validation scripts are executed
5. Pipeline fails if any check fails