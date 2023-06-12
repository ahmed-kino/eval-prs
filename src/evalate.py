from src.runner import Runner
from src.utils.create_email import create_email


class Evaluate(Runner):
    def run(self):
        data = self.load_file("data/data.json")

        commits_with_evaluation = []

        self.logger.info("Evaluating commits")
        for commit in data:
            self.logger.info(f"Evaluate commit: {commit}")
            json_agent_executor = self.client.json_agent_executor(commit)
            try:
                first_answer = json_agent_executor.run(
                    "Review the following code 'in the commit' and check wether it has been written in modern programming standards and formatting. provide me with yes or no answer"
                )
            except Exception as e:
                self.logger.error(
                    f"Could Not process commit for the first answer REASON: {e}"
                )
                first_answer = "No"
            try:
                second_answer = json_agent_executor.run(
                    "Review the following code 'in the commit' for any logical or security concerns. provide only a number on a scale of 1 to 10 based on your findings"
                )
            except Exception as e:
                self.logger.error(
                    f"Could Not process commit for the second answer REASON: {e}"
                )
                second_answer = 0
            commits_with_evaluation.append(
                self._save_results(commit, first_answer, second_answer)
            )

        self.write_to_json_file("data/results.json", commits_with_evaluation)

        self._create_template()

    def _create_template(self):
        data = self.load_file("data/results.json")
        max_point_value = max(data, key=lambda x: x["points"])
        email_template = create_email(**max_point_value)
        user = max_point_value.get("user")
        self.write_to_file(f"template/email_to_{user}.txt", email_template)

    def _save_results(self, commit, first_answer, second_answer):
        points = 10 if first_answer == "Yes" else 0
        points += int(second_answer)
        return dict(
            sha=commit.get("sha"),
            user=commit.get("user"),
            html_url=commit.get("html_url"),
            points=points,
        )
