#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Six"""

def convertCelsiusToKelvin(Value):
    """Converts Celcius to Kelvin

    Args:
        Value (float): Celcius value

    Returns:
        convertedValue: Kelvin Value
    """

    convertedValue = Value + 273.15

    #convertedValue = 0.0
    return round(convertedValue, 2)

def convertCelsiusToFahrenheit(Value):
    """Converts Celcius to Fahrenheit

    Args:
        Value (float): Celcius value

    Returns:
        convertedValue: Farenheit Value
    """

    convertedValue = Value * 9/5 + 32

    #convertedValue = 0.0
    return round(convertedValue, 2)

def convertFahrenheitToCelcius(Value):
    convertedValue = float((Value - 32) * 5/9)
    #print convertedValue

    #convertedValue = 0.0
    #print 'convertedValue: ',convertedValue
    return round(convertedValue, 2)

def convertFahrenheitToKelvin(Value):
    convertedValue = (Value + 459.67) * 5/9

    #convertedValue = 0.0
    return round(convertedValue, 2)

def convertKelvinToFarenheit(Value):
    convertedValue = Value * 9/5 - 459.67

    #convertedValue = 0.0
    return round(convertedValue, 2)

def convertKelvinToCelcius(Value):
    convertedValue = Value - 273.15

    #convertedValue = 0.0
    return round(convertedValue, 2)