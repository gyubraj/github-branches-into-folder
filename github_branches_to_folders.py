import os
import subprocess
import time
import shutil

# replace url with your repo url
repo_url = "git@github.com:gyubraj/FastApi.git"
repo_name = repo_url.split("/")[-1].split(".")[0]

# Check if repo folder exists or not then delete folder if it exists
if os.path.exists(repo_name):
    shutil.rmtree(repo_name)

# Clone the repository
subprocess.call(["git", "clone", repo_url])

# Get a list of all branches
branches = subprocess.check_output(["git", "branch", "-a"], cwd=repo_name).decode().splitlines()

# Filter the list of branches to only include remote branches
remote_branches = [b.strip() for b in branches if "remotes/origin/" in b]

# Iterate over each remote branch
for branch in remote_branches:
    # Extract branch name 
    branch_name = branch.split("/")[-1]

    # Checkout to particular branch 
    command = f"cd {repo_name}; git checkout {branch_name};"

    subprocess.run(command, capture_output=True, shell=True)

    time.sleep(5)

    # remove folders with same name as git branch 
    if os.path.exists(branch_name):
        shutil.rmtree(branch_name)

    # command to create branch folder and move code into that folder
    content_copy_command = f"mkdir {branch_name}; cd {repo_name}; cp -R * ../{branch_name};"
    subprocess.run(content_copy_command, shell=True)

    # allow some time to copy files into new branch 
    time.sleep(5)

    # terminal notification 
    print(f"Branch {branch_name} copied to {branch_name} folder.")

# At last remove the main project as main branch is already copied to main folder
shutil.rmtree(repo_name)