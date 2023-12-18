# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.

import json


def conduct_survey():
    questions = [
        "What is your name?",
        "How old are u?",
        "What is you surname?"
    ]

    answers = {}

    for question in questions:
        answers[question] = input(question + " ")

    return answers


def save_answers(answers, filename='survey.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(answers)

    with open(filename, 'w') as file:
        json.dump(data, file)


answers = conduct_survey()
save_answers(answers)
