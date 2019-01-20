from github import Github
import sys

g = Github(sys.argv[1])

repo = g.get_user().get_repo("Github_SemaphoreCI")
print(repo)
commits = repo.get_commits()
c = commits[commits.totalCount - 1]
print(c.committer)
c.create_comment("Automatic comment")