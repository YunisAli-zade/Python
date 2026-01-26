def solution():
    # TODO: Import Enum from enum module / enum modulundan Enum-u import edin
    from enum import Enum
    # TODO: Create EventStatus Enum class with DRAFT, CONFIRMED, IN_PROGRESS, COMPLETED members / DRAFT, CONFIRMED, IN_PROGRESS, COMPLETED üzvləri ilə EventStatus Enum sinfi yaradın
    class EventStatus(Enum):
        DRAFT = "Draft"
        CONFIRMED = "Confirmed"
        IN_PROGRESS = "In progress"
        COMPLETED = "Completed"
        
    class Event:
        def __init__(self, event_id: str, title: str):
            # TODO: Initialize __status_history to empty list / __status_history-ni boş siyahı olaraq inisializasiya edin
            self.__status_history = []
            # TODO: Store event_id as protected attribute / event_id-i protected atribut olaraq saxlayın
            self._event_id = event_id
            # TODO: Set event_type to "General" / event_type-i "General" olaraq təyin edin
            self.event_type = "General"
            # TODO: Store title as public attribute / title-i public atribut olaraq saxlayın
            self.title = title
            pass
        
        def __validate_attendees(self, count: int) -> bool:
            # TODO: Check if count < 0 / count < 0 olub-olmadığını yoxlayın
            if count < 0:
            # TODO: Raise ValueError if so / Belədirsə ValueError qaytarın
            	raise ValueError("Error should mention negative" )
            # TODO: Return True if valid / Etibarlıdırsa True qaytarın
            return True
            pass
        
        def update_status(self, status, timestamp: str) -> bool:
            # TODO: Add to __status_history: {"status": status, "timestamp": timestamp} / __status_history-yə əlavə edin
            self.__status_history.append({"status": status, "timestamp": timestamp})
            # TODO: Return True / True qaytarın
            return True
            pass
        
        def get_current_status(self):
            # TODO: Return last status from history, or None if empty / Tarixçədən sonuncu statusu qaytarın, boşdursa None qaytarın
            if not self.__status_history:
                return None
            return self.__status_history[-1]["status"]
            pass
        
        def get_status_history(self, status = None):
            # TODO: If status is None, return all history / status None-dursa bütün tarixçəni qaytarın
            if status is None:
                return self.__status_history
            # TODO: Otherwise filter by status / Əks halda status üzrə süzün
            return [rec for rec in self.__status_history if rec["status"] == status]
            pass
    
    # TODO: Make CorporateEvent inherit from Event / CorporateEvent-i Event-dən miras alın
    class CorporateEvent(Event):
        def __init__(self, event_id: str, title: str, min_attendees: int):
            # TODO: Call parent constructor / Valideyn konstruktorunu çağırın
            super().__init__(event_id, title)
            # TODO: Store min_attendees as private attribute / min_attendees-i private atribut olaraq saxlayın
            self._min_attendees = min_attendees
            # TODO: Set event_type to "Corporate" / event_type-i "Corporate" olaraq təyin edin
            self.event_type = "Corporate"
            pass
        
        def get_min_attendees(self) -> int:
            # TODO: Return min_attendees / min_attendees qaytarın
            return self._min_attendees
            pass
        
        def update_status(self, status, timestamp: str) -> bool:
            # TODO: Check if status is CONFIRMED and min_attendees < 10 / status CONFIRMED-dursa və min_attendees < 10-dursa yoxlayın
            if status == EventStatus.CONFIRMED and self._min_attendees < 10:
            # TODO: Raise ValueError if so / Belədirsə ValueError qaytarın
            	raise ValueError("Corporate events require at least 10 attendees to confirm")
            # TODO: Otherwise call parent's update_status / Əks halda valideynin update_status-unu çağırın
            return super().update_status(status, timestamp)
            pass
    
    # Write your code here
    return (EventStatus, Event, CorporateEvent)