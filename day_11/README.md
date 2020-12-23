# Day 11 - prefer catch-all unpacking over slicing

---

Please check the day11.py to know to the topic from the code perspective.

## Things to remember:

-   Unpacking assignments may use a starred expression to catch all values that weren't assigned to the other parts of the unpacking pattern into a list
-   Starred expressions may appear in any position, and the will always become a list containing the zero or more values they receive
-   When dividing a list into non-overlaping pieces, catch-all unpacking is much less error prone that slicing and indexing
