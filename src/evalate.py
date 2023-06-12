from src.runner import Runner


class Evaluate(Runner):
    def run(self):
        data = self.load_file("data/data.json")

        commits_with_evaluation = []

        self.logger.info("Evaluating commits")
        for commit in data:
            self.logger.info(f"Evaluate commit: {commit}")
            json_agent_executor = self.client.json_agent_executor(commit)
            first_answer = json_agent_executor.run(
                "Review the following code 'in the commit' and check wether it has been written in modern programming standards and formatting. provide me with yes or no answer"
            )
            second_answer = json_agent_executor.run(
                "Review the following code 'in the commit' for any logical or security concerns. provide only a number on a scale of 1 to 10 based on your findings"
            )
            commits_with_evaluation.append(
                self._save_results(commit, first_answer, second_answer)
            )

        self.write_to_json_file("data/results.json", commits_with_evaluation)

    def _save_results(self, commit, first_answer, second_answer):
        points = 10 if first_answer == "Yes" else 0
        points += int(second_answer)
        return dict(
            sha=commit.get("sha"), html_url=commit.get("html_url"), points=points
        )
