from Employee import Employee


class Designer(Employee):
    def __init__(self, name, seniority, awards_count):
        super().__init__(name, seniority)
        self.awards_count = awards_count
        self.seniority += self.awards_count * 2  # adds 2 points for each international award

    def check_time_for_update(self):
        self.seniority += 1

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()


def main():
    alex = Designer('Alex', awards_count=2, seniority=2)
    alex.check_time_for_update()


main()
