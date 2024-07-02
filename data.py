NATIONALITY_FILE_PATH = "./nationalities.txt"
JOB_FILE_PATH = "./role.txt"
NATIONALITY_LIST = []
JOB_ROLE_LIST = []


# Get the data from NATIONALITY FILE PATH
with open(NATIONALITY_FILE_PATH) as file:
    content = file.read().splitlines()
    for nation in content:
        NATIONALITY_LIST.append(nation)

# Get the data from Job file path
with open(JOB_FILE_PATH) as file:
    content = file.read().splitlines()
    for job in content:
        JOB_ROLE_LIST.append(job)