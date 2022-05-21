from django.utils.translation import gettext_lazy as _

# Document Type
OLD_NATIONAL_ID_CARD = "Old National ID Card"
DRIVERS_LICENSE = "Driver’s License"
VOTERS_CARD = "Voter’s card (Temporary or Permanent)"
INTERNATIONAL_PASSPORT = "Nigerian International passport"
COO = "Certificate of Origin"


def document_types():
    types = [
        (OLD_NATIONAL_ID_CARD, "Old National ID Card"),
        (DRIVERS_LICENSE, "Driver’s License"),
        (VOTERS_CARD, "Voter’s card (Temporary or Permanent)"),
        (INTERNATIONAL_PASSPORT, "Nigerian International passport"),
        (COO, "Certificate of Origin"),
    ]

    return types
