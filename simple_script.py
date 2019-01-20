from github import Github

# First create a Github instance:

# using username and password

# or using an access token
g = Github("token")

repo = g.get_user().get_repo("Github_SemaphoreCI")
print(repo)
commits = repo.get_commits()
c = commits[commits.totalCount - 1]
print(c.committer)
c.create_comment("Automatic comment")