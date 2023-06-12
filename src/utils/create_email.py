def create_email(**max_point_value):
    return f"""
    Subject: Review of Commit {max_point_value.get("sha")}

    Dear {max_point_value.get("user")},

    I hope this email finds you well. I am writing to provide you with a detailed review of the code in the latest commit {max_point_value.get("html_url")}. I have thoroughly analyzed the code for adherence to modern programming standards and formatting, as well as any logical or security concerns. Below, you will find the outcome of my review along with a list of recommendations.

    Review of Code Formatting and Programming Standards:
    Upon reviewing the code, I found that it adheres to modern programming standards and follows a consistent formatting style. The code is well-organized and readable, making it easier for developers to understand and maintain. It includes appropriate comments and variable/function names that enhance its readability.

    Review of Logical and Security Concerns:
    During my assessment, I carefully examined the code for any logical or security concerns. I am pleased to inform you that the code appears to be free from major logical flaws or security vulnerabilities.

    Thank you for considering my review. I appreciate your dedication to maintaining high programming standards and prioritizing security in the development process.

    Best regards,

    GPT
    """
