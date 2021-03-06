## The database format for universal energy management system.
## As there are three processes in the the operation, there are three tablets for all processes.
## For each equipment, the operation status in specific operation process is recorded as well.
## The following parameters are required to be recorded in the database.
## The naming of the database follow the following rules.
## 1)G represents the injection.
## 2)D represents the absorption.
## 3)AC represents for the alternative current.
## 4)DC represents for the direct current.
## 5)U represents for the uncritical.
## 6)P represents for the active power.
## 7)Q represents for the reactive power.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, FLOAT, INTEGER, DATETIME, BINARY

Base = declarative_base()


class db_long_term_forecasting(Base):
    # Long-term forecasting results.(For unit commitment.)
    __tablename__ = 'long_term_forecasting'

    # The unique and primary key in long term forecasting.
    TIME_STAMP = Column(INTEGER, primary_key=True)

    # Load group.
    AC_PD = Column(FLOAT)
    AC_QD = Column(FLOAT)
    UAC_PD = Column(FLOAT)
    UAC_QD = Column(FLOAT)
    DC_PD = Column(FLOAT)
    UDC_PD = Column(FLOAT)

    # Renewable energy group.
    PV_PG = Column(FLOAT)
    WP_PG = Column(FLOAT)

    # Price information.
    PRICE = Column(FLOAT)


class db_mid_term_forecasting(Base):
    # Mid-term forecasting results.(For economic dispatch.)
    __tablename__ = 'mid_term_forecasting'

    # The unique and primary key in long term forecasting.
    TIME_STAMP = Column(INTEGER, primary_key=True)

    # Load group.
    AC_PD = Column(FLOAT)
    AC_QD = Column(FLOAT)
    UAC_PD = Column(FLOAT)
    UAC_QD = Column(FLOAT)
    DC_PD = Column(FLOAT)
    UDC_PD = Column(FLOAT)

    # Renewable energy group.
    PV_PG = Column(FLOAT)
    WP_PG = Column(FLOAT)

    # Price information.
    PRICE = Column(FLOAT)


class db_short_term_forecasting(Base):
    # Short-term forecasting results.(For optimal power flow.)
    __tablename__ = 'short_term_forecasting'

    # The unique and primary key in long term forecasting.
    TIME_STAMP = Column(INTEGER, primary_key=True)

    # Load group.
    AC_PD = Column(FLOAT)
    AC_QD = Column(FLOAT)
    UAC_PD = Column(FLOAT)
    UAC_QD = Column(FLOAT)
    DC_PD = Column(FLOAT)
    UDC_PD = Column(FLOAT)

    # Renewable energy group.
    PV_PG = Column(FLOAT)
    WP_PG = Column(FLOAT)

    # Price information.
    PRICE = Column(FLOAT)


class db_unit_commitment(Base):
    # Long_term operation database format.
    __tablename__ = 'long_term_operation'
    TIME_STAMP = Column(INTEGER, primary_key=True)  # The primary and unique key in the database.
    # Forecasting results group.
    # Load group.
    AC_PD = Column(INTEGER)
    AC_QD = Column(INTEGER)
    UAC_PD = Column(INTEGER)
    UAC_QD = Column(INTEGER)
    DC_PD = Column(INTEGER)
    UDC_PD = Column(INTEGER)
    # Renewable energy group.
    PV_PG = Column(INTEGER)
    WP_PG = Column(INTEGER)
    PRICE = Column(FLOAT)
    # Schedulable sources group.
    # AC side
    # Generations
    DG_STATUS = Column(BINARY)
    DG_PG = Column(INTEGER)
    DG_QG = Column(INTEGER)
    # Utility grid.
    UG_STATUS = Column(BINARY)
    UG_PG = Column(INTEGER)
    UG_QG = Column(INTEGER)
    # BIC
    BIC_PG = Column(INTEGER)
    BIC_QG = Column(INTEGER)
    # DC side
    # Battery.
    BAT_PG = Column(INTEGER)
    BAT_SOC = Column(FLOAT)
    # The universal energy management settings. If it is a local version, these parameters will not be generated.
    PMG = Column(INTEGER)
    V_DC = Column(FLOAT)
    # Emergency operation
    # Renewable energy curtailment.
    PV_CURT = Column(INTEGER)
    WP_CURT = Column(INTEGER)
    # Load shedding.
    AC_SHED = Column(INTEGER)
    UAC_SHED = Column(INTEGER)
    DC_SHED = Column(INTEGER)
    UDC_SHED = Column(INTEGER)


