#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
# first solution
"""def triangle(a, b, c):
    if a == b:
        if a == c and b == c: return 'equilateral'
        return 'isosceles'
    elif b == c:
        if a == b and a == c: return 'equilateral'
        return 'isosceles'
    elif a == c:
        if a == b and b == c: return 'equilateral'
        return 'isosceles'
    return 'scalene'
"""
# alternative solution using sets: # Could store a, b and c in a set and check the len of the set to know the amount of unique sides
def triangle(a, b, c):
    sides = set([a, b, c])
    desc_sides = sorted([a, b, c], reverse=True)    # added sortign to make error handling easier
    for side in sides:
        if side <= 0: raise TriangleError

    if len(sides) == 1: return 'equilateral'

    elif len(sides) == 2:
        if desc_sides[1] * 2 <= desc_sides[0]: raise TriangleError
        return 'isosceles'

    if desc_sides[1] + desc_sides[2] <= desc_sides[0]: raise TriangleError
    return 'scalene'
#"""

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
