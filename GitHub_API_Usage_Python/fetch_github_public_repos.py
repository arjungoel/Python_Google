import base64
from github import Github
from pprint import pprint

username = input("Enter the username:")
g = Github()
user = g.get_user(username) 

# To loop around all the public repos a github user has
for repo in user.get_repos():
    print(repo)