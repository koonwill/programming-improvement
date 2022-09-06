class CourseList:
    def __init__(self) -> None:
        self.cl = {}

    def add_course(self, course):
        if course.course_id not in self.cl:
            self.cl[course.course_id] = course
            return True
        return False

    def drop_course(self, course_id):
        if course_id in self.cl:
            self.cl.pop(course_id)
            return True
        return False

    def get_credits(self):
        all_credits = 0
        for course in self.cl.values():
            all_credits += course.credits
        return all_credits

    def __len__(self):
        return len(self.cl)
