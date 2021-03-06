import enum


@enum.unique
class VrmType(enum.Enum):
    PROBE_INIT = 1
    PROBE_ACK = 2
    REG_ACK = 3
    QUERY_ACK = 4
