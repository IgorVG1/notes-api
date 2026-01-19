from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def name(self) -> str:
        return self.faker.name()

    def email(self) -> str:
        return self.faker.email()

    def password(self) -> str:
        return self.faker.password(length=8)

    def phone(self) -> str:
        return self.faker.phone_number()

    def company(self) -> str:
        return self.faker.company_name_word()

    def title(self) -> str:
        return self.faker.sentence()

    def description(self) -> str:
        return self.faker.paragraph(nb_sentences=1)

    def category(self) -> str:
        return self.faker.space_object_name()

    def id(self) -> str:
        return self.faker.uuid4()


fake = Fake(faker=Faker())