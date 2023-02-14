from collections import defaultdict
# Зарплаты и стаж
salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2),
]

# Зарплата в зависимости от стажа
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# print(salary_by_tenure.items())
# [(8.7, [83000]), (8.1, [88000]), (0.7, [48000]), (6, [76000]), (6.5, [69000]), (7.5, [76000]), (2.5, [60000]), (10, [83000]), (1.9, [48000]), (4.2, [63000])]


# Создание групп в зависимости от стажа работы
def groups_by_tenures(tenure):
    if tenure < 2:
        return "Стаж менее 2 лет"
    elif tenure < 5:
        return "Стаж от 2 до 5 лет"
    else:
        return "Стаж более 5 лет"
salary_by_tenure_groups = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure_groups[groups_by_tenures(tenure)].append(salary)
# print(salary_by_tenure_groups)
# {'Стаж более 5 лет': [83000, 88000, 76000, 69000, 76000, 83000], 'Стаж менее 2 лет': [48000, 48000], 'Стаж от 2 до 5 лет': [60000, 63000]}


# Средняя арифметическая зарплата по каждой группе
average_salaries_by_tenure = {
    tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure_groups.items()
}
# print(average_salaries_by_tenure)
# {'Стаж более 5 лет': 79166.66666666667, 'Стаж менее 2 лет': 48000.0, 'Стаж от 2 до 5 лет': 61500.0}