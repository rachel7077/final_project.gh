from tkinter import messagebox
import unittest
import trivia_game as tg

class QuestionTest(unittest.TestCase):

    @staticmethod
    def mkQ(title, question, answer):
        return tg.Question(title, question, answer)
    
    def test_constructor(self):
        q1 = QuestionTest.mkQ('Frozen', 'Who likes warm hugs and loves the idea of summer?', 'Olaf')
        self.assertEqual(q1.question, 'Who likes warm hugs and loves the idea of summer?')
        self.assertEqual(q1.answer, 'Olaf')
        self.assertEqual(q1.title, 'Frozen')

    def test_compare_answer(self):
        q1 = QuestionTest.mkQ('Frozen', 'Who likes warm hugs and loves the idea of summer?', 'Olaf')
        self.assertEqual(q1.compare_answer('Olaf'), True)
        self.assertEqual(q1.compare_answer('Elsa'), False)

class MultipleChoiceTest(unittest.TestCase):
    @staticmethod
    def mkQ(title, question, answer, choices):
        return tg.MultipleChoice(title, question, answer, choices)
    
    def test_constructor(self):
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        self.assertEqual(q2.question, 'How many brothers does Prince Hans have?')
        self.assertEqual(q2.answer, 'c')
        self.assertEqual(q2.title, 'Frozen')
        self.assertEqual(q2.choices, {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})

    def test_compare_answer(self):
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        self.assertEqual(q2.compare_answer('c'), True)
        self.assertEqual(q2.compare_answer('a'), False)
        self.assertEqual(q2.compare_answer('b'), False)
        self.assertEqual(q2.compare_answer('win'), 'incorrect entry')

class TrueOrFalseTest(unittest.TestCase):
    @staticmethod
    def mkQ(title, question, answer):
        return tg.TrueOrFalse(title, question, answer)
    
    def test_constructor(self):
        q3 = TrueOrFalseTest.mkQ('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True')
        self.assertEqual(q3.question, 'Flora dresses in red, Fauna in green, Merryweather in blue.')
        self.assertEqual(q3.answer, 'True')
        self.assertEqual(q3.title, 'Sleeping Beauty')

    def test_compare_answer(self):
        q3 = TrueOrFalseTest.mkQ('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True') 
        self.assertEqual(q3.compare_answer('True'), True)
        self.assertEqual(q3.compare_answer('true'), True)
        self.assertEqual(q3.compare_answer('t'), True)
        self.assertEqual(q3.compare_answer('False'), False)
        self.assertEqual(q3.compare_answer('f'), False)
        self.assertEqual(q3.compare_answer('false'), False)
        self.assertEqual(q3.compare_answer('w'), 'incorrect entry')

class QuizTest(unittest.TestCase):
    @staticmethod
    def mkQuiz():
        return tg.Quiz()

    def test_constructor(self):
        quiz = QuizTest.mkQuiz()
        self.assertEqual(quiz.lives, 3)
        self.assertEqual(quiz.points, 0)

    def test_add_question(self):
        quiz1 = QuizTest.mkQuiz()
        list = ['What time is it?']
        quiz1.add_question(list)
        self.assertEqual(quiz1.list_of_q, {type('str') : ['What time is it?']})

    def test_get_rand_quest(self):
        quiz2 = QuizTest.mkQuiz()
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        q3 = tg.TrueOrFalse('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True')
        quiz2.add_question([q2])
        quiz2.add_question([q3])
        self.assertEqual(quiz2.get_rand_quest('c'), 'try again')
        self.assertEqual(quiz2.get_rand_quest('b'), q3)
        self.assertEqual(quiz2.get_rand_quest('a'), q2)

    # cannot test users_answers because it is dependent on the input of the user and it produces graphics


# do i need tests for list_of_mc and list_of_tf?
# ask if variable naming is right format?
# cannot test ask_questions, leaderboard, or close because they create a gui

if __name__ == '__main__':
    unittest.main()
