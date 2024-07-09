"""
Given a 2D array of user IDs, find the number of friends a user has. Note that users can have none or multiple friends.
"""
def count_friends(user_ids):
    cnt = {}
    for row in user_ids:
        for user in row:
            if user in cnt.keys():
                cnt[user]+=1
            else:
                cnt[user] = 1
    return cnt
