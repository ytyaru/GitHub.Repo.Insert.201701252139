from github import GitHub
import json

username = "github_username"
db_path_account = "C:/GitHub.Accounts.sqlite3"
db_path_api = "C:/GitHub.Apis.sqlite3"
db_path_repo = "C:/GitHub.Repositories.{0}.sqlite3".format(username)

g = GitHub.GitHub(db_path_account, db_path_api, db_path_repo, username)
res = g.db.update_local_db()
print(len(res))
