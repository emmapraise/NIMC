from django.utils.translation import gettext_lazy as _

# Admin Type
LOCAL = "Local Goverment"
STATE = "State Goverment"
FEDERAL = "Federal Goverment"


def admin_types():
    types = [
        (LOCAL, "Local Goverment"),
        (STATE, "State Goverment"),
        (FEDERAL, "Federal Goverment"),
    ]
    return types
