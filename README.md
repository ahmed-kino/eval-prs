# Evaluate Prs

we need to pass the owner and the repo name in the prompt

## fetch commits for a certain user
- fetch all commits related to a user for a specific repo
- extract file changes and commit messages
- save the the extracted data into a file (could be a database)

## use langchain (GPT) to evaluate those commits

* the changes are relevant to the commit messages
* evaluate well written code based on:
    * Modernize and Add Best Practices: `Review the following code 'in the commit' and check wether it has been written in modern programming standards and formatting:`
    * Review for Logical Errors and Security Concerns: `Review your provided code 'in the commit' for any logical or security concerns and provide a list of recommendations.`

`NOTE: there might be lots of best practices for well implemented code but I've chosen these options only due to the limited time I have`

## create a template to show the use what is the best evaluation
