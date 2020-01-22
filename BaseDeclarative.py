""" THIS NODULE DEFINES THE BASE DECLARATIVE CLASS FOR THE SQLALCHEMY MODULES """

__version__ = '0.1 (2020-01-22)'
__author__ = 'OSAHON OKUNGBOWA'

import sqlalchemy.ext.declarative as declarative # pip install sqlalchemy

Base = declarative.declarative_base()
