from django.utils.translation import gettext_lazy as _

# Admin Type
LOCAL = "Local Government"
STATE = "State Government"
FEDERAL = "Federal Government"

# Approval Status
PENDING = 0
DISAPPROVED = 1
COMPLETED = 2
APPROVED = 3


def admin_types():
    """Enum field of admin types"""

    types = [
        (LOCAL, "Local Government"),
        (STATE, "State Government"),
        (FEDERAL, "Federal Government"),
    ]
    return types


def approval_status():
    """Enum field for approval status"""

    status = [
        (PENDING, "Pending"),
        (DISAPPROVED, "Disapproved"),
        (COMPLETED, "Completed"),
        (APPROVED, "Approved"),
    ]
    return status
