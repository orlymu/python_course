from unittest import TestCase
from qa5_objects.Student_1 import Student_1


class TestStudent_1(TestCase):
    def setUp(self):
        self.student = Student_1(12,"abc")

    def test_add_grade(self):
        self.student.add_grade("english",90)
        self.assertEqual(self.student.subjects_grades["english"],90)
