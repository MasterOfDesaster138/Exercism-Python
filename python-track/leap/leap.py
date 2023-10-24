"""
Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

```text
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
```
```text
für jedes Jahr, das gleichmäßig durch 4 teilbar ist
  außer für jedes Jahr, das durch 100 teilbar ist
    es sei denn, das Jahr ist auch durch 400 teilbar
```

For example, 1997 is not a leap year, but 1996 is.
1900 is not a leap year, but 2000 is.
"""

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
        
