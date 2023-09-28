# 0x04-loops_conditions_and_parsing

# Bash Scripting Basics
This repository provides a guide on Bash scripting basics, covering topics such as creating SSH keys, using different types of loops and condition statements, and working with common command-line tools like `cut`. 

## Table of Contents
- [How to create SSH keys](#create-ssh-keys)
- [Advantage of using #!/usr/bin/env bash](#advantage-of-env-bash)
- [How to use loops](#use-loops)
- [How to use condition statements](#use-condition-statements)
- [How to use the cut command](#use-cut-command)
- [Comparison operators](#comparison-operators)

---

## Bash Basics

```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

#!/usr/bin/env bash

# While loop
while [ condition ]; do
    # code to execute
done

# Until loop
until [ condition ]; do
    # code to execute
done

# For loop
for item in list; do
    # code to execute
done

# If, Else, Elif
if [ condition ]; then
    # code to execute if condition is true
elif [ condition2 ]; then
    # code to execute if condition2 is true
else
    # code to execute if no conditions are true
fi

# Case
case $variable in
    pattern1)
        # code to execute for pattern1
        ;;
    pattern2)
        # code to execute for pattern2
        ;;
    *)
        # code to execute if no patterns match
        ;;
esac

# Cut command
cut -d' ' -f1-3 file.txt

# Comparison operators
# -eq: Equal to
# -ne: Not equal to
# -gt: Greater than
# -lt: Less than
# -ge: Greater than or equal to
# -le: Less than or equal to
