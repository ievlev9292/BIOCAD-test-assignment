# Test problem for BIOCAD Data Science Trainee application
# Created by Free Fall
# May 2019


import pandas as pd

# Assume that each user has unique manager:

INPUT_FILENAME = "d1_managers.csv"
MANAGER_DEPTH = 8
OUTPUT_FILENAME = f"d1_managers_lev{MANAGER_DEPTH}.csv"

# read the data
people = pd.read_csv(INPUT_FILENAME)


## transform the data
users = {}
for index, row in people.iterrows():
    users[row['user']] = [row['manager_user']]

def deep_manager_onelev(users):
    """
    Go one level deeper into managing tree
    :param users: dictionary of user - managers pairs
    :return: nothing, works in-place
    """
    for user in users.keys():
        new_manager = users.get(users[user][-1])
        if new_manager:
            users[user].append(new_manager[0])


def deep_manager_nlev(n, users):
    """
    Go n levels deeper into managing tree
    :param n: needed increase of depth
    :param users: dictionary of user - managers pairs
    :return: nothing, works in-place
    """
    assert(n > 0)
    for i in range(n-1):
        deep_manager_onelev(users)


deep_manager_nlev(MANAGER_DEPTH, users)
all_users = []
all_managers = []
for user, managers in users.items():
    for manager in managers:
        all_users.append(user)
        all_managers.append(manager)


new_people = pd.DataFrame.from_dict({'user': all_users, 'MANAGER_USER': all_managers})
new_people.to_csv(OUTPUT_FILENAME, index=False)

print(f"All done! Data is written to {OUTPUT_FILENAME}.")

