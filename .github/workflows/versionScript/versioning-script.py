import subprocess
import json
import os
import sys

if len(sys.argv) < 2:
    print("Please Pass the Organization/repo name During running the script!")
    sys.exit(1)

repo_name = sys.argv[1]

# Get the current STAGEVERSION using GitHub CLI and parse it
gh_command = ["gh", "api", f"repos/{repo_name}/actions/variables/STAGEVERSION", "--method", "GET"]
result = subprocess.run(gh_command, capture_output=True, text=True, check=True)
stage_version = json.loads(result.stdout)["value"]

print("Old Version is :",stage_version)
stage_version=stage_version.split("-")[1]
# Remove the 'v' prefix from the version string
version = stage_version.lstrip('v')

# Split version into parts
version_parts = list(map(int, version.split('.')))
patch_version = version_parts[2] + 1

# Construct the new version string
new_version = f"v{version_parts[0]}.{version_parts[1]}.{patch_version}"

updated_version = f"stage-{new_version}"
print("New Version is: ", updated_version)


update_command = [
    "gh", "api", "-X", "PATCH",
    f"repos/{repo_name}/actions/variables/STAGEVERSION",
    "-f", f"value={updated_version}"
]

result = subprocess.run(update_command)
