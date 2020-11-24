import requests
from perceval.backends.core.git import Git
import json

def extract_commits(name,url):
      
      repo_url=url+".git"

      repo_dir="/tmp/"+name+".git"

      repo=Git(uri=repo_url,gitpath=repo_dir)

      for commit in repo.fetch():
            
            with open("task-8/commits.json","a") as outfile:
              json.dump(commit,outfile)

url = "https://api.github.com/orgs/amfoss/repos"

payload={}
headers = {
  'Authorization': 'Bearer bb01ceb41a25135d54dd61c67dc52df2b5afaf66'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_obj=json.dumps(response.json(),indent=4)
with open('task-8/repo_data.json','w') as outfile:
    outfile.write(json_obj)

with open('task-8/repo_data.json') as json_file:
    data=json.load(json_file)
    print("amfoss Organization Repositories:")
    for i in data:
        print("Repo name : ",i['name'])
        print("Repo url : ",i['html_url'])
        extract_commits(i['name'],i['html_url'])

print("Dumping commits done.")