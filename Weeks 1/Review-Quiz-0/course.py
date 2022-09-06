
class Course:
    def __init__(self, course_id: str, description: str, credits: int) -> None:
        # Didn't raise ValueError, TypeError
        self._course_id = course_id
        self._description = description
        self._credits = credits
    
    @property
    def course_id(self):
        return self._course_id

    @property
    def description(self):
        return self._description

    @property
    def credits(self):
        return self._credits
    
    def __str__(self):
        return f"{self._course_id} {self._description} ({self._credits})"

    def __eq__(self, other):
        # Didn't check Course obj.
        return self._course_id == other._course_id and self._description == other.description and self._credits == other.credits
