# Contest #2  
**Date:** February 8, 2025  

Welcome to **Contest #2**! This contest features a set of problems focusing on **string manipulation** and **number manipulation**. The problems are designed to challenge your problem-solving skills while keeping the difficulty balanced. Below, you'll find the list of problems along with their links and a brief summary of the contest.

---

## Problems

### [A. Assem's Secret Code](https://codeforces.com/gym/586622/problem/A)
<details>
<summary><strong>Problem Summary</strong></summary>

- **Focus:** String Manipulation  
- **Description:**  
  Assem has a secret code `s`, a three-letter word hidden in plain sight. Your task is to determine if this word, regardless of capitalization, spells out "YES". For example, "yES", "Yes", or "yes" are all valid.  

- **Input:**  
  - The first line contains an integer `t` (1 ≤ `t` ≤ 10<sup>3</sup>) — the number of test cases.  
  - Each test case consists of a string `s` of three characters. Each character is either an uppercase or lowercase English letter.  

- **Output:**  
  - For each test case, output "YES" if `s` can be transformed into "YES" by adjusting the case of its letters. Otherwise, output "NO".  
  - The output is case-insensitive (e.g., "yES", "yes", and "Yes" are all valid positive responses).  

- **Examples:**  
  | Input | Output |  
  |-------|--------|  
  | `10`<br>`YES`<br>`yES`<br>`yes`<br>`Yes`<br>`YeS`<br>`Noo`<br>`orZ`<br>`yEz`<br>`Yas`<br>`XES` | `YES`<br>`YES`<br>`YES`<br>`YES`<br>`YES`<br>`NO`<br>`NO`<br>`NO`<br>`NO`<br>`NO` |  

- **Note:**  
  The first five test cases contain strings like "YES", "yES", "yes", "Yes", and "YeS". All of these are valid because they can be transformed into "YES" by adjusting the case of their letters.  
</details>

### [B. The Special Paintbrush](https://codeforces.com/gym/586622/problem/B)
<details>
<summary><strong>Problem Summary</strong></summary>

- **Focus:** String Manipulation, Greedy Algorithm  
- **Description:**  
  Lusekello has a row of `n` cells, some black (`'B'`) and some white (`'W'`). She wants to turn the entire strip completely white using a special paintbrush. The brush can paint a continuous segment of cells, turning all black cells in that segment white. Your task is to find the **minimum length** of the segment needed to make all cells white.  

- **Input:**  
  - The first line contains an integer `t` (1 ≤ `t` ≤ 10<sup>4</sup>) — the number of test cases.  
  - For each test case:  
    - The first line contains an integer `n` (1 ≤ `n` ≤ 10) — the length of the strip.  
    - The second line contains a string `s` of length `n`, consisting of `'W'` (white) and `'B'` (black). At least one cell is black.  

- **Output:**  
  - For each test case, output a single integer — the minimum length of a continuous segment to paint white so that all cells become white.  

- **Examples:**  
  | Input | Output |  
  |-------|--------|  
  | `8`<br>`6`<br>`WBBWBW`<br>`1`<br>`B`<br>`2`<br>`WB`<br>`3`<br>`BBW`<br>`4`<br>`BWWB`<br>`6`<br>`BWBWWB`<br>`6`<br>`WWBBWB`<br>`9`<br>`WBWBWWWBW` | `4`<br>`1`<br>`1`<br>`2`<br>`4`<br>`6`<br>`4`<br>`7` |  

- **Note:**  
  - In the first test case (`WBBWBW`), the minimum segment length is **4**. You need to paint cells 2 to 5 (1-based indexing).  
  - The problem ensures that at least one cell is black, so the answer is always valid.  
</details>

### [C. Sura Loves Coding](https://codeforces.com/gym/586622/problem/C)
<details>
<summary><strong>Problem Summary</strong></summary>

- **Focus:** String Manipulation, Encoding/Decoding  
- **Description:**  
  Sura has created a unique encoding method called **Sveta encoding**. It works by repeatedly selecting the **median letter** of a word, writing it down, and removing it until the word is empty. Your task is to **reverse this process** and reconstruct the original word from its encoded version.  

- **Encoding Process:**  
  1. The **median letter** is:  
     - The exact middle letter if the word length is odd.  
     - The left of the two middle letters if the word length is even.  
  2. Write down the median letter, remove it from the word, and repeat until the word is empty.  
  3. The encoded sequence is the order of the chosen letters.  

  **Example:**  
  Encoding `"volga"` results in `"logva"`:  
  - `volga` → `l` (remove `'l'`) → `voga`  
  - `voga` → `o` (remove `'o'`) → `vga`  
  - `vga` → `g` (remove `'g'`) → `va`  
  - `va` → `v` (remove `'v'`) → `a`  
  - `a` → `a` (last letter remains)  

