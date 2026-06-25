# py_echo_validator
---
Write a function:
```
def py_echo_validator(s: str) -> bool:
```
Returns True if s is a palindrome, ignoring:
    * Case (uppercase/lowercase)
    * Non-alphanumeric characters
Returns False otherwise.

### Examples
```
py_echo_validator("Was it a car or a cat I saw?") → True
py_echo_validator("tab a cat")                     → False
py_echo_validator("A man, a plan, a canal: Panama") → True
py_echo_validator("No lemon, no melon")           → True
```
