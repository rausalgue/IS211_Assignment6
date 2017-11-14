#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit testing for conversion.py"""

#Import needed libraries
import conversions
import unittest

class KnownValue(unittest.TestCase):
    c2kKnownValues = (
        (-100, 173.15),
        (0, 273.15),
        (50.5, 323.65),
        (155, 428.15),
        (300, 573.15)
    )

    def testconvertCelsiusToKelvin(self):
        print 'Testing that convertCelsiusToKelvin returns the correct known values'
        for c, k in self.c2kKnownValues:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(k, result)

    c2fKnownValues = (
        (-100, -148.00),
        (0, 32),
        (50.5, 122.9),
        (155, 311),
        (300, 572)
    )

    def testconvertCelsiusToFahrenheit(self):
        print 'Testing that convertCelsiusToFarenheit returns the correct known values'
        for c, f in self.c2fKnownValues:
            #print 'celcius', c
            #print 'far', f
            result = conversions.convertCelsiusToFahrenheit(c)
            #print 'result', result
            self.assertEqual(f, result)

    f2cKnownValues = (
        (-148,-100),
        (32, 0),
        (122.9, 50.5),
        (311, 155),
        (572, 300)
    )

    def testconvertFahrenheitToCelcius(self):
        print 'Testing that convertFahrenheitToCelcius returns the correct known values'
        for f, c in self.f2cKnownValues:
            result = conversions.convertFahrenheitToCelcius(f)
            self.assertEqual(c, result)

    f2kKnownValues = (
        (-148, 173.15),
        (32, 273.15),
        (122.9, 323.65),
        (311, 428.15),
        (572, 573.15)
    )

    def testconvertFarenheitToKelvin(self):
        print 'Testing that convertFarenheitToKelvin returns the correct known values'
        for f, k in self.f2kKnownValues:
            result = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(k, result)

    k2fKnownValues = (
        (173.15, -148),
        (273.15, 32),
        (323.65, 122.9),
        (428.15, 311),
        (573.15, 572)
    )

    def testconvertKelvinToFarenheit(self):
        print 'Testing that convertKelvinToFarenheit returns the correct known values'
        for k, f in self.k2fKnownValues:
            result = conversions.convertKelvinToFarenheit(k)
            self.assertEqual(f, result)

    k2cKnownValues = (
        (173.15, -100),
        (273.15, 0),
        (323.65, 50.5),
        (428.15, 155),
        (573.15, 300)
    )

    def testconvertKelvinToCelsius(self):
        print 'Testing that convertKelvinToCelsius returns the correct known values'
        for k, c in self.k2cKnownValues:
            result = conversions.convertKelvinToCelcius(k)
            self.assertEqual(c, result)

if __name__ == '__main__':
    unittest.main()