import requests

from src.utils.logger import Logger


class GithubClient:
    def __init__(self, github_api_key, owner, repo, author):
        self.logger = Logger()
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {github_api_key}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        self.owner = owner
        self.repo = repo
        self.author = author

    def _get(self, url):
        try:
            return requests.get(url, headers=self.headers).json()
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")

    def get_commits(self):
        try:
            return self._get(f"{self.base_url}/repos/{self.owner}/{self.repo}/commits")
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")

    def get_commits_by_author(self):
        try:
            return self._get(
                f"{self.base_url}/repos/{self.owner}/{self.repo}/commits?q=author:{self.author}&per_page:10"
            )
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")

    def get_commit_details(self, sha):
        try:
            return self._get(
                f"{self.base_url}/repos/{self.owner}/{self.repo}/commits/{sha}"
            )
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")
