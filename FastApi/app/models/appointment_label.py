"""
This module defines the AppointmentLabel enum class,
which represents different types of appointment labels.
"""

from enum import Enum


class AppointmentLabel(Enum):
    """
    Enum class representing different types of appointment labels.
    Attributes:
        URGENCY (int): Represents an urgent appointment.
        CONTROL (int): Represents a control appointment.
        HYGIENE (int): Represents a hygiene appointment.
        ASSESSMENT (int): Represents an assessment appointment.
    """

    URGENCY = 1
    CONTROL = 2
    HYGIENE = 3
    ASSESSMENT = 4
