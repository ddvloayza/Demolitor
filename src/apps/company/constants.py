from django.utils.translation import gettext_lazy as _

UNIPERSONAL = "UNIPERSONAL"
EIRL = "EIRL"
SRL = "SRL"
SA = "SA"
SAA = "SAA"
SAC = "SAC"


TYPE_COMPANY_CHOICES = (
    (UNIPERSONAL, _("EMPRESA UNIPERSONAL")),
    (EIRL, _("E.I.R.L")),
    (SRL, _("S.R.L")),
    (SA, _("SOCIEDAD ANONIMA S.A.")),
    (SAA, _("SOCIEDAD ANONIMA ABIERTA S.A.A.")),
    (SAC, _("SOCIEDAD ANONIMA CERRADA S.A.C.")),

)


