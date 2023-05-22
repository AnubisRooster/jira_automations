# jira-automation

## Getting started

### Run jira sprint summary in confluence automation

1. Get a token from jira to be used in your local execution in https://id.atlassian.com/manage-profile/security/api-tokens and add it to .jira_auth
```
$ echo "YOUR_TOKEN" > .jira_auth
```

2. Install necessary python dependencies (you can skip this step if you have docker available in your environment - check the next step)
```
$ pip install -r pip-requirements.txt
```

2. (alternative) Use docker to avoid python env and dependencies installation
```
$ make shell
```

3. Source necessary environment variables
```
$ source scripts/dev-jira-auth.sh
```

4. Run script manually
```
$ ./scripts/sprint-report-confluence.py
```

5. Confirm page got created in confluence. Without touching
   scripts/dev-jira-auth.sh the consumed sprint will be a Psyduck one and a page
   is created in the CLOUDINFRA confluence space
