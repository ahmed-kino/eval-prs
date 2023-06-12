import os
from dotenv import load_dotenv


from src.extractor import Extractor
from src.evalate import Evaluate
from src.github_client import GithubClient
from src.openai_client import OpenAIClient


def main():
    load_dotenv()

    # extract commits from github api
    GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
    OWNER = os.getenv("OWNER")
    REPO = os.getenv("REPO")
    AUTHOR = os.getenv("AUTHOR")
    github_client = GithubClient(
        github_api_key=GITHUB_API_KEY, owner=OWNER, repo=REPO, author=AUTHOR
    )
    extractor = Extractor(client=github_client)
    extractor.run()


if __name__ == "__main__":
    main()
