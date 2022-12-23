class IdentifierNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
class OperatorNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
class KeywordNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
        
class ExprNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CodeBlockNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class FuncNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ClassNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MethodNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class FieldNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ModelFieldNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class FormFieldNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ViewNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class UrlNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ViewSetNotValidError(TypeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
