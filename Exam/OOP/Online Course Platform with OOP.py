def solution():
    from enum import Enum
    class LessonStatus(Enum):
        NOT_STARTED = "Not started"
        IN_PROGRESS = "In progress"
        COMPLETED = "Completed"
    class Course:
        def __init__(self, course_id: str, title: str):
            self._lesson_progress = []
            self._cource_id = course_id
            self.cource_level = "Beginner"
            # TODO: Store title as public attribute / title-i public atribut olaraq saxlayın
            self.title = "title"
            pass
        
        def __validate_lesson(self, lesson_name: str) -> bool:
            if lesson_name == "":
                raise ValueError("Lesson name cannot be empty")
            return True
            pass
        
        def start_lesson(self, lesson_name: str) -> bool:
            self.__validate_lesson(lesson_name)
            self._lesson_progress.append({"lesson_name": lesson_name, "status": LessonStatus.IN_PROGRESS})
            return True
            pass
        
        def complete_lesson(self, lesson_name: str) -> bool:
            self._lesson_progress.append({"lesson_name": lesson_name, "status": LessonStatus.COMPLETED})
            return True
            pass
        
        def get_completion_rate(self) -> float:
            count = 0
            total = len(self._lesson_progress)
            if total == 0:
                return 0
            for lesson in self._lesson_progress:
                if lesson["status"] == LessonStatus.COMPLETED:
                    count += 1
            return (count / total) * 100
            pass
        
        def get_lesson_progress(self, status = None):
            if status is None:
                return self._lesson_progress
            return [rec for rec in self._lesson_progress if rec["status"] == status]
            pass
    
    class AdvancedCourse(Course):
        def __init__(self, course_id: str, title: str, prerequisites: list):
            super().__init__(course_id, title)
            self.__prerequisites = prerequisites
            self.cource_level = "Advanced"
            pass
        
        def get_prerequisites(self) -> list:
            return self.__prerequisites
            pass
        
        def start_lesson(self, lesson_name: str) -> bool:
            count = 0
            for lesson in self._lesson_progress:
                if lesson["status"] == LessonStatus.COMPLETED:
                    count += 1
            if count < 1:
                raise ValueError("Must complete prerequisites first")
            super().start_lesson(lesson_name)
            pass
    
    # Write your code here
    return (LessonStatus, Course, AdvancedCourse)