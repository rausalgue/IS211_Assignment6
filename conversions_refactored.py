#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Six - Part IV Refactor"""

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    """Converts Values

        Check that all temperature conversions are working
        Check that all distance conversions are working
        * Check that converting from one unit to itself returns the same value for all units
        * Check that converting from incompatible units will raise a ConversionNotPossible exception
        * which should be defined in the conversions_refactored.py file)

    Args:
        fromUnit (str): From Unit
        toUnit (str): To Unit
        value (float): value to convert

    Returns:
        convertedValue: Convert Value
    """

    if fromUnit == toUnit:
        convertedValue = value
        return convertedValue

    isTempFrom = False
    isDistFrom = False
    isTempTo = False
    isDistTo = False

    #Check if we have Temperature
    if fromUnit.lower() == "celcius" or fromUnit.lower() == "kelvin" or fromUnit.lower() == "farenheit":
        isTempFrom = True
    else:
        if fromUnit.lower() == "miles" or fromUnit.lower() == "yards" or fromUnit.lower() == "meters":
            isDistFrom = True
        else:
            raise ConversionNotPossible, "Error: Incompatible Units"

    if toUnit.lower() == "celcius" or toUnit.lower() == "kelvin" or toUnit.lower() == "farenheit":
        isTempTo = True
    else:
        if toUnit.lower() == "miles" or toUnit.lower() == "yards" or toUnit.lower() == "meters":
            isDistTo = True
        else:
            raise ConversionNotPossible, "Error: Incompatible Units"

    if isTempFrom and isTempTo:
        #All the cases
        if fromUnit.lower() == 'celcius' and toUnit.lower() == 'kelvin':
            convertedValue = value + 273.15

        elif fromUnit.lower() == 'celcius' and toUnit.lower() == 'farenheit':
            convertedValue = value * 9 / 5 + 32
            #print 'c - f',convertedValue

        elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'celcius':
            convertedValue = value - 273.15

        elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'farenheit':
            convertedValue = value * 9 / 5 - 459.67

        elif fromUnit.lower() == 'farenheit' and toUnit.lower() == 'celcius':
            convertedValue = (value - 32) * 5 / 9

        elif fromUnit.lower() == 'farenheit' and toUnit.lower() == 'kelvin':
            convertedValue = (value + 459.67) * 5 / 9

        return round(convertedValue,2)


    if isDistFrom and isDistTo:
        if fromUnit.lower() == 'miles' and toUnit.lower() == 'yards':
            convertedValue = value * 1760

        elif fromUnit.lower() == 'miles' and toUnit.lower() == 'meters':
            convertedValue = value / 0.00062137

        elif fromUnit.lower() == 'yards' and toUnit.lower() == 'miles':
            convertedValue = value / 1760

        elif fromUnit.lower() == 'yards' and toUnit.lower() == 'meters':
            convertedValue = value / 1.0936

        elif fromUnit.lower() == 'meters' and toUnit.lower() == 'miles':
            convertedValue = value * 0.00062137

        elif fromUnit.lower() == 'meters' and toUnit.lower() == 'yards':
            convertedValue = value * 1.0936

        return round(convertedValue,2)

    raise ConversionNotPossible, "Error: Cannot Convert Distance and Temperature"



