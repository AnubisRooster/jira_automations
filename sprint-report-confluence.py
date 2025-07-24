#!/usr/bin/env python3

import os
import sys
from jira import JIRA
from atlassian import Confluence

# Jira credentials
JIRA_SERVER = os.getenv("JIRA_SERVER", 'https://[domain].atlassian.net')
CONFLUENCE_SERVER = os.getenv("CONFLUENCE_SERVER", 'https://[domain].atlassian.net')
DRY_RUN = True if os.getenv("DRY_RUN", "false") == "true" else False

required_env_vars = [
    'JIRA_USERNAME',
    'JIRA_PASSWORD',
    "JIRA_BOARD_ID",
    "CONFLUENCE_USERNAME",
    "CONFLUENCE_PASSWORD",
    "CONFLUENCE_SPACE_KEY",
    "CONFLUENCE_PARENT_PAGE_ID"
]

# Check if all required environment variables are set
missing_env_vars = [var for var in required_env_vars if var not in os.environ]

if missing_env_vars:
    print(f"Missing environment variables: {', '.join(missing_env_vars)}")
else:
    JIRA_USERNAME = os.environ['JIRA_USERNAME']
    JIRA_PASSWORD = os.environ['JIRA_PASSWORD']
    JIRA_BOARD_ID = os.environ['JIRA_BOARD_ID']
    CONFLUENCE_USERNAME = os.environ['CONFLUENCE_USERNAME']
    CONFLUENCE_PASSWORD = os.environ['CONFLUENCE_PASSWORD']
    CONFLUENCE_SPACE_KEY = os.environ['CONFLUENCE_SPACE_KEY']
    CONFLUENCE_PARENT_PAGE_ID = os.environ['CONFLUENCE_PARENT_PAGE_ID']

# Connect to Jira and Confluence
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))
confluence = Confluence(
    url=CONFLUENCE_SERVER,
    username=CONFLUENCE_USERNAME,
    password=CONFLUENCE_PASSWORD,
)

try:
    closed_sprints = [s for s in jira.sprints(JIRA_BOARD_ID) if s.state == 'closed']

    if not closed_sprints:
        print("No closed sprints found for the scrum board.")
        sys.exit(1)
    else:
        # Find the last closed sprint
        sprint = max(closed_sprints, key=lambda s: s.id)
        sprint_id = sprint.id
        print(f"Last closed sprint ID: {sprint_id} {sprint.name}")

    # Get the sprint issues
    sprint_issues = jira.search_issues(
        f'Sprint = {sprint.id}',
        maxResults=False,
    )

    for issue in sprint_issues:
        print(f"Issue {issue.key}")

    # Prepare the table content
    table_rows = []
    for issue in sprint_issues:
        table_row = "| {key} | {summary} | {status} |".format(
            key=issue.key,
            jira_server=JIRA_SERVER,
            summary=issue.fields.summary,
            status=issue.fields.status,
        )
        table_rows.append(table_row)

    # Create the page in Confluence
    page_title = "Sprint {} Summary".format(sprint.name)
    page_content = """
    h2. Sprint Summary - {}

    ||Issue Key||Summary||Status||
    |{}|
    """.format(sprint.name, '\n'.join(table_rows))

    print(page_content)

    if DRY_RUN:
        print("Skipping page creation DRY_RUN=true")
    else:
        confluence.create_page(
            space=CONFLUENCE_SPACE_KEY,
            title=page_title,
            body=page_content,
            parent_id=CONFLUENCE_PARENT_PAGE_ID,
            representation='wiki',
        )

        print("Page created successfully.")
except Exception as e:
    print(f"Error: {e}")
    print(f"Response content: {e.response.text}")
