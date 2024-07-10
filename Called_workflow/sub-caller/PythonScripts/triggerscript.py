import os 
import sys
import requests

TOKEN = str(sys.argv[1])
OWNER = str(sys.argv[2])
REPO = str(sys.argv[3])
workflow_name = str(sys.argv[4])
link_repository = str(sys.argv[5])


def trigger_workflow(token, git_account, repository,
                     workflow_name, link_repository):
    headers = {
        "Accept" : "application/vnd.github.v3+json",
        "Authorization" : f"token {token}"
    }

    data = {
        "event_type" : workflow_name,
        "client_payload": {
            "git_akun": git_account,
            "repository": repository,
            "link_repository": link_repository,
            "tree_repository": "sub-caller",
            "link_tree_repository": "git@github.com:mohammadfikrinursyahbani/sub-caller.git"
        }
    }

    responseValue = requests.post(
        f"https://api.github.com/repos/{git_account}/{repository}/dispatches", 
        headers=headers, json=data
    )
    print(responseValue.content)

trigger_workflow(TOKEN, OWNER, REPO, workflow_name, link_repository)
