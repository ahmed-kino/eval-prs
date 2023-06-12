from src.runner import Runner


class Extractor(Runner):
    def run(self):
        self.logger.info(
            f"Extracting commits for user {self.client.author} in {self.client.owner}/{self.client.repo} repo..."
        )
        commits = self.client.get_commits()

        sha_set = set()
        self.logger.info("Getting list of commit sha only...")
        for commit in commits:
            sha_set.add(commit["sha"])

        commit_list = []
        self.logger.info("Processing shas started...")
        for sha in sha_set:
            commit_details = self.client.get_commit_details(sha)

            self.logger.info(
                f"Extract files changes and commit messages from {sha[:5]}..."
            )
            files = [
                dict(filename=file["filename"], patch=file["patch"])
                for file in commit_details["files"]
            ]

            commit_list.append(
                dict(
                    sha=sha,
                    commit_message=commit_details["commit"]["message"],
                    html_url=commit_details["html_url"],
                    files=files,
                )
            )
            self.logger.prompt("---------------------")
        self.logger.info("Processing shas finished.")

        self.logger.info("uploading data to data.json")

        self.write_to_json_file("data/data.json", commit_list)
