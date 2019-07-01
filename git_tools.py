def commentGitPRUsingCurl(prnumber, comment):
    data = {'body': comment}
    user = 'your_git_account'
    token = 'your_git_token'
    repo_org = 'your_repo_org'
    repo = 'your_repo'
    url = 'https://api.github.com/' + f'repos/{repo_org}/{repo}/issues/' + str(prnumber) + '/comments'

    curlProcess = ["curl", "-i", "-H", f"Authorization: token {token}", "-X", "POST", url, '--data', json.dumps(data)]
    subprocess.run(curlProcess, stdout=subprocess.PIPE, check=True)
    
def commentGitPRUsingRequests(prnumber, comment):
    data = {'body': comment}
    user = 'your_git_account'
    token = 'your_git_token'
    repo_org = 'your_repo_org'
    repo = 'your_repo'
    url = 'https://api.github.com/' + f'repos/{repo_org}/{repo}/issues/' + str(prnumber) + '/comments'

    res = requests.post(url, auth=(user,token), data=json.dumps(data))
    

commentGitPRUsingCurl(12345, 'Congratz! your PR has passed the tests :tada:')
