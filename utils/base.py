import keyword
import re
import logging
import exceptions as ex
import helpers as H

# TODO: Keyword class
class Keyword:
    def __init__(self, name) -> None:
        self.name = self.__set_name(name)

    def __set_name(self, name):
        if not self.valid(name):
            raise SyntaxError(f"{name} is not a valid keyword")
        return name

    @staticmethod
    def is_valid(name) -> bool:
        return name in keyword.kwlist

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


# TODO: Operator class
class Operator:
    def __init__(self, __symbol) -> None:
        self.__symbol = self.__set_symbol(__symbol)

    @staticmethod
    def is_valid(symbol):
        return H.is_operator(symbol)

    def __set_symbol(self, symbol):
        if not self.is_valid(symbol):
            raise SyntaxError(f"'{symbol}' is not a valid operator")
        return symbol

    def __str__(self) -> str:
        return self.__symbol

    def __repr__(self) -> str:
        return self.__str__()


# TODO: Comment class
class Comment:
    def __init__(self, __str, multiline=False) -> None:
        self.__str = __str
        self.multiline = multiline

    @property
    def str(self):
        return self.__str

    # TODO: write a method to format the comment as per PEP-8
    def format(self):
        pass

    def __str__(self) -> str:
        return f"""{self.str}""" if self.multiline else f"# {self.str}"

    def __repr__(self) -> str:
        return self.__str__()


# TODO: Indentation class
class Indentation:
    def __init__(self, __spacing=4) -> None:
        self.__spacing = __spacing
        self.level = 0

    @property
    def spaces(self):
        return (self.level * self.__spacing) * " "

    @property
    def next(self):
        self.level += 1
        return self

    @property
    def prev(self):
        self.level -= 1
        return self

    def get_spaces(self, level):
        return (level * self.__spacing) * " "

    def __add__(self, other):
        if not isinstance(other, int | self.__class__):
            raise TypeError(
                f"{other.__class__.__name__} is not a valid type(int or indentation)"
            )
        if isinstance(other, int):
            self.level += other
            self.get_spaces(self.level + other)
        if isinstance(other, self.__class__):
            self.level + other.level
            self.get_spaces(self.level + other.level)

        return self

    def __str__(self) -> str:
        return self.spaces

    def __repr__(self) -> str:
        return self.__str__()


# TODO: Identifier class
class Identifier:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.identifier = __name

    @property
    def identifier(self):
        pass

    @identifier.setter
    def identifier(self, name):
        if not self.is_valid(name):
            raise ex.IdentifierNotValidError(f"{name} is not a valid identifier typw")
        return name

    @staticmethod
    def is_valid(name):
        if not isinstance(name, str):
            raise TypeError(f"{name.__class__.__name__} is not a valid str object")

        pattern_str = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        pattern = re.compile(pattern_str)
        match = pattern.match(name)

        if match is None:
            raise SyntaxError(f"'{name}' is not a valid identifier")

        return match.group()

    def __str__(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return self.__str__()


# TODO: Expression class
class Expression:
    def __init__(self) -> None:
        pass


# TODO: Block class
class Block:
    def __init__(self, lines) -> None:
        self.lines = lines

    def __str__(self) -> str:
        return "\n".join([line for line in self.lines]) + "\n" if self.lines else ""


# TODO: Var class
class Var:
    def __init__(self, identifier, value) -> None:
        self._operator = Operator("=")
        self.identifier = self.__set_identifier(identifier)
        self.value = self.__set_value(value)

    def __set_identifier(self, identifier):
        if not isinstance(identifier, Identifier):
            raise ex.IdentifierNotValidError(
                f"{identifier} is not a valid identifier instance"
            )
        return identifier

    def __set_value(self, value):
        return value

    def __str__(self) -> str:
        return " ".join([str(self.identifier), str(self._operator), str(self.value)])


# TODO: Condition class
class Condition:
    def __init__(self, keyword, expression) -> None:
        self.keyword = self.__set_keywor


# TODO: ForLoop class
# TODO: WhileLoop class
# TODO: Function class
class Function:
    def __init__(self, name, args, kwargs, body, prefix="", suffix="") -> None:
        self.prefix = prefix
        self.suffix = suffix
        self.indentation = Indentation()
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.__variables = []

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, values):
        name, value = values
        var = Var(Identifier(name), value)
        self.__variables.append(var)

    @property
    def header(self):
        args = ", ".join([str(arg) for arg in self.args])
        kwargs = ", ".join([f"{k}={v}" for k, v in self.kwargs.items()])
        args_kwargs = args + ", " + kwargs
        head = f"{self.indentation.next}def {self.prefix}{self.name}{self.suffix}({args_kwargs}):\n"
        return head

    @property
    def body(self):
        self.indentation + 1
        variables = (
            "\n".join([str(self.indentation) + str(var) for var in self.variables])
            + "\n"
            if self.variables
            else ""
        )

        body_ = variables

        return body_

    def __str__(self) -> str:
        return self.header + self.body


