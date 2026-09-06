# Graph Report - jira_automations  (2026-09-06)

## Corpus Check
- Corpus is ~9,359 words - fits in a single context window. You may not need a graph.

## Summary
- 16 nodes · 12 edges · 4 communities (1 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- dev-jira-auth.sh
- graphify_pipeline.py

## God Nodes (most connected - your core abstractions)
1. `dev-jira-auth.sh script` - 1 edges
2. `JIRA_USERNAME` - 1 edges
3. `JIRA_PASSWORD` - 1 edges
4. `JIRA_BOARD_ID` - 1 edges
5. `CONFLUENCE_USERNAME` - 1 edges
6. `CONFLUENCE_PASSWORD` - 1 edges
7. `CONFLUENCE_SPACE_KEY` - 1 edges
8. `CONFLUENCE_PARENT_PAGE_ID` - 1 edges
9. `Self-contained graphify pipeline for CI. Builds a knowledge graph over this…` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 1 thin omitted)

### Community 0 - "dev-jira-auth.sh"
Cohesion: 0.22
Nodes (8): CONFLUENCE_PARENT_PAGE_ID, CONFLUENCE_PASSWORD, CONFLUENCE_SPACE_KEY, CONFLUENCE_USERNAME, JIRA_BOARD_ID, JIRA_PASSWORD, JIRA_USERNAME, dev-jira-auth.sh script

## Knowledge Gaps
- **8 isolated node(s):** `dev-jira-auth.sh script`, `JIRA_USERNAME`, `JIRA_PASSWORD`, `JIRA_BOARD_ID`, `CONFLUENCE_USERNAME` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 13 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `dev-jira-auth.sh script`, `JIRA_USERNAME`, `JIRA_PASSWORD` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._