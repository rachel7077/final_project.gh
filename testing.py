from tkinter import messagebox
import unittest
import trivia_game as tg

class QuestionTest(unittest.TestCase):
    """ 
    Tests for the question class
    """
    @staticmethod
    def mkQ(title, question, answer):
        """
        Creates a question
        """
        return tg.Question(title, question, answer)
    
    def test_constructor(self):
        """
        Tests the question constructor
        """
        q1 = QuestionTest.mkQ('Frozen', 'Who likes warm hugs and loves the idea of summer?', 'Olaf')
        self.assertEqual(q1.question, 'Who likes warm hugs and loves the idea of summer?')
        self.assertEqual(q1.answer, 'Olaf')
        self.assertEqual(q1.title, 'Frozen')

    def test_compare_answer(self):
        """
        Tests the compare answer method in the question class
        """
        q1 = QuestionTest.mkQ('Frozen', 'Who likes warm hugs and loves the idea of summer?', 'Olaf')
        self.assertEqual(q1.compare_answer('Olaf'), True)
        self.assertEqual(q1.compare_answer('Elsa'), False)

class MultipleChoiceTest(unittest.TestCase):
    """
    Tests for the multiple choice question subclass
    """
    @staticmethod
    def mkQ(title, question, answer, choices):
        """
        Creates a multiple choice question
        """
        return tg.MultipleChoice(title, question, answer, choices)
    
    def test_constructor(self):
        """
        Tests the multiple choice question constructor
        """
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        self.assertEqual(q2.question, 'How many brothers does Prince Hans have?')
        self.assertEqual(q2.answer, 'c')
        self.assertEqual(q2.title, 'Frozen')
        self.assertEqual(q2.choices, {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})

    def test_compare_answer(self):
        """
        Tests the compare answer method in the multiple choice class
        """
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        self.assertEqual(q2.compare_answer('c'), True)
        self.assertEqual(q2.compare_answer('a'), False)
        self.assertEqual(q2.compare_answer('b'), False)
        self.assertEqual(q2.compare_answer('win'), 'incorrect entry')

class TrueOrFalseTest(unittest.TestCase):
    """
    Tests for the true or false question subclass
    """
    @staticmethod
    def mkQ(title, question, answer):
        """
        Creates a true or false question
        """
        return tg.TrueOrFalse(title, question, answer)
    
    def test_constructor(self):
        """
        Tests the true or false constructor
        """
        q3 = TrueOrFalseTest.mkQ('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True')
        self.assertEqual(q3.question, 'Flora dresses in red, Fauna in green, Merryweather in blue.')
        self.assertEqual(q3.answer, 'True')
        self.assertEqual(q3.title, 'Sleeping Beauty')

    def test_compare_answer(self):
        """
        Tests the compare answer method in the true or false class
        """
        q3 = TrueOrFalseTest.mkQ('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True') 
        self.assertEqual(q3.compare_answer('True'), True)
        self.assertEqual(q3.compare_answer('true'), True)
        self.assertEqual(q3.compare_answer('t'), True)
        self.assertEqual(q3.compare_answer('False'), False)
        self.assertEqual(q3.compare_answer('f'), False)
        self.assertEqual(q3.compare_answer('false'), False)
        self.assertEqual(q3.compare_answer('w'), 'incorrect entry')

class QuizTest(unittest.TestCase):
    """
    Tests for the quiz class
    """
    @staticmethod
    def mkQuiz():
        """
        Creates a quiz
        """
        return tg.Quiz()

    def test_constructor(self):
        """
        Tests the quiz class constructor
        """
        quiz = QuizTest.mkQuiz()
        self.assertEqual(quiz.lives, 3)
        self.assertEqual(quiz.points, 0)

    def test_add_question(self):
        """
        Tests the add question method in the quiz class
        """
        quiz1 = QuizTest.mkQuiz()
        list = ['What time is it?']
        quiz1.add_question(list)
        self.assertEqual(quiz1.list_of_q, {type('str') : ['What time is it?']})

    def test_get_rand_quest(self):
        """
        Tests the get random question in the quiz class
        """
        quiz2 = QuizTest.mkQuiz()
        q2 = MultipleChoiceTest.mkQ('Frozen', 'How many brothers does Prince Hans have?', 'c', {'a' : 'seven', 'b' : 'eleven', 'c' : 'twelve'})
        q3 = tg.TrueOrFalse('Sleeping Beauty', 'Flora dresses in red, Fauna in green, Merryweather in blue.', 'True')
        quiz2.add_question([q2])
        quiz2.add_question([q3])
        self.assertEqual(quiz2.get_rand_quest('c'), 'try again')
        self.assertEqual(quiz2.get_rand_quest('b'), q3)
        self.assertEqual(quiz2.get_rand_quest('a'), q2)

    # cannot test users_answers because it is dependent on the input of the user and it produces graphics

class AddQuestions(unittest.TestCase):
    """
    Tests for the list of questions functions
    """
    def test_list_of_mc(self):
        """
        Tests the function that creates a list of multiple 
        choice questions from a file
        """
        list_of_mc = tg.list_of_mc('multiple_choice.csv')
        first_q = list_of_mc[0]
        self.assertEqual(first_q.title, 'Tangled')
        self.assertEqual(first_q.question, "The magic of Rapunzel's hair is awoken by what")
        self.assertEqual(first_q.answer, 'c')
        self.assertEqual(first_q.choices, {'a' : 'Laughter', 'b' : 'Tears', 'c' : 'Song'})

    def test_list_of_tf(self):
        """
        Tests the function that creates a list of true
        or false questions from a file
        """
        list_of_tf = tg.list_of_tf('true_or_false.csv')
        first_q = list_of_tf[0]
        self.assertEqual(first_q.title, 'Aladdin')
        self.assertEqual(first_q.question, "Lago's feathers are red and yellow.")
        self.assertEqual(first_q.answer, 'FALSE')

# cannot test ask_questions, or leaderboard because they create a gui

if __name__ == '__main__':
    unittest.main()
