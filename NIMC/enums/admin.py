from django.utils.translation import gettext_lazy as _

# Admin Type
LOCAL = "Local Goverment"
STATE = "State Goverment"
FEDERAL = "Federal Goverment"

# Approval Status
PENDING = 0
DISAPPROVED = 1
VERIFIED = 2
APPROVED = 3


def admin_types():
    """Enum field of admin types"""

    types = [
        (LOCAL, "Local Goverment"),
        (STATE, "State Goverment"),
        (FEDERAL, "Federal Goverment"),
    ]
    return types


def approval_status():
    """Enum field for approval status"""

    status = [
        (PENDING, "Pending"),
        (DISAPPROVED, "Disapproved"),
        (VERIFIED, "Verified"),
        (APPROVED, "Approved"),
    ]
    return status