class db_economic_dispatch(Base):
    # Mid_term operation database format.
    __tablename__ = 'mid_term_operation'
    TIME_STAMP = Column(INTEGER, primary_key=True)  # The primary and unique key in the database.
    # Forecasting results group.
    # Load group.
    AC_PD = Column(INTEGER)
    AC_QD = Column(INTEGER)
    UAC_PD = Column(INTEGER)
    UAC_QD = Column(INTEGER)
    DC_PD = Column(INTEGER)
    UDC_PD = Column(INTEGER)
    # Renewable energy group.
    PV_PG = Column(INTEGER)
    WP_PG = Column(INTEGER)
    PRICE = Column(FLOAT)
    # Schedulable sources group.
    # AC side
    # Generations
    DG_STATUS = Column(BINARY)
    DG_PG = Column(INTEGER)
    DG_QG = Column(INTEGER)
    # Utility grid.
    UG_STATUS = Column(BINARY)
    UG_PG = Column(INTEGER)
    UG_QG = Column(INTEGER)
    # BIC
    BIC_PG = Column(INTEGER)
    BIC_QG = Column(INTEGER)
    # DC side
    # Battery.
    BAT_PG = Column(INTEGER)
    BAT_SOC = Column(FLOAT)
    # The universal energy management settings. If it is a local version, these parameters will not be generated.
    PMG = Column(INTEGER)
    V_DC = Column(FLOAT)
    # Emergency operation
    # Renewable energy curtailment.
    PV_CURT = Column(INTEGER)
    WP_CURT = Column(INTEGER)
    # Load shedding.
    AC_SHED = Column(INTEGER)
    UAC_SHED = Column(INTEGER)
    DC_SHED = Column(INTEGER)
    UDC_SHED = Column(INTEGER)


class db_optimal_power_flow(Base):
    # The database format of optimal power flow.
    __tablename__ = 'short_term_operation'

    TIME_STAMP = Column(INTEGER, primary_key=True)  # The primary and unique key in the database.
    # Forecasting results group.
    # Load group.
    AC_PD = Column(INTEGER)
    AC_QD = Column(INTEGER)
    UAC_PD = Column(INTEGER)
    UAC_QD = Column(INTEGER)
    DC_PD = Column(INTEGER)
    UDC_PD = Column(INTEGER)
    # Renewable energy group.
    PV_PG = Column(INTEGER)
    WP_PG = Column(INTEGER)
    # Schedulable sources group.
    # AC side
    # Generations
    DG_STATUS = Column(BINARY)
    DG_PG = Column(INTEGER)
    DG_QG = Column(INTEGER)
    # Utility grid.
    UG_STATUS = Column(BINARY)
    UG_PG = Column(INTEGER)
    UG_QG = Column(INTEGER)
    # BIC
    BIC_PG = Column(INTEGER)
    BIC_QG = Column(INTEGER)
    # DC side
    # Battery.
    BAT_PG = Column(INTEGER)
    BAT_SOC = Column(FLOAT)
    # The universal energy management settings. If it is a local version, these parameters will not be generated.
    PMG = Column(INTEGER)
    V_DC = Column(FLOAT)
    # Emergency operation
    # Renewable energy curtailment.
    PV_CURT = Column(INTEGER)
    WP_CURT = Column(INTEGER)
    # Load shedding.
    AC_SHED = Column(INTEGER)
    UAC_SHED = Column(INTEGER)
    DC_SHED = Column(INTEGER)
    UDC_SHED = Column(INTEGER)