# TODO: Class class
class Class:
    def __init__(self, name, parents, prefix="", suffix="") -> None:
        self.errors = []
        self.__body = []
        self.indentation = Indentation()
        self.class_vars = []
        self.methods = []
        self.name = name
        self.prefix = prefix
        self.suffix = suffix
        self.parents = [
            parent_ for parent in parents if (parent_ := self.add_parent(parent))
        ]

    def add_parent(self, parent):
        if not isinstance(parent, Class):
            print(f"#WARNING: {parent} is not a valid class instance!")
            return self.errors.append(
                ex.ClassNotValidError(f"{parent} is not a valid class instance!")
            )
        return parent

    def add_class_var(self, name, value):
        var = Var(Identifier(name), value)
        self.class_vars.append(var)

    def add_method(self, method):
        if not isinstance(method, Method):
            print(f"#WARNING: {method} is not a valid class instance!")
            return self.errors.append(
                ex.ClassNotValidError(f"{method} is not a valid class instance!")
            )
        method.class_ = self
        self.methods.append(method)

    @property
    def header(self):
        parents = ", ".join([str(parent) for parent in self.parents])
        head = f"{str(self.indentation)}class {self.prefix}{self.name}{self.suffix}({parents}):\n\n"
        return head

    @property
    def body(self):
        class_variables = (
            "\n".join([str(self.indentation + 1) + str(var) for var in self.class_vars])
            + "\n\n"
            if self.class_vars
            else ""
        )
        methods = (
            "\n\n".join([str(method) for method in self.methods]) + "\n"
            if self.methods
            else ""
        )

        body_ = class_variables + methods

        return body_

    def __str__(self) -> str:
        return self.header + self.body


# TODO: Method class
class Method(Function):
    def __init__(
        self,
        name,
        args,
        kwargs,
        body,
        type="user_defined",
        access="public",
        prefix="",
        suffix="",
    ) -> None:
        super().__init__(name, args, kwargs, body, prefix, suffix)
        self.args.insert(0, "self")
        self.__class = None
        if access == "public":
            self.acces_prefix = ""
        elif access == "protected":
            self.acces_prefix = "_"
        elif access == "private":
            self.acces_prefix = "__"
        # to add built-in method prefix, suffix
        if type == "built_in":
            self.prefix = "__"
            self.suffix = "__"

        for line in body:
            self.variables = line

    @property
    def class_(self):
        return self.__class

    @class_.setter
    def class_(self, value):
        if not isinstance(value, Class):
            print(f"#WARNING: {value} is not a valid class instance!")
            return self.errors.append(
                ex.ClassNotValidError(f"{value} is not a valid class instance!")
            )
        self.__class = value
        self.indentation = self.class_.indentation + 1
        return self


# TODO: Statement class
class Statement:
    def __init__(self, identifier, operator, value) -> None:
        self.identifier = identifier
        self.operator = operator
        self.value = self.__set_value(value)
        super().__init__()

    def __str__(self) -> str:
        return self.identifier + self.operator + self.value

    def __set_value(self, value):
        return value


# ident = Identifier("name_1")
# result = ident.is_valid("name__1")
# print(ident)

stat = Statement(Identifier("name"), Operator("="), "Jinto A G")
klass = Class("MyClass", [])
klass.add_class_var("class_var_1", "1")
klass.add_method(
    Method(
        Identifier("some_method"),
        ["arg_1", "arg_2"],
        {"kwargs_1": "value_1", "kwargs_2": "value_2"},
        [
            ("some_variable", "1"),
            ("some_variable_2", "1"),
        ],
    )
)
print(klass)


class Arg:
    pass


class Kwargs:
    pass


klass_1 = Class(
    Identifier("MyClass"),
    parents=[
        Class(Identifier("ParentClass")),
    ],
    methods=[
        Method(
            Identifier("first_method"),
            args=[
                Arg("arg_1"),
                Arg("arg_2"),
            ],
            kwargs=[
                Kwargs("key", "value"),
                Kwargs("key", "value"),
            ],
            body=[
                Statement(),
                Statement(),
                Block(
                    header=[
                        Keyword("if"),
                        Expression(
                            Identifier("name"),
                            Operator("=="),
                            "value",
                        ),
                    ],
                    body=[
                        Var(Identifier(), "value"),
                        Function()(Arg(), Kwargs())
                    ],
                ),
            ],
        ),
    ],
)
