#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Six - PTesting Refactor"""

import conversions_refactored

def main():
    value = conversions_refactored.convert('Celcius','Farenheit',155)

    print 'Converted Value: ',value

if __name__ == '__main__':
    main()