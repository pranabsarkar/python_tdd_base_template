import os

command_list = [
    "pytest ./tests",
    "flake8 ./src ./tests --count --max-complexity=10 --max-line-length=127 --statistics"
]

for command in command_list:
    os.system(command)