import requests 
import random
import html
CATEGORY_ID = 17
URL = f"https://opentdb.com/api.php?amount=10&category={CATEGORY_ID}&type=multiple"
def get_questions() :
    response = requests.get(URL)
    if response.status_code == 200 : 
        data = response.json()
        if data['response_code'] == 0 and data['results'] :
            return data['results']
        return None
def run_quiz() :
    ques = get_questions()
    if not ques :
        print('Failed to retrieve questions')
        return
    score = 0
    print("Welcome to trivia time !")
    #print(ques)
    for i, q in enumerate(ques, 1) :
        que = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrect = [html.unescape(a) for a in q["incorrect_answers"]]
        options = incorrect + [correct]
        random.shuffle(options)
        print(f'Question {i} : {que}')
        for id, option in enumerate(options, 1) :
            print(f'  {id}.{option}')
        while True :
            try :
                choice = int(input('\nYour answer (1 - 4) : '))
                if 1<= choice <= 4 :
                    break
            except ValueError :
                pass
            print('Invalid input!')
        if options[choice - 1] == correct :
            print('Correct :)')
            score += 1
        else :
            print(f'Incorrect :(\nCorrect answer : {correct}')
    print(f'Final score : {score}/{len(ques)}')
    print(f'Percentage : {score/len(ques)*100:.1f}%')
if __name__ == '__main__' :
    run_quiz()