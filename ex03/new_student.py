from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    """generate a random id"""
    random_chars = ''.join(random.choices(string.ascii_lowercase, k=8))
    return random_chars


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """post init"""
        self.login = self.name[0].lower() + self.surname[:7].lower()
        self.id = generate_id()
