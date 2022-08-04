import json


def load_candidates():
    """
    распаковываем файл с кандидатами
    """
    with open('candidates.json', 'rt', encoding='utf-8') as candidates_dict:
        data = json.load(candidates_dict)
    return data


def get_all():
    """
    получаем спискок всех кадидатов, формируем список сразу в формате вывода
    """
    candi_list = []
    for c in load_candidates():
        name = c['name']
        position = c['position']
        skills = c['skills']
        candi_list.append(f'Имя кандидата: {name}\n'
                          f'Позиция кандидата: {position}\n'
                          f'Навыки: {skills}\n\n')
    return candi_list


def get_by_pk(pk):
    """
    получаем кандидата по pk
    """
    for c in load_candidates():
        if c["pk"] == pk:
            photo = c['picture']
            name = c['name']
            position = c['position']
            skills = c['skills']

            return f'<img src="({photo})">\n<pre>\nИмя кандидата: {name}\nПозиция кандидата: {position}\nНавыки: {skills}\n</pre>'


def get_by_skill(skill_name):
    """
    отсеиваем кандидатов по скилу
    """
    need_skills = []
    for c in load_candidates():
        for s in c['skills'].split(', '):
            if s == skill_name.lower() or s == skill_name.title():
                name = c['name']
                position = c['position']
                skills = c['skills']
                need_skills.append(f'Имя кандидата: {name}\n'
                                   f'Позиция кандидата: {position}\n'
                                   f'Навыки: {skills}\n\n')
    return need_skills


# print(get_by_skill('python'))
