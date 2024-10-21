import graphene


class EnumChoices(graphene.Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)