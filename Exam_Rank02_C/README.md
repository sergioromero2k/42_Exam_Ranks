# Exam RANK02- C

A curated collection of exercises that may appear in the **Exam 02** of the 42 School common core.

All functions were written by me. If you're a student, I strongly recommend reading each exercise carefully, attempting it on your own first, and only then checking the solution. Good luck.

---

## Level 1

Basic C functions focused on string manipulation, character transformation, and bitwise operations. A good warm-up for the exam — most of these are short but require clean, precise code.

| | | | |
|---|---|---|---|
| first_word | fizzbuzz | putstr | ft_strcpy |
| ft_strlen | ft_swap | repeat_alpha | rev_print |
| rot_13 | rotone | search_and_replace | ulstr |
| last_word | max | print_bits | reverse_bits |
| snake_to_camel | swap_bits | union | wdmatch |

- **fizzbuzz** — the classic. Print numbers 1–100, replacing multiples of 3 with "Fizz", 5 with "Buzz", and both with "FizzBuzz".
- **rot_13** — Caesar cipher shifted by 13. Each letter maps to the one 13 positions ahead in the alphabet.
- **print_bits / reverse_bits / swap_bits** — bitwise manipulation exercises. You'll need to work at the byte level without any arithmetic shortcuts.
- **snake_to_camel** — converts `snake_case` strings to `CamelCase`. Straightforward but easy to get wrong at the boundaries.

---

## Level 2

Slightly more involved string functions, closer to what you'd find in a real `libft`. Expect to handle edge cases and write careful pointer logic.

| | | | |
|---|---|---|---|
| alpha_mirror | camel_to_snake | do_op | ft_atoi |
| ft_strcmp | ft_strcspn | ft_strdup | ft_strpbrk |
| ft_strrev | ft_strspn | is_power_of_2 | str_capitalizer |
| tab_mult | | | |

- **ft_atoi** — convert a string to an integer, handling signs, leading whitespace, and non-digit characters correctly.
- **do_op** — takes three arguments (two numbers and an operator) and performs the corresponding arithmetic operation.
- **is_power_of_2** — returns 1 if a number is a power of 2, 0 otherwise. Solvable in one line with bitwise logic.
- **tab_mult** — prints a formatted multiplication table for a given number.

---

## Level 3

Algorithms and data structures start appearing here. You'll work with linked lists, ranges, and number theory.

| | | | |
|---|---|---|---|
| add_prime_sum | epur_str | expand_str | ft_atoi_base |
| ft_list_size | ft_range | ft_rrange | hidenp |
| lcm | paramsum | pgcd | rstr_capitalizer |

- **ft_atoi_base** — like `ft_atoi`, but converts a string from any given base (e.g. hex, binary) to an integer.
- **ft_range / ft_rrange** — allocate and return an array of integers between two values, in ascending or descending order.
- **lcm / pgcd** — compute the least common multiple and greatest common divisor. Classic number theory, simple recursive solutions work well.
- **ft_list_size** — returns the number of elements in a linked list. Requires understanding the `t_list` struct.

---

## Level 4

The hardest group. Dynamic memory, recursion, sorting, and more complex algorithms. These require both correctness and efficiency.

| | | | |
|---|---|---|---|
| flood_fill | fprime | ft_itoa | ft_list_foreach |
| ft_list_remove_if | ft_split | rev_wstr | rostring |
| sort_int_tab | sort_list | | |

- **flood_fill** — given a 2D grid and a starting point, fill all connected cells of the same value. A classic BFS/DFS problem.
- **ft_itoa** — convert an integer to a string, including handling of negative numbers and `INT_MIN`.
- **ft_split** — split a string by a delimiter character and return a null-terminated array of substrings. Memory management is key.
- **fprime** — print all prime factors of a given number, in ascending order.
- **sort_int_tab** — sort an array of integers. Any correct sorting algorithm works, but bubble sort is usually the fastest to implement under pressure.

---

**56 exercises across 4 levels.**