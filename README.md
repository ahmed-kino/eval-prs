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

# Running Evaluate Prs

- Clone the repository: Run the following command `$ git clone git@github.com:ahmed-kino/eval-prs.git`

- Change directory: Run the following command `$ cd eval-prs`

- Copy `.env.example`: Run the following command `$ cp .env.example .env`

- Make sure to set all the environment variables right
```.env
GITHUB_API_KEY="<github api key>"
OWNER="<owner>"
AUTHOR="<author>"
REPO="<repo name>"
```
NOTE: If you don't know how to set up `GITHUB_API_KEY` please check this [link](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#about-personal-access-tokens)

## Run directly on you machine

- make sure you have [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/)

- Make sure you have python `virtualenv` setup. You can check this [link](https://docs.python.org/3/library/venv.html) on how to set virtualenv

- Run the following command `$ pip install -r requirements.txt`

- make sure you have `make` installed. You can check these links ([Ubuntu](https://askubuntu.com/questions/161104/how-do-i-install-make), [Windows](https://linuxhint.com/install-use-make-windows/), [MacOS](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac)) on how to install make

- Run the following command `$ make`


## Run with docker (to be done later)