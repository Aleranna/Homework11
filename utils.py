import json
from classes import Candidate


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    candidates_list = []
    for i in data:
        candidate = Candidate(i['id'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills'])
        candidates_list.append(candidate)
    return candidates_list


def get_candidate(candidate_id, path):
    """возвращает кандидата по его id"""
    data = load_candidates_from_json(path)
    for i in data:
        if i.id == candidate_id:
            return i


def get_candidates_by_name(candidate_name, path):
    """возвращает кандидатов по имени"""
    data = load_candidates_from_json(path)
    names = []
    for i in data:
        if candidate_name.lower() in i.name.lower():
            names.append(i)
    return names


def get_candidates_by_skill(skill_name, path):
    """возвращает кандидатов по скиллу"""
    data = load_candidates_from_json(path)
    has_skill = []
    for i in data:
        if skill_name.lower() in i.skills.lower():
            has_skill.append(i)
    return has_skill









