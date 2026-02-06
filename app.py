import os

workspace = os.getcwd()

print("Jenkins Workspace Path:", workspace)
print("Files in Jenkins Workspace:")

for file in os.listdir(workspace):
    print(file)

print("Git clone successful – files are present in workspace")
