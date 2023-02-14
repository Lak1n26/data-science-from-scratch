# Все пользователи
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
# Дружеские отношения
friendships_pairs = [ (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendship = {user['id']: [] for user in users}
# Для каждого пользователя определен список его друзей
for i, j in friendships_pairs:
    friendship[i].append(j)
    friendship[j].append(i)

# Определяем количество друзей у пользователя
def number_of_friends(user):
    return len(friendship[user['id']])

# print('У пользователя ' + str(users[0]['name']) + ' количество друзей = ' + str(number_of_friends(users[0])) )
# У пользователя Zero количество друзей = 2

total_friends = sum(number_of_friends(user) for user in users) # Суммарное число связей
total_users = len(users) # Всего пользователей
avg_friend = total_friends / total_users # Среднее число друзей

# print("Среднее число друзей в графе = ", avg_friend)
# Среднее число друзей в графе =  2.4

# Создать список в формате (id пользователя, количество друзей) и отсортировать по количеству друзей в убывающем порядке
how_many_friends = [(user["id"], number_of_friends(user)) for user in users]
how_many_friends.sort(key = lambda number_of_friends: number_of_friends[1], reverse = True)
# print(how_many_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


# Рекомендация новых друзей относительно друзей моих друзей
def friends_of_friends(user):
    friends_of_friend = []
    for friends in friendship[user['id']]:
        for friend in friendship[friends]:
            if friend != user['id'] and friend not in friendship[user['id']] and friend not in friends_of_friend:
                friends_of_friend.append(friend)
    friends_of_friend.sort()
    return user['name'] + ' (' + str(user['id']) + ')'+ ' стоит подружиться с ' + str(friends_of_friend)

# print(friends_of_friends(users[0]))
# Zero (0) стоит подружиться с [3]
# print(friends_of_friends(users[4]))
# Four (4) стоит подружиться с [1, 2, 6, 7]

# Интересы пользователей
# (id пользователя, интерес)
interests = [
    (0,"Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"), (7, "machine learning"),
    (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

users_by_interests = {}
for id, interest in interests:
    if interest not in users_by_interests:
        users_by_interests[interest] = [id]
    else:
        users_by_interests[interest] += [id]
# print(users_by_interests)
# {'Hadoop': [0, 9], 'Big Data': [0, 8, 9], 'HBase': [0, 1], 'Java': [0, 5, 9], 'Spark': [0], 'Storm': [0], 'Cassandra': [0, 1], 'NoSQL': [1], 'MongoDB': [1], 'Postgres': [1], 'Python': [2, 3, 5], 'scikit-learn': [2, 7], 'scipy': [2], 'numpy': [2], 'statsmodels': [2], 'pandas': [2], 'R': [3, 5], 'statistics': [3, 6], 'regression': [3, 4], 'probability': [3, 6], 'machine learning': [4, 7], 'decision trees': [4], 'libsvm': [4], 'C++': [5], 'Haskell': [5], 'programming languages': [5], 'mathematics': [6], 'theory': [6], 'Mahout': [7], 'neural networks': [7, 8], 'deep learning': [8], 'artificial intelligence': [8], 'MapReduce': [9]}

interests_by_users = {}
for id, interest in interests:
    if id not in interests_by_users:
        interests_by_users[id] = [interest]
    else:
        interests_by_users[id] += [interest]
# print(interests_by_users)
# {0: ['Hadoop', 'Big Data', 'HBase', 'Java', 'Spark', 'Storm', 'Cassandra'], 1: ['NoSQL', 'MongoDB', 'Cassandra', 'HBase', 'Postgres'], 2: ['Python', 'scikit-learn', 'scipy', 'numpy', 'statsmodels', 'pandas'], 3: ['R', 'Python', 'statistics', 'regression', 'probability'], 4: ['machine learning', 'regression', 'decision trees', 'libsvm'], 5: ['Python', 'R', 'Java', 'C++', 'Haskell', 'programming languages'], 6: ['statistics', 'probability', 'mathematics', 'theory'], 7: ['machine learning', 'scikit-learn', 'Mahout', 'neural networks'], 8: ['neural networks', 'deep learning', 'Big Data', 'artificial intelligence'], 9: ['Hadoop', 'Java', 'MapReduce', 'Big Data']}

from collections import Counter
def recommendant_friend_by_interests(target_user):
    same_interests = Counter (user for interest in interests_by_users[target_user['id']] for user in users_by_interests[interest] if user != target_user['id'])
    # возвращает список в формате (id пользователя, количество общих интересов)
    return same_interests.most_common()

# print(recommendant_friend_by_interests(users[0]))
# [(9, 3), (1, 2), (8, 1), (5, 1)]
# Следовательно, по интересам пользователю 0 подходит больше всего пользователь 9.
# У них 3 общих интереса - Hadoop, Big Data и Java.

