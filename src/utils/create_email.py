def create_email(**max_point_value):
    return f"""
    Subject: Review of Commit {max_point_value.get("sha")}

    Dear {max_point_value.get("user")},

    I hope this email finds you well. I wanted to share some positive feedback regarding the recent commit {max_point_value.get("html_url")}. I have thoroughly reviewed both the commit message and the corresponding code changes, and I am pleased to inform you of the following findings:

    Well-Written Commit Message:
    The commit message associated with [Commit ID] is exemplary. It provides a clear and concise description of the changes made in the commit. The message accurately reflects the purpose and intention of the code modifications, making it easier for team members and future developers to understand the context of the changes at a glance. This demonstrates your commitment to maintaining good communication practices within the development process.

    Relevant Code Changes:
    Upon reviewing the code changes in the commit, I found that they align perfectly with the description provided in the commit message. The modifications made directly address the specific problem or feature mentioned in the message. This consistency between the commit message and the actual code changes is commendable, as it ensures that the development process remains transparent and well-documented.

    Your attention to detail in writing informative and meaningful commit messages greatly contributes to the overall clarity and effectiveness of the codebase. It facilitates collaboration among team members and enables a smoother understanding of the project's history.

    Best regards,

    GPT
    """