- **Input:**  
  - The first line contains an integer `n` (1 ≤ `n` ≤ 2000) — the length of the encoded word.  
  - The second line contains the string `s` of length `n` — the encoded word (lowercase English letters).  

- **Output:**  
  - Print the original word that Sura encoded.  

- **Examples:**  
  | Input | Output |  
  |-------|--------|  
  | `5`<br>`logva` | `volga` |  
  | `2`<br>`no` | `no` |  
  | `4`<br>`abba` | `baba` |  

- **Note:**  
  - In the first example, Sura encoded `"volga"` into `"logva"`.  
  - In the second example, the word and its encoding are the same (`"no"`).  
  - In the third example, Sura encoded `"baba"` into `"abba"`.  
</details>

### [D. Mugisho and Rufeyda](https://codeforces.com/gym/586622/problem/D)
<details>
<summary><strong>Problem Summary</strong></summary>

- **Focus:** Number Theory, Divisibility  
- **Description:**  
  Mugisho loves numbers with exactly `n` digits, while Rufeyda only likes numbers divisible by `t`. Your task is to find a number that satisfies both conditions:  
  1. It has exactly `n` digits.  
  2. It is divisible by `t`.  
  If no such number exists, print `-1`.  

- **Input:**  
  - A single line containing two integers:  
    - `n` (1 ≤ `n` ≤ 100) — the number of digits.  
    - `t` (2 ≤ `t` ≤ 10) — the divisor.  

- **Output:**  
  - Print a positive `n`-digit number divisible by `t` without leading zeros.  
  - If no such number exists, print `-1`.  
  - If multiple answers exist, any valid number is acceptable.  

- **Examples:**  
  | Input | Output |  
  |-------|--------|  
  | `3 2` | `712` |  

- **Note:**  
  - In the example, `712` is a 3-digit number divisible by `2`.  
  - The problem ensures that `t` is small (2 ≤ `t` ≤ 10), making it easier to find valid numbers.  
</details>

### [E. The Beautiful String](https://codeforces.com/gym/586622/problem/E)
<details>
<summary><strong>Problem Summary</strong></summary>

- **Focus:** String Manipulation, Substring Search  
- **Description:**  
  Sara has a binary string `s` (consisting of `'0'` and `'1'`). She performs `q` operations to modify the string, and after each operation, she wants to know if the substring `"1100"` appears in the string. Your task is to answer her queries efficiently.  

- **Input:**  
  - The first line contains an integer `t` (1 ≤ `t` ≤ 10<sup>4</sup>) — the number of test cases.  
  - For each test case:  
    - The first line contains the string `s` (1 ≤ `|s|` ≤ 2⋅10<sup>5</sup>).  
    - The second line contains an integer `q` (1 ≤ `q` ≤ 2⋅10<sup>5</sup>) — the number of queries.  
    - The next `q` lines contain two integers `i` (1 ≤ `i` ≤ `|s|`) and `v` (`v` ∈ {`0`, `1`}), describing the query. Here, `i` is the position to update, and `v` is the new value (`0` or `1`).  

  **Constraints:**  
  - The sum of `|s|` across all test cases does not exceed 2⋅10<sup>5</sup>.  
  - The sum of `q` across all test cases does not exceed 2⋅10<sup>5</sup>.  

- **Output:**  
  - For each query, output `"YES"` if the substring `"1100"` is present in the string after the update; otherwise, output `"NO"`.  
  - The output is case-insensitive (e.g., `"yEs"`, `"yes"`, `"Yes"`, and `"YES"` are all valid).  

- **Examples:**  
  | Input | Output |  
  |-------|--------|  
  | `4`<br>`100`<br>`4`<br>`1 1`<br>`2 0`<br>`2 0`<br>`3 1`<br>`1100000`<br>`3`<br>`6 1`<br>`7 1`<br>`4 1`<br>`111010`<br>`4`<br>`1 1`<br>`5 0`<br>`4 1`<br>`5 0`<br>`0100`<br>`4`<br>`3 1`<br>`1 1`<br>`2 0`<br>`2 1` | `NO`<br>`NO`<br>`NO`<br>`NO`<br>`YES`<br>`YES`<br>`NO`<br>`NO`<br>`YES`<br>`YES`<br>`YES`<br>`NO`<br>`NO`<br>`NO`<br>`NO` |  

- **Note:**  
  - In the first test case, after each update, the string never contains the substring `"1100"`.  
  - In the second test case, the string initially contains `"1100"`, and some updates preserve or reintroduce it.  
  - The problem requires efficient handling of updates and queries due to the large constraints.  
</details>
---
 

---

## How to Participate  
1. Visit the problem links above to access the contest problems.  
2. Solve the problems and submit your solutions on the platform.  
3. Share your feedback or solutions in the repository's discussion section.

---

Good luck, and happy coding! 🚀