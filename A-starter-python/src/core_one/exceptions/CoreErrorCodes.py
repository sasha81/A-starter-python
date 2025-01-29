import enum


core = "CORE"

class CoreErrorCodes(enum.Enum):
    incompatibleInputConditions = core+".INCOMPATIBLE_INPUT_CONDITIONS"

    divisionByZero = core+".DIVISION_BY_ZERO"
