from collections import defaultdict, namedtuple


# Python’s built-in dictionary type is wonderful for maintaining dynamic internal state over the lifetime of an object. By dynamic, I mean situations in which you need to do bookkeeping for an unexpected set of identifiers. For example, say that I want to record the grades of a set of students whose names aren’t known in advance. I can define a class to store the names in a dictionary instead of using a predefined attribute for each student
class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student('Patryk Klimowicz')
book.report_grade('Patryk Klimowicz', 86)
book.report_grade('Patryk Klimowicz', 96)
book.report_grade('Patryk Klimowicz', 66)
print(f'{book.average_grade("Patryk Klimowicz"):.2f}')


# Now we want to extend the SimpleGradebook class to keep a list of grades by subject, not just overall. We can do this by changing the _grades dictionary to map student names (its keys) to yet another dictionary (its values). The innermost dictionary will map subjects (its keys) to a list of grades (its values.) We'll use a defaultdict instance for the inner dictionary to handle missing subjects
class BySubjectsGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectsGradebook()
book.add_student('Patryk Klimowicz')
book.report_grade('Patryk Klimowicz', 'Math', 90)
book.report_grade('Patryk Klimowicz', 'Math', 92)
book.report_grade('Patryk Klimowicz', 'Gym', 100)
book.report_grade('Patryk Klimowicz', 'Gym', 95)
average = book.average_grade('Patryk Klimowicz')
print(f'{average:.2f}')


# Now we want to track the weight of each score toward the overall grade in the class so that midterm and final exams are more important than pop quizzes. One way to implement this feature is to change the innermost dictionary instead of mapping subjects(its keys) to a list of grades(its values), I can use the tuple of(score, weight) in the values list
class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count


# The use of this class is hard now:
book = WeightedGradebook()
book.add_student('Patryk Klimowicz')
book.report_grade('Patryk Klimowicz', 'Math', 75, 0.05)
book.report_grade('Patryk Klimowicz', 'Math', 65, 0.15)
book.report_grade('Patryk Klimowicz', 'Math', 70, 0.80)
book.report_grade('Patryk Klimowicz', 'Gym', 100, 0.40)
book.report_grade('Patryk Klimowicz', 'Gym', 85, 0.60)
print(book.average_grade('Patryk Klimowicz'))


# REFACTORIN CLASSES #
# Use of namedtuple allows us to create tiny, immutable data classes we can use for grades:
Grade = namedtuple('Grade', ('score', 'weight'))

####################################################
#           LIMITATIONS OF NAMEDTUPLE              #
####################################################
# 1. You can’t specify default argument values for namedtuple classes. This makes them unwieldy when your data may have many optional properties. If you find yourself using more than a handful of attributes, using the built-in dataclasses module may be a better choice.
# 2. The attribute values of namedtuple instances are still accessible using numerical indexes and iteration. Especially in externalized APIs, this can lead to unintentional usage that makes it harder to move to a real class later. If you’re not in control of all of the usage of your namedtuple instances, it’s better to explicitly define a new class.
###################################################


# Next we can define a class to represent a single subject that contains a set of grades:
class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


# Next we can write a class to represent a set of subjects that are being studied by a single student
class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


# Finally we can create a gradebook keyed dynamically by their name
class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


# And now how we can use our gradebook:
book = Gradebook()
patryk = book.get_student('Patryk Klimowicz')

math = patryk.get_subject('Math')
math.report_grade(93, 0.05)
math.report_grade(82, 0.15)
math.report_grade(84, 0.80)

gym = patryk.get_subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(patryk.average_grade())
