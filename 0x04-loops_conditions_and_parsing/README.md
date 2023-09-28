# Bash Scripting Basics

This repository provides a guide on Bash scripting basics, covering topics such as creating SSH keys, using different types of loops and condition statements, and working with common command-line tools like `cut`. 

## Table of Contents

1. [Creating SSH Keys](#creating-ssh-keys)
2. [Advantages of `#!/usr/bin/env bash` over `#!/bin/bash`](#advantages-of-env-bash)
3. [Working with Loops: `while`, `until`, and `for`](#working-with-loops)
4. [Conditional Statements: `if`, `else`, `elif`, and `case`](#conditional-statements)
5. [Using the `cut` Command](#using-the-cut-command)
6. [File Comparison Operators](#file-comparison-operators)

---

## Creating SSH Keys

To create SSH keys, follow these steps:

1. Open your terminal.
2. Use the command `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"` to generate a new SSH key.
3. Follow the prompts to set a passphrase (optional).
4. Your keys will be generated and stored in `~/.ssh` by default.

For more detailed instructions, refer to [GitHub's guide on generating SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## Advantages of `#!/usr/bin/env bash` over `#!/bin/bash`

Using `#!/usr/bin/env bash` is advantageous because it allows for better portability across different systems. It locates the Bash interpreter dynamically using the system's `PATH`, ensuring the script runs with the user's preferred Bash version.

## Working with Loops: `while`, `until`, and `for`

- **`while` Loop**: Executes a block of code as long as a specified condition is true.
  
  Example:
  ```bash
  while [ condition ]; do
      # code to be executed
  done
# 0x04-loops_conditions_and_parsing

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
