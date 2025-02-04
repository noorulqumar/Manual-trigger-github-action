import subprocess
import json

# Get the current STAGEVERSION using GitHub CLI and parse it
gh_command = ["gh", "api", "repos/noorulqumar/Manual-trigger-github-action/actions/variables/STAGEVERSION", "--method", "GET"]
result = subprocess.run(gh_command, capture_output=True, text=True)
stage_version = json.loads(result.stdout)["value"]

print(stage_version)
stage_version=stage_version.split("-")[1]
print(stage_version)
# Remove the 'v' prefix from the version string
version = stage_version.lstrip('v')

print(version)

# Split version into parts
version_parts = list(map(int, version.split('.')))
print(version_parts)
patch_version = version_parts[2] + 1

# Construct the new version string
new_version = f"v{version_parts[0]}.{version_parts[1]}.{patch_version}"
print(f"New version: {new_version}")

updated_version = f"vstage-{new_version}"
print(updated_version)


update_command = [
    "gh", "api", "-X", "PATCH",
    "repos/noorulqumar/Manual-trigger-github-action/actions/variables/STAGEVERSION",
    "-f", f"value={updated_version}"
]

result = subprocess.run(update_command)
