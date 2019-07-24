# To-Do-Proj (In Progress)

## Project Description
The goal of this project is to imitate a to-do list with a focus on presenting flexible display functions (sort, day/month/year, multilevels, etc.) and storage of various to-do item based on their status (checked/unchecked, special tasks, etc.). 


## Technical Description

> **1st step:** Program bare codes to show basic functions such as add, remove, check, uncheck.

***Program used:*** `Visual Studio Code`

***Shown in:*** `fxn.py`


> **2nd step:** Mock up a visual prototype for the application

**Program used:** `Adobe XD`

**Shown in:** `file.xd`

> **3rd step:** In progress...


## Functions Description

**Add:**
- Available parameters for 1 argument: `str, int, list, or tuple`
- Available parameters for 2 arguments: `pair of (str/int, str/int) and (list/tuple, list/tuple)`
    - _1st arg = index, 2nd arg = str, **interchangable_
    - _If both args contain strictly numbers, default to 1st arg = index, 2nd arg = values_

**Remove:**
- Available parameters for 1 argument: `str, int, list, tuple`
    - _All integers will default to indices_
    - _All strings will default to values_