from course import Course

class CourseList(Course):
    def __init__(self) -> None:
        #Wrong Logic
        self.course_list = []

    def add_course(self, course):
        if course not in CourseList:
            return True
    # Can't Finish it in time.