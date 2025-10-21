# Mini-Projects Explained

This document provides explanations for various mini-projects created as part of the 100 Days of Code challenge. Each project is a small, self-contained application designed to demonstrate specific programming concepts.

---

## `age_calc.py`

This Python script calculates the user's age in 5, 10, and 25 years.

**Purpose:**
To practice with user input, basic arithmetic operations, and f-string formatting.

**How it works:**

1. It prompts the user to enter their current age.
2. It calculates the future age by adding 5, 10, and 25 to the current age.
3. It prints out the user's age at these future points in time.

**Key Concepts Demonstrated:**

- `input()` function for user interaction.
- `int()` function for type conversion.
- Basic arithmetic (`+`).
- Formatted output using f-strings.

---

## `can_i_drive.py`

This Python script determines if a user is allowed to drive based on their age and whether they have a driver's license.

**Purpose:**
To illustrate conditional logic and the use of functions to structure code.

**How it works:**

1.  It prompts the user for their age and, if applicable, for their driver's license status.
2.  A function `check_driving_eligibility()` contains the core logic to evaluate the user's status.
3.  The main script calls this function with the user's data and prints the returned message.

**Key Concepts Demonstrated:**

- Defining and calling functions.
- `input()` function for user interaction.
- `int()` for type conversion and string methods (`.strip()`, `.lower()`).
- Conditional statements (`if`, `elif`, `else`).
- Returning values from a function.

---

## `euclidian_distance.py`

This Python script calculates the Euclidean distance between two points in 3D space.

**Purpose:**
To demonstrate the use of the `math` module and its functions.

**How it works:**

1. It defines two points as tuples.
2. It uses the `math.dist()` function to calculate the Euclidean distance between them.
3. It prints the result, formatted to three decimal places.

**Key Concepts Demonstrated:**

- Importing modules (`math`).
- Using functions from a module (`math.dist`).
- Tuples to represent data points.
- Formatted output using f-strings.

---

## `pizza_calculator.py`

This Python script calculates the cost per person for a pizza order, including a dynamic tip and a possible discount.

**Purpose:**
To demonstrate breaking down a problem into smaller functions and handling complex conditional logic.

**How it works:**

1.  It takes the pizza price and number of people as input.
2.  A function `determine_tip_percentage()` decides the tip based on the group size.
3.  A function `calculate_total_bill()` computes the final bill, including the tip and a conditional discount for large groups.
4.  The main script orchestrates the calls to these functions and prints the final price per person.

**Key Concepts Demonstrated:**

- Decomposing a problem into multiple functions (`determine_tip_percentage`, `calculate_total_bill`).
- `input()` for user input and type conversion (`float()`, `int()`).
- Complex conditional logic with `if`, `elif`, `else`.
- Returning values from functions and passing them to others.
- Formatted output using f-strings.

---

## `playlist.py`

This Python script manages a simple playlist of favorite songs.

**Purpose:**
To practice with lists and their methods.

**How it works:**

1. It initializes a list of favorite songs.
2. It asks the user to input a song.
3. It checks if the song is in the playlist and informs the user.
4. If the song is not in the playlist, it displays the current songs.
5. It demonstrates adding and removing items from the list.

**Key Concepts Demonstrated:**

- Lists for data storage.
- `in` operator to check for existence in a list.
- `enumerate()` to loop with an index.
- List methods: `append()`, `pop()`.
- `len()` to get the length of a list.

---

## `time_calc.py`

This Python script converts a given number of minutes into hours and remaining minutes.

**Purpose:**
To practice with integer division and the modulo operator.

**How it works:**

1. It prompts the user to enter a number of minutes.
2. It uses integer division (`//`) to find the number of hours.
3. It uses the modulo operator (`%`) to find the remaining minutes.
4. It prints the result in a user-friendly format, handling pluralization for "hour" and "minute".

**Key Concepts Demonstrated:**

- `input()` for user input.
- `int()` for type conversion.
- Integer division (`//`).
- Modulo operator (`%`).
- Conditional expressions within an f-string for pluralization.