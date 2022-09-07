
class Course:
    def __init__(self, course_id, description, credits) -> None:
        if course_id.isspace() or course_id == "":
            raise ValueError(
                "Course_id should not be empty string or one whitespace characters")
        if description.isspace() or description == "":
            raise ValueError(
                "description should not be empty string or one whitespace characters")
        # if type(credits) != int:
        if not isinstance(credits, int):
            raise TypeError("Credits must be integer")
        self.__course_id = course_id
        self.__description = description
        self.__credits = credits

    @property
    def course_id(self):
        return self.__course_id

    @property
    def description(self):
        return self.__description

    @property
    def credits(self):
        return self.__credits

    def __str__(self) -> str:
        return f"{self.course_id} {self.description} ({self.credits})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Course):
            return False
        return other.course_id == self.course_id and other.description == self.description and other.credits == self.credits
