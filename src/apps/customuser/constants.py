from django.utils.translation import gettext_lazy as _

TYPE_DNI = "DNI"
TYPE_CARNET = "CARNET"

TYPE_CHOICES = (
    (TYPE_DNI, _("DNI")),
    (TYPE_CARNET, _("Carnet de Extranjeria")),
)

GENDER_MALE = "MALE"
GENDER_FEMALE = "FEMALE"
GENDER_OTHER = "OTHER"

GENDER_CHOICES = (
    (GENDER_MALE, _("Hombre")),
    (GENDER_FEMALE, _("Mujer")),
    (GENDER_OTHER, _("Otros")),
)

CHOICE_MARRIED = "MARRIED"
CHOICE_DIVORCED = "DIVORCED"
CHOICE_SINGLE = "SINGLE"

CIVIL_CHOICES = (
    (CHOICE_MARRIED, _("Casado")),
    (CHOICE_DIVORCED, _("Divorciado")),
    (CHOICE_SINGLE, _("Soltero")),
)
