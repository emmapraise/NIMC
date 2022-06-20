from django.utils.translation import gettext_lazy as _

# Document Type
OLD_NATIONAL_ID_CARD = "Old National ID Card"
DRIVERS_LICENSE = "Driver’s License"
VOTERS_CARD = "Voter’s card (Temporary or Permanent)"
INTERNATIONAL_PASSPORT = "Nigerian International passport"
COO = "Certificate of Origin"

# Martial Status
SINGLE = "Single"
MARRIED = "Married"
DIVORCED = "Divoreced"

# Blood Group
A = "A"
B = "B"
AB = "AB"
O = "O"

# Genotype
AA = "AA"
AS = "AS"
AC = "AC"
SS = "SS"


def documentTypes():
    types = [
        (OLD_NATIONAL_ID_CARD, "Old National ID Card"),
        (DRIVERS_LICENSE, "Driver’s License"),
        (VOTERS_CARD, "Voter’s card (Temporary or Permanent)"),
        (INTERNATIONAL_PASSPORT, "Nigerian International passport"),
        (COO, "Certificate of Origin"),
    ]

    return types


def maritalStatus():
    type = [(SINGLE, "Single"), (MARRIED, "Married"), (DIVORCED, "Divoreced")]
    return type


def bloodGroup():
    group = [(A, "A"), (B, "B"), (AB, "AB"), (O, "O")]
    return group


def genotype():
    type = [(AA, "AA"), (AS, "AS"), (AC, "AC"), (SS, "SS")]
    return type
