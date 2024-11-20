# 2048 (Single Line) 💻

## Description 💬
This programming task involves emulating the mechanics of the game 2048 along a single horizontal line. The function `slide_line` is designed to take an array of integers and either slide and merge its elements to the left or right. 

The function prototype is:
```c
int slide_line(int *line, size_t size, int direction);

-line: the array to manipulate.
size: the number of elements in the array.
direction: specifies the slide direction, defined by the macros SLIDE_LEFT and SLIDE_RIGHT.
A successful operation returns 1, while a failure returns 0. The implementation does not permit dynamic memory allocation, ensuring that the function operates strictly within the bounds of pre-allocated memory.


#Task 📚
0. Slide Line
The goal of this task is to reproduce the 2048 game mechanics on a single horizontal line.

Given an array of integers, we want to be able to slide and merge it to the left or to the right. Identical numbers, if they are contiguous or separated by zeros, should be merged.

Requirements:
Write a function that slides and merges an array of integers.
Prototype: int slide_line(int *line, size_t size, int direction);
Parameters:
line: points to an array of integers containing size elements, which must be slid and merged in the direction represented by direction.
direction:
SLIDE_LEFT
SLIDE_RIGHT
If the direction is invalid, the function must fail.
Return:
1 upon success.
0 upon failure.
Macros:
SLIDE_LEFT
SLIDE_RIGHT
These must be defined in slide_line.h.
Memory:
No dynamic memory allocation (malloc, calloc, etc.) is allowed.

alex@~/slide_line$ gcc -Wall -Wextra -Werror -pedantic -o 0-slide_line 0-main.c 0-slide_line.c
alex@~/slide_line$ ./0-slide_line L 2 2 0 0
Line: 2, 2, 0, 0
Slide to the left
Line: 4, 0, 0, 0

alex@~/slide_line$ ./0-slide_line R 2 2 2 2
Line: 2, 2, 2, 2
Slide to the right
Line: 0, 0, 4, 4


Author ✒️
Saber Younes
