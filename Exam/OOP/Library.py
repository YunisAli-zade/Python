def solution():
    # TODO: Import Enum from enum module / enum modulundan Enum-u import edin
    from enum import Enum
    # TODO: Create ActionType enum class with BORROW = "borrow" and RETURN = "return" / ActionType enum sinfi yaradın: BORROW = "borrow" və RETURN = "return"
    class ActionType(Enum):
        BORROW = "borrow"
        RETURN = "return"
    
    class Book:
        def __init__(self, book_id: str, title: str):
            # TODO: Initialize _is_borrowed to False / _is_borrowed-u False olaraq inisializasiya edin
            self._is_borrowed = False
            # TODO: Initialize _borrow_history to empty list / _borrow_history-ni boş siyahı olaraq inisializasiya edin
            self._borrow_history = []
            # TODO: Store book_id as protected attribute _book_id / book_id-i protected atribut _book_id olaraq saxlayın
            self._book_id = book_id
            # TODO: Store title as public attribute / title-ı public atribut olaraq saxlayın
            self.title = title
            # TODO: Set book_type to "Regular" / book_type-ı "Regular" olaraq təyin edin
            self.book_type = "Regular"
            pass
        
        def _validate_operation(self) -> bool:
            # TODO: Check if book is already borrowed / Kitabın artıq götürülüb-götürülmədiyini yoxlayın
            if self._is_borrowed:
            # TODO: Raise ValueError with message "Book is already borrowed" if it is / Götürülübsə "Book is already borrowed" mesajı ilə ValueError qaytarın
            	raise ValueError("Book is already borrowed")
            # TODO: Return True if not borrowed / Götürülməyibsə True qaytarın
            return True
            pass
        
        def borrow(self) -> bool:
            # TODO: Call _validate_operation to check if book can be borrowed / Kitabın götürülə biləcəyini yoxlamaq üçün _validate_operation-u çağırın
            if self._validate_operation():
            # TODO: Set _is_borrowed to True / _is_borrowed-u True olaraq təyin edin
            	self._is_borrowed = True
            # TODO: Add record dict to _borrow_history using ActionType.BORROW.value: {"action": ActionType.BORROW.value, "book_id": self._book_id} / ActionType.BORROW.value istifadə edərək qeyd dict-ini _borrow_history-ə əlavə edin
            self._borrow_history.append({"action": ActionType.BORROW.value, "book_id": self._book_id})
            # TODO: Return True / True qaytarın
            return True
            pass
        
        def return_book(self) -> bool:
            # TODO: Set _is_borrowed to False / _is_borrowed-u False olaraq təyin edin
            self._is_borrowed = False
            # TODO: Add record dict to _borrow_history using ActionType.RETURN.value: {"action": ActionType.RETURN.value, "book_id": self._book_id} / ActionType.RETURN.value istifadə edərək qeyd dict-ini _borrow_history-ə əlavə edin
            self._borrow_history.append({"action": ActionType.RETURN.value, "book_id": self._book_id})
            # TODO: Return True / True qaytarın
            return True
            pass
        
        def is_available(self) -> bool:
            # TODO: Return True if not borrowed, False otherwise / Götürülməyibsə True, əks halda False qaytarın
            return True if not self._is_borrowed else False
            pass
        
        def get_history(self, action: ActionType = None):
            # TODO: If action is None, return all history from _borrow_history / Əgər action None-dursa, _borrow_history-dən bütün tarixçəni qaytarın
            if action is None:
                return self._borrow_history
            # TODO: Otherwise, filter and return only records where h["action"] == action.value / Əks halda, yalnız h["action"] == action.value olan qeydləri süzün və qaytarın
            return [rec for rec in self._borrow_history if rec["action"] == action.value]
            pass
    
    # TODO: Make ReferenceBook inherit from Book / ReferenceBook-u Book-dan miras alın
    class ReferenceBook(Book):
        def __init__(self, book_id: str, title: str, max_borrow_days: int):
            # TODO: Call parent constructor with super().__init__(book_id, title) / Valideyn konstruktorunu super().__init__(book_id, title) ilə çağırın
            super().__init__(book_id, title)
            # TODO: Store max_borrow_days as private attribute _max_borrow_days / max_borrow_days-i private atribut _max_borrow_days olaraq saxlayın
            self._max_borrow_days = max_borrow_days
            # TODO: Set book_type to "Reference" / book_type-ı "Reference" olaraq təyin edin
            self.book_type = "Reference"
            pass
        
        def borrow(self) -> bool:
            # TODO: Check if _max_borrow_days > 3 / _max_borrow_days > 3 olub-olmadığını yoxlayın
            if self._max_borrow_days > 3:
            # TODO: If yes, raise ValueError with message "Reference books cannot be borrowed for more than 3 days, but this book requires X days" / Bəli olarsa, ValueError qaytarın
            	raise ValueError("Reference books cannot be borrowed for more than 3 days, but this book requires X days")
            # TODO: Otherwise, call and return parent's borrow method using super().borrow() / Əks halda, super().borrow() istifadə edərək valideynin borrow metodunu çağırın və qaytarın
            return super().borrow()
            pass
        
        def get_max_days(self) -> int:
            # TODO: Return _max_borrow_days / _max_borrow_days-i qaytarın
            return self._max_borrow_days
            pass
    
    # Write your code here
    return (ActionType, Book, ReferenceBook)
