from django.utils.translation import gettext_lazy as _

# Document Type
OLD_NATIONAL_ID_CARD = "Old National ID Card"
DRIVERS_LICENSE = "Driver’s License"
VOTERS_CARD = "Voter’s card (Temporary or Permanent)"
INTERNATIONAL_PASSPORT = "Nigerian International passport"
COO = "Certificate of Origin"
CV = "Curriculum Vitae"
CERTIFICATE = "Certificate"
TRANSCRIPT = "Transcript"

# Education Type
PRIMARY_EDUCATION = "Primary Education"
SECONDARY_EDUCATION = "Secondary Education"
OND = "Ordinary National Diploma"
HND = "Higher National Diploma"
DEGREE = "Degree"
MASTERS = "Masters"
PHD = "Doctor of Philosophy"

# Education Class type
FIRST_CLASS = "First class"
SECOND_CLASS_UPPER = "Second class upper"
SECOND_CLASS_LOWER = "Second class lower"
THIRD_CLASS = "Third class"
PASS = "Pass"

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
        (CV, "Curriculum Vitae"),
        (CERTIFICATE, "Certificate"),
        (TRANSCRIPT, "Transcript"),
    ]

    return types


def education_type():
    types = [
        (PRIMARY_EDUCATION, "Primary Education"),
        (SECONDARY_EDUCATION, "Secondary Education"),
        (OND, "Ordinary National Diploma"),
        (HND, "Higher National Diploma"),
        (DEGREE, "Degree"),
        (MASTERS, "Masters"),
        (PHD, "Doctor of Philosophy"),
    ]
    return types


def education_class_type():
    types = [
        (FIRST_CLASS, "First Class"),
        (SECOND_CLASS_UPPER, "Second Class Upper"),
        (SECOND_CLASS_LOWER, "Second Class Lower"),
        (THIRD_CLASS, "Third Class"),
        (PASS, "Pass"),
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
