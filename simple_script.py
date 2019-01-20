from github import Github
import sys

g = Github(sys.argv[1])

repo = g.get_user().get_repo("Github_SemaphoreCI")
commits = repo.get_commits()
c = commits[0]
c.create_comment("Automatic comment")