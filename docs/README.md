
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Functions
## Calculate
calc(figure, function, size):
- calculate input figure size of area or perimeter
- figure - type of figure (circle, rectangle, triangle)
- function - type of function (area(), perimeter())
- size - size for each side of triangle, two sides for rectangle, radius for circle

## Area
Input data: radius or sides of the figure
- area(r) - for circle, r - radius
- area(a, b) - for rectangle, a and b are sides of rectangle
- area(a, b, c) - for triangle, a b c are sides of triangle
returns area of figure

## Perimeter
Input data: radius or sides of the figure
- perimeter(r) - for circle, r - radius
- perimeter(a, b) - for rectangle, a and b are sides of rectangle
- perimeter(a, b, c) - for triangle, a b c are sides of triangle
returns area of figure


# History of changes
commit e98848624d91e5cc04fd994f0306ce3aa190d0f1 (HEAD -> documentation)
Author: Alexandr <alergilm@gmail.com>
Date:   Mon Oct 7 16:52:51 2024 +0000

    Added documentation to source files

commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added
