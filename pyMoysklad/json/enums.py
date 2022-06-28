from enum import Enum


class GenderEnum(Enum):
    MASCULINE = "masculine"
    FEMININE = "feminine"


class TariffEnum(Enum):
    BASIC = "BASIC"
    CORPORATE = "CORPORATE"
    FREE = "FREE"
    MINIMAL = "MINIMAL"
    PROFESSIONAL = "PROFESSIONAL"
    RETAIL = "RETAIL"
    START = "START"
    TRIAL = "TRIAL"


class CompanyType(Enum):
    LEGAL = "legal"
    ENTREPRENEUR = "entrepreneur"
    INDIVIDUAL = "individual"
