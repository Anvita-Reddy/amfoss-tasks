### Sir Perceval's Quest
It was a little confusing using perceval for the first time. I hit a few bumps in the process, but after going through the resources available on the internet, I finally was able to implement it in python.
###### https://chaoss.github.io/grimoirelab-tutorial/perceval/git.html
###### https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
###### https://docs.github.com/en/free-pro-team@latest/rest/reference/repos

Using Postman was very helpful in understanding how sending requests to GitHub API works. I used 'requests' module and implemented the script in python. Firstly, gathered all the repository data from amfoss organization. Iterated over each repository, finally using perceval.backends.core.git fetched all commits from each repository and dumped it in the commits.json file.
