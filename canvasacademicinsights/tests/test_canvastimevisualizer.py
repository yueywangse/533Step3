import unittest
from unittest.mock import patch, MagicMock
import datetime
from canvasacademicinsights.canvasvisualizer import canvastimevisualization as tv


class TestTimeVisuals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
            cls.grade_meta_data =[{
                'html_url': 'https://canvas.ubc.ca/courses/174247/grades/2650436',
                'current_grade': None,
                'current_score': None,
                'final_grade': None,
                'final_score': 10.0,
            }]
            cls.assesments = []

    def setUp(self):
        self.testData = [["courseid","coursename", self.grade_meta_data, self.assesments] for j in range(5)] 

    def tearDown(self):
        self.testData = None
        print("tearDown: Finished a test.")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass: All tests done")

    def test_get_last_graded_items_normal(self):
        class FakeAssignment:
            def __init__(self, score, total, date):
                self.score = score
                self.total = total
                self.date = date
            def isAssignment(self): return True
            def isQuiz(self): return False

        class FakeQuiz:
            def __init__(self, score, total, date=None):
                self.score = score
                self.total = total
                self.date = date
            def isAssignment(self): return False
            def isQuiz(self): return True

        a1 = FakeAssignment(9, 10, "2025-01-01")
        a2 = FakeAssignment(5, 5,  "2025-02-01")
        q1 = FakeQuiz(8, 10, "2025-01-10")
        q2 = FakeQuiz(7, 10, "2025-02-05")
        self.testData[0][3] = [a1, a2, q1, q2]

        visualizer = tv.CanvasTimeVisualization(self.testData)
        last_a, last_q = visualizer.get_last_graded_items()

        self.assertIs(last_a, a2)  
        self.assertIs(last_q, q2)  
        self.assertEqual(last_a.date, "2025-02-01")
        self.assertEqual(last_q.date, "2025-02-05")

    @patch("canvasacademicinsights.canvasvisualizer.canvastimevisualization.plt")
    def test_plot_weekly_average_score_heatmap(self, mock_plt):
        class FakeGradeItem:
            def __init__(self, score, total, date):
                self.score = score
                self.total = total
                self.date = date

        self.testData[0][3] = [
            FakeGradeItem(18, 20, datetime.date(2025, 1, 10)), 
            FakeGradeItem(24, 26, datetime.date(2025, 1, 12)), 
        ] 
        self.testData[1][3] = [
            FakeGradeItem(18, 20, datetime.date(2025, 1, 17)), 
            FakeGradeItem(24, 26, datetime.date(2025, 1, 19)), 
        ]
        visualizer = tv.CanvasTimeVisualization(self.testData)
        visualizer.plot_weekly_average_score_heatmap()

        mock_plt.figure.assert_called_once_with(figsize=(14, 6))
        mock_plt.xlabel.assert_called_once_with("Week")
        mock_plt.ylabel.assert_called_once_with("Course")
        mock_plt.title.assert_called_once_with("Weekly average percentage score by course")
        self.assertTrue(mock_plt.imshow.called)
        self.assertTrue(mock_plt.colorbar.called)
        self.assertTrue(mock_plt.tight_layout.called)
        self.assertTrue(mock_plt.show.called)

    @patch("canvasacademicinsights.canvasvisualizer.canvastimevisualization.plt")
    def test_plot_item_scores(self, mock_plt):
        class FakeAssignment:
            def __init__(self, score, total, date):
                self.score = score
                self.total = total
                self.date = date
            def isAssignment(self): return True
            def isQuiz(self): return False
        class FakeQuiz:
            def __init__(self, score, total, date=None):
                self.score = score
                self.total = total
                self.date = date
            def isAssignment(self): return False
            def isQuiz(self): return True


        self.testData[0][3] = [
            FakeAssignment(8, 10, datetime.date(2025, 1, 2)), 
            FakeAssignment(5, 5,  datetime.date(2025, 1, 1)), 
            FakeQuiz(15, 20,  datetime.date(2025, 1, 3)),  
        ]
        mock_fig = MagicMock()
        mock_ax_assign = MagicMock()
        mock_ax_quiz = MagicMock()
        mock_plt.subplots.return_value = (mock_fig, (mock_ax_assign, mock_ax_quiz))
        visualizer = tv.CanvasTimeVisualization(self.testData)
        visualizer.plot_item_scores(course_index=0)
        
        mock_plt.subplots.assert_called_once_with(2, 1, figsize=(10, 8))
        self.assertEqual(mock_ax_assign.plot.call_count, 1)
        self.assertEqual(mock_ax_quiz.plot.call_count, 1)
        mock_ax_assign.set_ylim.assert_called_once_with(0, 110)
        mock_ax_quiz.set_ylim.assert_called_once_with(0, 110)
        mock_ax_assign.set_ylabel.assert_called_once_with("Score (%)")
        mock_ax_quiz.set_xlabel.assert_called_once_with("Quiz number")
        mock_ax_assign.set_xticks.assert_called_once()
        mock_ax_quiz.set_set_title("Quizzes")
        mock_fig.tight_layout.assert_called_once()
        self.assertTrue(mock_plt.show.called)




    @patch("canvasacademicinsights.canvasvisualizer.canvastimevisualization.plt")
    def test_plot_all_last_graded_items_bar(self, mock_plt):
        class FakeAssignment:
            def __init__(self, score, total, date):
                self.score = score
                self.total = total
                self.date = date

        visualizer = tv.CanvasTimeVisualization(self.testData)

        self.testData[0][3] = [FakeAssignment(8, 10, datetime.date(2025, 1, 2))]

        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_plt.subplots.return_value = (mock_fig, mock_ax)
        visualizer.plot_all_last_graded_items_bar()

        mock_plt.subplots.assert_called_once_with(figsize=(14, 6))
        self.assertTrue(mock_plt.show.called)
        self.assertEqual(len(mock_ax.bar.call_args_list), 2)
        mock_ax.set_ylabel.assert_called_once_with("Score (%)")
        mock_ax.set_ylim.assert_called_once_with(0, 110)
        mock_ax.set_title.assert_called_once_with(
            "Last graded assignment and quiz across all courses"
        )
        mock_fig.tight_layout.assert_called_once()
        self.assertTrue(mock_plt.show.called)
