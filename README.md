# Week 3 Assignment: Conditions and Loops

## Files in this repository

- **grade_reporter.py** - A program that grades a list of scores using if/elif/else, counts passes and fails, and calculates the average.
- **bug_hunt.py** - A fixed program that adds numbers 1 to 5 using a while loop. Contains three `# BUG:` comments explaining each bug that was fixed.

## Reflection

The hardest bug to find in Part B was the third one — the loop condition. Unlike the first two bugs that produced clear error messages (SyntaxError and TypeError), the third bug let the program run without any error. The program printed "Sum of 1 to 5 is: 10" instead of 15. I knew something was wrong because the expected answer was 15, but the output was 10. By tracing the loop manually (1+2+3+4 = 10, but 5 was missing), I realized the condition `count < 5` stopped the loop before adding 5. Changing it to `count <= 5` fixed the problem.