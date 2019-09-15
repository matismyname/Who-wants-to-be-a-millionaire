from question_class import *

def questions(bool_eng):
    questions_and_answers_dict = {
        "Test question" : "Test answer"
    }

    list_of_false_answer = [
        [
            "False 1", "False 2", "False 3"
        ],
        [
            "Hm"
        ]
    ]

    i = 0
    for key, value in questions_and_answers_dict.items():
        question_class(bool_eng,
        key,
        value,
        list_of_false_answer[i][0],
        list_of_false_answer[i][1],
        list_of_false_answer[i][2]).start()