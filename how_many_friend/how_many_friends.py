
users = [
    {"id": 0, "name": 'Zero'},
    {"id": 1, "name": 'One'},
    {"id": 2, "name": 'Two'},
    {"id": 3, "name": 'Three'},
    {"id": 4, "name": 'Four'},
    {"id": 5, "name": 'Five'},
    {"id": 6, "name": 'Six'},
    {"id": 7, "name": 'Seven'},
    {"id": 8, "name": 'Eight'},
    {"id": 9, "name": 'Nine'},
]

friendships_pairs = [ (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendship = {user['id']: [] for user in users}

for i, j in friendships_pairs:
    friendship[i].append(j)
    friendship[j].append(i)

def number_of_friends(user):
    return len(friendship[user['id']])

total_friends = sum(number_of_friends(user) for user in users)
total_users = len(users)
avg_friend = total_friends / total_users

how_many_friends = [(user["id"], number_of_friends(user)) for user in users]
how_many_friends.sort(key = lambda number_of_friends: number_of_friends[1], reverse = True)


print(how_many_friends)
print("AVG = ", avg_friend)

