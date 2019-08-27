from copy import deepcopy
from random import choice, choices, shuffle
from os import system
import getch


def main():
    print('(Q)uestion or (T)erms?', end=' ')
    quiz_type = getch.getche()
    num_terms = 4  # len(term_dict)

    if quiz_type.lower() == 't':
        print('\n(Q)uestion or (A)nswer mode?', end=' ')
        term_mode = getch.getche()
        term_dict = load_terms()
        do_term_quiz_with_hints(term_dict, num_terms, term_mode == 'a')
    else:
        questions_dict = load_questions()
        do_question_quiz(questions_dict, num_terms)


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


def do_question_quiz(dict, num_terms, answer_mode = False):
    questions_dict = deepcopy(dict)
    success_count, failure_count = 0, 0
    failure_dict = {}

    for i in range(num_terms):
        system('clear')
        print('Questions Quiz ({count}/{total})\n'.format(count=(i + 1), total=num_terms))
        q = choice(list(questions_dict.keys()))
        answer = questions_dict.pop(q)
        print("{question} ".format(question=q), end=' ')
        getch.getch()

        print("\n\n{value}".format(value=answer))
        print("did you get it right? ", end=' ')
        input_value = getch.getch()
        if input_value.lower() == 'y':
            success_count = success_count + 1
            # msg = "Correct!"
        else:
            # input("whoops!  correct answer was \n {answer}".format(answer=answer))
            failure_count = failure_count + 1
            failure_dict[q] = answer
        # input("{msg} ".format(msg=msg))

    report_results(success_count, failure_count, failure_dict)

    return success_count, failure_count, failure_dict


def report_results(success_count, failure_count, failure_dict):
    system('clear')
    print("Quizzing Complete:\n{right} right, {wrong} wrong\n".format(right=success_count, wrong=failure_count))
    if failure_count > 0:
        print('You missed\n')
        for key in failure_dict.keys():
            print("\t*** {key}\n{answer}".format(key=key, answer=failure_dict[key]))


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


def do_term_quiz_with_hints(dict, num_terms, answer_mode=False):
    success_count, failure_count = 0, 0
    failure_dict = {}

    if answer_mode:
        # reverse the dictionary
        term_dict = {}
        for (k,v) in dict.items():
            term_dict[v] = k
    else:
        term_dict = deepcopy(dict)

    all_answers = list(term_dict.values())

    for i in range(num_terms):
        system('clear')
        print('Terminology Quiz ({count}/{total})\n'.format(count=(i + 1), total=num_terms))

        # pick a random term
        term = choice(list(term_dict.keys()))
        answer = term_dict.pop(term)
        if answer_mode:
            print("what term represents:\n\t{key}? ".format(key=term))
        else:
            print("what is the definition of {key}? ".format(key=term))
        getch.getch()

        num_hints = 4
        possible_answers, correct_answer = build_possible_answers(all_answers, answer, num_hints)

        for index in range(len(possible_answers)):
            ans = possible_answers[index]
            if ans.strip() == '':
                ans = '[undefined]'
            print("{offset}): {value}".format(offset=(index + 1), value=ans))

        print("Answer? (1-{num_answers}) ".format(num_answers=(num_hints + 1)), end=' ')
        input_value = getch.getche()
        if int(input_value) == correct_answer:
            success_count = success_count + 1
            # msg = "Correct!"
        else:
            msg = "whoops!  correct answer was \n{num}): {answer}".format(num=correct_answer,answer=answer)
            failure_count = failure_count + 1
            failure_dict[term] = answer
            print("{msg} ".format(msg=msg))
            getch.getch()

    report_results(success_count, failure_count, failure_dict)

    return success_count, failure_count, failure_dict


if __name__ == '__main__':
    main()