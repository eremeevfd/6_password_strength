# 6_password_strength
Thank you for using my password ranking script.
This script evaluates your password by score *from* __1__ *to* __10__
## Quick Start
Unpack and run 'password_strength.py'.
## Typical output
<pre>Enter your password: 123asaSSD--
Your password strength score is: 9</pre>
## Algorithm
Script reads your password and then checks for.
- Whether your password is not in blacklist it gets 1 score.
- Length
 - less than 8 grants 0 score
 - more than 8 but less than 13 grants 1 score
 - more than 13 grants 2 score
- Digits
 - 0 digits grant 0 score
 - 1 digit grants 1 score
 - 2 or more digits grant 2 score
- Lowercase grants 1 score
- Uppercase
 - 0 uppercases grant 0 score
 - 1 uppercase grants 1 score
 - 2 or more uppercases grant 2 score
- Symbols
 - 0 symbols grant 0 score
 - 1 symbols grants 1 score
 - 2 symbols grant 2 score
 
