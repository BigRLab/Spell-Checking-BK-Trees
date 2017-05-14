# Fuzzy searching for spell checking
---
This project builds a BK-Tree from the dictionary.txt file and checks the first book in the Books folder for spelling mistakes.

### String Metric Techniques
---
The current version has two string metrics:
- Levenshtein Distance. Caters for edit operations such as insertion, deletion and swapping.
- Hamming Distance. Only takes into consideration the mismatching letters.

### Updates
---
#### v1.1
Added parallelism and stability throughout. Radius and loading dictionary from file bool has been moved to the definitions dictionary in the utils.py file.
