#!/usr/bin/env python3

import sys
import requests
import json

def get_repo():
    while 1:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break

        ORG_NAME = line.split('/')[0]
        REPO_NAME = line.split('/')[1]

        URL = ('https://api.github.com/repos/%s/%s' % (ORG_NAME, REPO_NAME)).strip()
        URL_COMMIT = URL + '/commits'

        response = requests.get(URL)
        commits = requests.get(URL_COMMIT)

        if response.status_code == 200:
            repo_inf = json.loads(response.text)
            commit_inf = json.loads(commits.text)
            print('%s, %s, %s, %s' %(repo_inf['name'], repo_inf['clone_url'], commit_inf[0]['commit']['author']['name'],
                                     commit_inf[0]['commit']['author']['date']))

        elif response.headers['X-RateLimit-Remaining'] == 0:
            print('Rate Limit exceeded, wait for some time')

        elif response.status_code == 404:
            print('Private Repo, Not authorized to make a call')

if __name__ == '__main__':
    '''
    HELP: This project does the following:
    
    - MAKE API request to github repo.
    - Accepts ORG name and REPO name from stdin 
    - Outputs name of repo, clone_url, latest_author_name, latest_commit_date in a comma separated as stdout
    
    To prevent the complexity of project, it is a python script that can be called simply and not an application
    
    All the dependencies are listed in requirements.txt
    '''

    get_repo()
