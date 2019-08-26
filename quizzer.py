from copy import deepcopy
from random import choice, choices, shuffle
from os import system


def load_questions():
    q_file = open("questions.txt")
    q_dict = {}
    for line in q_file:
        question = line.rstrip()

        answer = ''
        for answer_line in q_file:
            if answer_line.rstrip() == '':
                q_dict[question.lstrip('Q: ')] = answer.lstrip('A: ')
                # print("read line: {key} => {value}".format(key=question, value=answer))
                break
            answer = answer + answer_line
    q_file.close()
    return q_dict


def load_terms():
    term_file = open("terminology.txt")
    term_dict = {}
    for line in term_file:
        parts = line.split(":")
        term_dict[parts[0]] = parts[1].lstrip().rstrip()
        # print("read line: {key} => {value}".format(key=parts[0], value=term_dict[parts[0]]))
    term_file.close()
    return term_dict


def main():
    term_dict = load_terms()
    num_terms = 20  # len(term_dict)
    do_term_quiz_with_hints(term_dict, num_terms)

    # questions_dict = load_questions()
    # do_question_quiz(questions_dict, num_terms)


def do_question_quiz(questions_dict, num_terms, answer_mode = False):
    for i in range(num_terms):
        system('clear')
        print('Questions Quiz\n')
        q = choice(list(questions_dict.keys()))
        print("{key} ".format(key=q), end=" ")
        input_value = input()
        print("{value}".format(value=questions_dict[q]))
        input_value = input("did you get it right? ")


def do_term_quiz(term_dict):
    num_terms = 20  # len(term_dict)
    success_count, failure_count = 0, 0
    failure_dict = {}
    for i in range(num_terms):
        system('clear')
        print('Terminology Quiz ({count}/{total})\n'.format(count=(i+1), total=num_terms))

        # pick a random term
        term = choice(list(term_dict.keys()))
        input("what is the definition of {key}? ".format(key=term))

        print("{value}\n".format(value=term_dict[term]))
        input_value = input("did you get it right? ")
        if input_value.lower() == 'y':
            success_count = success_count + 1
        else:
            failure_count = failure_count + 1
            failure_dict[term] = term_dict[term]
    print(failure_dict)
    input("{right} right, {wrong} wrong ".format(right=success_count, wrong=failure_count))

    return success_count, failure_count, failure_dict


def build_possible_answers(all_answers, answer, num_hints):
    answers = [answer]
    answers.extend(choices(all_answers, k=num_hints))
    shuffle(answers)

    return answers, answers.index(answer) + 1


def do_term_quiz_with_hints(dict, num_terms):
    term_dict = deepcopy(dict)
    all_answers = list(load_terms().values())
    success_count, failure_count = 0, 0
    failure_dict = {}

    for i in range(num_terms):
        system('clear')
        print('Terminology Quiz ({count}/{total})\n'.format(count=(i + 1), total=num_terms))

        # pick a random term
        term = choice(list(term_dict.keys()))
        answer = term_dict.pop(term)
        input("what is the definition of {key}? ".format(key=term))

        num_hints = 4
        possible_answers, correct_answer = build_possible_answers(all_answers, answer, num_hints)

        for index in range(len(possible_answers)):
            ans = possible_answers[index]
            if ans.strip() == '':
                ans = '[undefined]'
            print("{offset}): {value}".format(offset=(index + 1), value=ans))

        input_value = input("Answer? (1-{num_answers}) ".format(num_answers=(num_hints + 1)))
        if int(input_value) == correct_answer:
            success_count = success_count + 1
            msg = "Correct!"
        else:
            msg = "whoops!  correct answer was \n{num}): {answer}".format(num=correct_answer,answer=answer)
            failure_count = failure_count + 1
            failure_dict[term] = answer
        input("{msg} ".format(msg=msg))

    system('clear')
    print("Quizzing Complete:\n{right} right, {wrong} wrong\n".format(right=success_count, wrong=failure_count))
    if failure_count > 0:
        print('You missed\n')
        for key in failure_dict.keys():
            print("\t{key}): {answer}".format(key=key, answer=failure_dict[key]))

    return success_count, failure_count, failure_dict


if __name__ == '__main__':
    main()