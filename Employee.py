class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        self.grade += 1

    def publish_grade(self):
        print(self.name, self.grade)

    def check_time_for_update(self):
        pass
