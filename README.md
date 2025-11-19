# A 50-Project Path to Python Mastery: A Structured Curriculum

This document provides a 50-project curriculum designed as an intensive sprint to build a comprehensive, professional-grade Python portfolio. The projects are structured to move from foundational scripts to complex, architecturally-sound applications.

This list is a set of project briefs, or specifications, not tutorials. The user's directive—"I can google if I don't know"—is the guiding principle. This curriculum provides the "what" and "why" for each project; the "how" is left to research. This approach is designed to build the single most important skill for a developer: finding, evaluating, and implementing solutions independently.

The project timelines (e.g., 1 hour) are not stopwatches but scoping mechanisms. A "1-hour" project is a small, self-contained script with a single conceptual goal, designed to be completed in one sitting. A "4-6 hour" advanced project involves complex integration and, most importantly, a professional project architecture.

The curriculum is divided into three parts:
*   **Part I: The Foundation:** Focuses on core syntax, standard libraries, and single-file scripts.
*   **Part II: Building Competence:** Focuses on building modular projects with classes (OOP), external APIs, GUIs, and data tools.
*   **Part III: Professional Specialization:** Focuses on integrating multiple concepts into applications that adhere to professional, industry-standard project structures.

---

## Part I: The Foundation (20 Beginner Projects)

**Objective:** Master Python's core syntax, standard libraries, and the flow of a simple script. All projects in this section should be a single `.py` file. The folder structure for all beginner projects can be a single directory containing the main file: `project_name/main.py`.

### 1. Mad Libs
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Create a simple "Mad Libs" game. The script will prompt the user to enter various words (nouns, verbs, adjectives), and then use these inputs to construct and print a formatted, humorous story. This project focuses on user `input()`, `print()`, and f-string formatting.
*   **Possible Folder Structure:** `mad_libs/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* User provides a series of prompts: `Enter a noun:...`, `Enter a verb:...`.
    *   *Output:* A formatted string, e.g., "The [noun] decided to [verb] on the [adjective] cat."

### 2. Guess the Number (Computer)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** The computer generates a secret random number within a range (e.g., 1 to 20). The user then tries to guess the number. The script provides feedback ("Too high," "Too low," or "Correct!"). This project uses the `random` module, `while` loops, and `if/elif/else` conditional logic.
*   **Possible Folder Structure:** `guess_the_number/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* User enters a number: `Guess a number (1-20): 10`.
    *   *Output:* Feedback: `Too low! Guess again: 15`.

### 3. Guess the Number (User)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A reversal of the previous game. The user thinks of a secret number, and the computer tries to guess it. The user provides feedback ("high," "low," "correct"). This project forces a different logical approach (like a binary search) for the computer's guessing strategy.
*   **Possible Folder Structure:** `user_guesses/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* User provides feedback: `Is your number 50? (h/l/c): h`.
    *   *Output:* Computer's next guess: `Is your number 75? (h/l/c):...`.

### 4. Rock, Paper, Scissors
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Implement the classic game against the computer. The script should get the user's choice, have the computer make a random choice, and then determine and announce the winner based on the rules. This reinforces `random.choice()` and handling user input validation (e.g., what if the user types "rockk"?).
*   **Possible Folder Structure:** `rock_paper_scissors/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter your choice (rock, paper, scissors): rock`.
    *   *Output:* `Computer chose paper. You lose!`

### 5. Countdown Timer
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Create a simple command-line countdown timer. The user enters a number of seconds, and the script counts down to zero, printing the remaining time each second. This project introduces the `time` module, specifically the `time.sleep()` function, within a `while` loop.
*   **Possible Folder Structure:** `countdown_timer/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter seconds: 5`.
    *   *Output:* `5...`, `4...`, `3...`, `2...`, `1...`, `BLAST OFF!`.

### 6. Password Generator
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Write a script that generates a random password of a user-specified length. The password should include a mix of letters (upper and lower), numbers, and symbols. This project uses the `random` and `string` modules. It's a great exercise in `for` loops, list manipulation, and `random.shuffle()`.
*   **Possible Folder Structure:** `password_generator/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter password length: 12`.
    *   *Output:* `Your new password is: Gt8!#pW_9z$K`.

### 7. QR Code Encoder
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** This project is the first to use an external library. The user provides a URL or text string, and the script generates a QR code image and saves it to a file (e.g., `qr.png`). This requires learning how to `pip install qrcode` and use the library.
*   **Possible Folder Structure:** `qr_encoder/main.py`, `qr_encoder/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter text or URL to encode: https://www.google.com`.
    *   *Output:* A new file named `qr.png` in the project directory.

### 8. Simple Calculator (CLI)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Create a command-line calculator that takes two numbers and an operator (e.g., +, -, *, /) from the user. It should then perform the calculation and print the result. This project focuses on defining simple functions (e.g., `add(a, b)`) and parsing user input.
*   **Possible Folder Structure:** `cli_calculator/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter first number: 10`, `Enter operator (+, -, *, /): *`, `Enter second number: 5`.
    *   *Output:* `Result: 50`.

### 9. Palindrome Checker
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Write a script that checks if a user-provided word or phrase is a palindrome (reads the same forwards and backward). The script should ignore spaces and capitalization. This is a classic exercise in string manipulation (slicing and methods like `.lower()` and `.replace()`).
*   **Possible Folder Structure:** `palindrome_checker/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter a word: Madam`.
    *   *Output:* `Yes, 'Madam' is a palindrome.`
    *   *Input:* `Enter a word: Hello`.
    *   *Output:* `No, 'Hello' is not a palindrome.`

### 10. Word Count Tool
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Create a script that reads a text file (`input.txt`) and counts the total number of words. A more advanced version could also count the frequency of each word. This introduces basic file I/O using `with open(...) as f:` and using string methods like `.split()`.
*   **Possible Folder Structure:** `word_count/main.py`, `word_count/input.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* A file `input.txt` containing "Hello world hello".
    *   *Output:* `Total words: 3`.

### 11. Find and Replace (File I/O)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Write a script that prompts the user for a filename, a word to find, and a word to replace it with. The script should read the file, perform the replacements, and write the new text to a new file (e.g., `output.txt`). This expands on file I/O, combining reading and writing.
*   **Possible Folder Structure:** `find_replace/main.py`, `find_replace/sample.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Filename: sample.txt`, `Find: "apple"`, `Replace: "orange"`.
    *   *Output:* A file `output.txt` with all instances of "apple" replaced.

### 12. Email Slicer
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A simple script that takes an email address from the user and "slices" it into its username and domain. This is another string manipulation exercise, focusing on finding the "@" symbol and using string splitting or indexing.
*   **Possible Folder Structure:** `email_slicer/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter your email: user@example.com`.
    *   *Output:* `Username: user`, `Domain: example.com`.

### 13. Dice Rolling Simulator
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Simulate rolling one or more dice. The user specifies how many dice to roll and how many sides each die has (e.g., two 6-sided dice). The script should print the result of each roll and the total. Uses the `random.randint()` function.
*   **Possible Folder Structure:** `dice_roller/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `How many dice? 2`, `How many sides? 6`.
    *   *Output:* `Roll 1: 4`, `Roll 2: 3`, `Total: 7`.

### 14. BMI Calculator
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Create a Body Mass Index (BMI) calculator. The script prompts the user for their weight (in kg) and height (in meters). It then calculates and prints their BMI. This involves basic mathematical formulas and converting `input()` strings to floats.
*   **Possible Folder Structure:** `bmi_calculator/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter weight (kg): 70`, `Enter height (m): 1.75`.
    *   *Output:* `Your BMI is: 22.86`.

### 15. Simple To-Do List (CLI)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A basic command-line to-do list. The script should use a loop that repeatedly asks the user what they want to do ("add", "view", "remove", "quit"). Tasks are stored in a simple Python list. The program ends when the user types "quit". This focuses on list methods (`.append()`, `.remove()`) and `while` loops.
*   **Possible Folder Structure:** `cli_todo/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `> add Buy milk`, `> view`.
    *   *Output:* `1. Buy milk`.
    *   *Input:* `> quit`.
    *   *Output:* `Goodbye!`

### 16. Currency Converter (Static)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A simple currency converter with static, hard-coded exchange rates (e.g., 1 USD = 0.9 EUR). The user specifies an amount, the "from" currency, and the "to" currency. The script calculates and prints the converted amount. This focuses on using dictionaries to store the rates.
*   **Possible Folder Structure:** `currency_converter/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Amount: 100`, `From (USD/EUR): USD`, `To (USD/EUR): EUR`.
    *   *Output:* `100 USD is 90 EUR`.

### 17. Hangman (Simple)
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A simplified version of Hangman. The script has a single, hard-coded secret word. The user guesses letters. The script shows the "hanged man" (using ASCII art for each wrong guess) and the word with correctly guessed letters filled in (`_ _ T _ _`). The game ends on a win or loss.
*   **Possible Folder Structure:** `hangman/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Secret word is: _ _ _ _ _`, `Guess a letter: e`.
    *   *Output:* `_ e _ _ e`, `You have 5 lives left`.

### 18. FizzBuzz
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** The classic "FizzBuzz" problem. Write a script that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For multiples of both 3 and 5, print "FizzBuzz". This is a core test of `for` loops and conditional logic (`if/elif/else`).
*   **Possible Folder Structure:** `fizzbuzz/main.py`
*   **Inputs and Expected Outputs:**
    *   *Output:* `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz,...`

### 19. Generate Text File
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** A script that generates a large text file. The user specifies a filename and a number of lines. The script should then write "This is line X" for X from 1 to the specified number. This is useful for practicing file I/O with large files and `for` loops.
*   **Possible Folder Structure:** `text_generator/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Filename: large_file.txt`, `Lines: 1000`.
    *   *Output:* A file `large_file.txt` with 1000 lines of text.

### 20. Build "Snake" in the Terminal
*   **Difficulty Level:** Beginner (Est. 1 Hour)
*   **Project Description:** Recreate the classic snake game in the command line. This project uses the `curses` standard library (do not use Pygame) to control the terminal cursor and read non-blocking key presses. It reinforces data structures (a list for the snake's body) and the main game loop. This is a "capstone" for the beginner section.
*   **Possible Folder Structure:** `terminal_snake/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* Keyboard arrow keys.
    *   *Output:* A real-time game rendered with ASCII characters in the terminal window.

---

## Part II: Building Competence (20 Intermediate Projects)

**Objective:** Move from single scripts to modular projects. This section focuses on Object-Oriented Programming (OOP), external libraries, APIs, GUIs, and the basics of data science. The folder structures will now be multi-file.

### Subgroup A: Object-Oriented Programming (OOP) Foundations

#### 21. Simple Banking System
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Create a command-line banking system using OOP principles. You will create a `Client` class (with attributes like name, account number, balance, and methods like `deposit()`, `withdraw()`, `check_balance()`) and a `Bank` class that manages a dictionary of Client objects. The `main.py` file will run the CLI menu to interact with the bank.
*   **Possible Folder Structure:**
    ```text
    banking_system/
    ├── main.py     # (Runs the CLI menu, instantiates Bank)
    ├── bank.py     # (Contains the Bank class)
    └── client.py   # (Contains the Client class)
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* CLI commands: `create_account John`, `deposit John 100`, `balance John`.
    *   *Output:* `Account created.`, `Deposited $100.`, `Current Balance: $100`.

#### 22. Library Management System
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Implement a library management system using OOP. Create a `Book` class (attributes: title, author, "is_borrowed") and a `Library` class (attributes: a list of Book objects; methods: `add_book()`, `borrow_book()`, `return_book()`, `view_books()`). The `main.py` provides the user menu.
*   **Possible Folder Structure:**
    ```text
    library_system/
    ├── main.py     # (CLI menu)
    ├── library.py  # (Contains Library class)
    └── book.py     # (Contains Book class)
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* User selects "1" (Add Book), then enters "1984" and "George Orwell".
    *   *Output:* `Book '1984' added successfully`.
    *   *Input:* User selects "3" (Borrow Book), enters "1984".
    *   *Output:* `You have borrowed '1984'`.

#### 23. Simple E-commerce Store
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Model a simple e-commerce system. Create a `Product` class (name, price, quantity_in_stock) and a `ShoppingCart` class. The `ShoppingCart` class should have methods like `add_item(product, quantity)`, `remove_item(product)`, and `calculate_total()`. This project focuses on class composition (a ShoppingCart "has" Products).
*   **Possible Folder Structure:**
    ```text
    e_commerce/
    ├── main.py        # (Simulates adding items to a cart)
    ├── product.py     # (Contains Product class)
    └── shopping_cart.py # (Contains ShoppingCart class)
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* (In main.py) `cart.add_item(product_A, 2)`, `cart.add_item(product_B, 1)`.
    *   *Output:* `print(cart.calculate_total())` -> `55.97`.

#### 24. University Management System (Inheritance)
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a system to model a university, focusing on OOP inheritance. Create a base `Person` class. Then, create `Student` and `Professor` classes that inherit from Person. Student could have attributes like `student_id` and `courses` (a list). Professor could have `employee_id` and `department`.
*   **Possible Folder Structure:**
    ```text
    university/
    ├── main.py       # (Creates and prints student/professor objects)
    └── models.py     # (Contains Person, Student, Professor classes)
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* (In main.py) `s1 = Student("Alice", 123)`, `p1 = Professor("Dr. Bob", 789, "Physics")`.
    *   *Output:* `print(s1.name)` -> Alice, `print(p1.department)` -> Physics.

### Subgroup B: API Integration and Web Clients

#### 25. CLI Weather App
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Create a command-line tool that fetches and displays the weather for a user-specified city. This requires using the `requests` library to call a free weather API (like OpenWeatherMap), parsing the JSON response, and printing a formatted, human-readable forecast. This project teaches API keys (using `.env` files), JSON parsing, and HTTP error handling.
*   **Possible Folder Structure:** `weather_cli/main.py`, `weather_cli/requirements.txt`, `weather_cli/.env`
*   **Inputs and Expected Outputs:**
    *   *Input:* `python main.py "London"`
    *   *Output:* `London, UK: 15°C, Light Rain`.

#### 26. API Client Wrapper (OOP + API)
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build on the previous project by creating an OOP wrapper for the API. Create a `WeatherAPIClient` class. The class should be initialized with an API key. It should have methods like `get_forecast(city)` that handle the requests call and JSON parsing internally. This abstracts the API logic, making it reusable.
*   **Possible Folder Structure:**
    ```text
    weather_client/
    ├── main.py         # (Imports and uses the client)
    ├── client.py       # (Contains WeatherAPIClient class)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* (In main.py) `client = WeatherAPIClient(api_key)`, `forecast = client.get_forecast("Tokyo")`.
    *   *Output:* `print(forecast)` -> `Tokyo, JP: 22°C, Clear Sky`.

#### 27. GitHub Repository Fetcher
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Use the `requests` library to interact with the GitHub API. The script should prompt the user for a GitHub username and then fetch and list all of that user's public repositories, including the repository name and its URL.
*   **Possible Folder Structure:** `github_fetcher/main.py`, `github_fetcher/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `Enter GitHub username: octocat`.
    *   *Output:* A list: `Spoon-Knife (https://github.com/octocat/Spoon-Knife)`, `Hello-World (https://github.com/octocat/Hello-World)`...

#### 28. Web Scraper with BeautifulSoup
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a scraper to get specific data from a web page. Use `requests` to get the HTML of a page (e.g., a "Hacker News" page) and `BeautifulSoup` to parse the HTML. Extract all the article titles and their links and print them to the console.
*   **Possible Folder Structure:** `web_scraper/main.py`, `web_scraper/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* (None, URL is hard-coded in the script).
    *   *Output:* A list of titles and URLs from the target page.

### Subgroup C: GUI and Game Development

#### 29. Tkinter Calculator
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a graphical calculator using Python's built-in `tkinter` library. This project involves creating a GUI with buttons for numbers (0-9) and operators (+, -, *, /), a display screen (a Label or Entry widget), and functions to handle button-click events and perform the calculations.
*   **Possible Folder Structure:** `tkinter_calc/main.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* User clicks buttons "1", "0", "+", "5", "=".
    *   *Output:* The GUI display updates to show "15".

#### 30. Pygame Snake
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Recreate the classic game Snake using `pygame`. This requires OOP: you will likely have a `Snake` class (managing its body segments, direction) and a `Food` class. The `main.py` will contain the main game loop, which handles events (key presses), updates game state, and draws to the screen.
*   **Possible Folder Structure:**
    ```text
    pygame_snake/
    ├── main.py
    ├── snake.py       # (Snake class)
    ├── food.py        # (Food class)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* Keyboard arrow keys.
    *   *Output:* A graphical game window where the user controls a snake.

#### 31. Pygame Pong
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Implement the classic "Pong" game using `pygame`. This will involve creating `Paddle` objects (controlled by the user) and a `Ball` object. The logic will need to handle ball movement, collision detection with walls and paddles, and score-keeping.
*   **Possible Folder Structure:**
    ```text
    pygame_pong/
    ├── main.py
    ├── ball.py        # (Ball class)
    ├── paddle.py      # (Paddle class)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* "W" and "S" keys for one paddle, Up and Down arrows for the other.
    *   *Output:* A graphical two-player Pong game.

#### 32. Simple Photo Editor (GUI)
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Use `tkinter` for the GUI and the Pillow (PIL) library for image processing. The application should allow a user to open an image file, and then apply simple filters like "Grayscale," "Blur," or "Sharpen," and finally save the new image.
*   **Possible Folder Structure:** `photo_editor/main.py`, `photo_editor/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* User clicks "Open" and selects `image.jpg`. User clicks "Grayscale".
    *   *Output:* The image in the GUI window turns to grayscale. User can "Save As".

### Subgroup D: Data Science and Web Apps

#### 33. Basic Flask Web App
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a simple "microblog" with Flask. Create a `main.py` that runs the app. It should have at least two routes: `/` (the main page, which shows posts) and `/add` (a page with a form to add a new post). For this intermediate project, the posts can be stored in a simple global list.
*   **Possible Folder Structure:**
    ```text
    flask_blog/
    ├── main.py
    ├── templates/
    │   ├── index.html
    │   └── add_post.html
    ├── static/
    │   └── style.css
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* User navigates to `http://127.0.0.1:5000/add` and submits a form.
    *   *Output:* The user is redirected to `/`, which now displays the new post.

#### 34. Flask Weather App
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Combine the skills from projects 25 and 33. Create a Flask web app where a user can type a city name into a form. When the form is submitted, the app's backend calls the weather API (using your `WeatherAPIClient` class), gets the forecast, and then renders an HTML template displaying that forecast.
*   **Possible Folder Structure:** (Similar to Flask Blog, but adds client.py)
    ```text
    flask_weather/
    ├── main.py
    ├── client.py        # (The WeatherAPIClient from project 26)
    ├── templates/
    │   ├── index.html
    │   └── forecast.html
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* User enters "Tokyo" in an HTML form and clicks "Submit".
    *   *Output:* A new page `forecast.html` is rendered, showing "Tokyo, JP: 22°C...".

#### 35. Exploring Hacker News Posts (Pandas)
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Use the `pandas` library to analyze a CSV file of Hacker News posts. This project, which can be done in a Jupyter Notebook, involves loading the data (`pd.read_csv`), filtering for specific post types (e.g., Ask HN vs. Show HN), and performing aggregate calculations (e.g., find the mean number of comments for each post type).
*   **Possible Folder Structure:**
    ```text
    hn_analysis/
    ├── analysis.ipynb
    ├── data/
    │   └── hacker_news.csv
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `hacker_news.csv`.
    *   *Output:* A Jupyter Notebook with data tables and matplotlib plots answering questions like "Do 'Ask HN' or 'Show HN' posts get more comments?"

#### 36. Simple Scikit-Learn Model
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build your first "real" end-to-end machine learning model. Use the "Wine Quality" dataset (a common CSV dataset). Load it with `pandas`, separate features (X) and target (y), perform a `train_test_split`, and then train a `RandomForestClassifier` from scikit-learn to predict the wine quality. Print the model's accuracy.
*   **Possible Folder Structure:**
    ```text
    wine_model/
    ├── model.ipynb
    ├── data/
    │   └── wine.csv
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `wine.csv`.
    *   *Output:* A printed accuracy score: `Model Accuracy: 0.68`.

#### 37. Face Detection with OpenCV
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Use the `opencv-python` library to perform simple face detection on an image. This requires finding a pre-trained Haar Cascade XML file (which OpenCV provides). The script should load an image, load the cascade, detect faces (which returns coordinates), and then draw rectangles around the detected faces and display the image.
*   **Possible Folder Structure:** `face_detector/main.py`, `face_detector/image.jpg`, `face_detector/haarcascade_frontalface_default.xml`, `face_detector/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `image.jpg` (containing faces).
    *   *Output:* A window pops up showing the same image, but with blue rectangles drawn around the faces.

#### 38. Reddit Bot (Simple)
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a simple bot that monitors a specific subreddit for a keyword. Using the `praw` (Python Reddit API Wrapper) library, the bot should scan new comments. If a comment contains a specific phrase (e.g., "!hello"), the bot should automatically reply (e.g., "Hello to you too!").
*   **Possible Folder Structure:** `reddit_bot/main.py`, `reddit_bot/requirements.txt`, `reddit_bot/.env`
*   **Inputs and Expected Outputs:**
    *   *Input:* A new comment on Reddit containing "!hello".
    *   *Output:* The bot posts a reply: "Hello to you too!".

#### 39. Tic-Tac-Toe AI
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Build a Tic-Tac-Toe game where the human plays against an "unbeatable" computer AI. This project introduces the **minimax algorithm**, a recursive algorithm used for decision-making in two-player games. This is a significant step up from a simple game.
*   **Possible Folder Structure:** `tictactoe_ai/main.py`, `tictactoe_ai/game.py`
*   **Inputs and Expected Outputs:**
    *   *Input:* User makes moves in the terminal.
    *   *Output:* The computer makes optimal counter-moves, resulting in a draw or a win for the AI.

#### 40. Markov Chain Text Composer
*   **Difficulty Level:** Intermediate (Est. 2-3 Hours)
*   **Project Description:** Create a script that generates new text in the style of an original author. The script reads a large text file (e.g., a public domain book), builds a Markov chain model (a dictionary where keys are words and values are a list of words that follow), and then generates new sentences by "walking" the chain.
*   **Possible Folder Structure:** `markov_text/main.py`, `markov_text/corpus.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `corpus.txt` (e.g., the text of "Alice in Wonderland").
    *   *Output:* A paragraph of semi-coherent, computer-generated text, e.g., "Alice said to the Caterpillar, who was sitting on the table, and the Queen...".

---

## Part III: Professional Specialization (10 Advanced Projects)

**Objective:** Build portfolio-defining capstone projects. The focus here is less on "new" concepts and more on integration and, critically, professional project architecture. These projects must be structured for maintainability, testability, and scalability, following industry-standard templates.

### Subgroup A: Advanced Web APIs (FastAPI)

#### 41. FastAPI CRUD API with Database
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Build a full CRUD (Create, Read, Update, Delete) API for a resource (e.g., "Books" or "Users"). This project must use **FastAPI** for the API logic, **Pydantic** models for data validation and serialization (`schemas.py`), and **SQLAlchemy** with a SQLite database for persistence (`models.py`). Create separate files for different concerns.
*   **Possible Folder Structure:**
    ```text
    fastapi_crud_db/
    ├── main.py         # (Imports router, runs app)
    ├── crud.py         # (Functions to interact with DB, e.g., get_user)
    ├── database.py     # (Engine, SessionLocal, Base)
    ├── models.py       # (SQLAlchemy models)
    ├── schemas.py      # (Pydantic models)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `POST /books/` with JSON `{"title": "1984", "author": "George Orwell"}`.
    *   *Output:* A 200 OK response with the created object's JSON.
    *   *Input:* `GET /books/1`.
    *   *Output:* `{"id": 1, "title": "1984", "author": "George Orwell"}`.

#### 42. Scalable FastAPI Application
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** This project is purely about professional API architecture. Refactor a simple API into the scalable "Bigger Applications" structure recommended by the official FastAPI documentation. This involves using `APIRouter` to split your path operations into multiple files (e.g., `users.py`, `items.py`) and including them in the main app object.
*   **Possible Folder Structure:** (This structure is the goal of the project)
    ```text
    scalable_fastapi/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py         # (Main FastAPI app, includes routers)
    │   ├── dependencies.py # (Shared dependencies)
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── items.py    # (APIRouter for /items)
    │   │   └── users.py    # (APIRouter for /users)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `GET http://127.0.0.1:8000/users/`.
    *   *Output:* JSON from the `users.py` router.

#### 43. FastAPI with User Authentication
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Extend the CRUD API from project 41 to include user authentication. Implement `/token` endpoint using OAuth2 with password flow. Secure the CRUD endpoints so that (for example) only authenticated users can create items. This involves password hashing (`passlib`), JWT token creation, and FastAPI's `Depends` system for protected routes.
*   **Possible Folder Structure:** (Extends project 41, adding authentication logic)
    ```text
    fastapi_auth/
    ├── main.py
    ├── auth.py         # (Token/OAuth2 logic, user helpers)
    ├── crud.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `POST /token` with form data `username=...` & `password=...`.
    *   *Output:* JSON `{"access_token": "...", "token_type": "bearer"}`.
    *   *Input:* `POST /books/` without a valid Authorization header.
    *   *Output:* `401 Unauthorized`.

### Subgroup B: Data Science and Machine Learning

#### 44. Standardized Data Science Project (EDA)
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Perform a comprehensive Exploratory Data Analysis (EDA) on a complex dataset (e.g., Titanic or a Kaggle dataset). The primary requirement is to use the **cookiecutter-data-science** template structure. This forces a professional workflow: data in `data/raw`, cleaning scripts in `src/`, and analysis in `notebooks/`.
*   **Possible Folder Structure:** (Mandated by the project)
    ```text
    eda_project/
    ├── data/
    │   ├── raw/         # (Original data.csv)
    │   ├── processed/   # (Cleaned data.csv)
    ├── notebooks/
    │   └── 1.0-eda.ipynb # (Analysis notebook)
    ├── reports/
    │   └── figures/     # (Plots saved from notebook)
    ├── src/
    │   ├── __init__.py
    │   ├── data.py      # (Script to process data)
    │   └── features.py  # (Script to build features)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* `data/raw/train.csv`.
    *   *Output:* A fully populated `notebooks/1.0-eda.ipynb` with insights and plots, and a `data/processed/train.csv` file generated by `src/data.py`.

#### 45. Laptop Price Predictor
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Build an end-to-end regression model to predict laptop prices. Use the `cookiecutter-data-science` structure. This involves loading the data, extensive feature engineering (e.g., one-hot encoding for "Company," extracting numbers from "Ram"), training a model (RandomForestRegressor or XGBoost), and evaluating it using Root Mean Squared Error (RMSE).
*   **Possible Folder Structure:** (Uses the `cookiecutter-data-science` structure as above).
*   **Inputs and Expected Outputs:**
    *   *Input:* `data/raw/laptops.csv`.
    *   *Output:* A `models/laptop_price_regressor.joblib` file and a `notebooks/` file reporting the final Test RMSE.

#### 46. Detecting Fake News
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Implement the "Detecting Fake News" project, a text classification task. The project must use `TfidfVectorizer` (for feature extraction from text) and `PassiveAggressiveClassifier` (a specific online learning algorithm), as specified in the source repository. This forces you to learn these specific scikit-learn components.
*   **Possible Folder Structure:** (Uses the `cookiecutter-data-science` structure).
*   **Inputs and Expected Outputs:**
    *   *Input:* `data/raw/news.csv` (with "text" and "label" columns).
    *   *Output:* A classification report (precision, recall, F1-score) and a confusion matrix saved in `reports/figures/`.

#### 47. Keras CNN Image Classifier
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Build, train, and evaluate a Convolutional Neural Network (CNN) using `tf.keras`. Classify images from a standard dataset like MNIST or CIFAR-10. The project must follow a modular, OOP-based structure, separating data loading, model definition, and training into different modules.
*   **Possible Folder Structure:** (Mandated by the project)
    ```text
    cnn_classifier/
    ├── config_files/
    │   └── config.ini     # (Hyperparams: epochs, batch_size)
    ├── data_loader/
    │   └── data_loader.py # (Class to load and prep tf.data)
    ├── model/
    │   └── cnn_model.py   # (Function/class defines Keras model)
    ├── main.py            # (Main training/evaluation script)
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* The `config.ini` file and the dataset (e.g., MNIST).
    *   *Output:* Console logs of training/validation accuracy per epoch, and a final "Test Accuracy: 99.1%".

#### 48. Face Recognition System
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Build a system that recognizes faces, not just detects them. This involves a multi-step pipeline: (1) Use `opencv` to detect faces in images. (2) Use a deep learning model (e.g., `face_recognition` library) to create a 128-dimension "encoding" for each face. (3) Compare these encodings to a database of "known" face encodings to find a match.
*   **Possible Folder Structure:**
    ```text
    face_recognition/
    ├── main.py            # (Runs the recognition on new image)
    ├── create_encodings.py # (Scans 'known_faces' dir)
    ├── known_faces/
    │   ├── person1.jpg
    │   └── person2.jpg
    ├── encodings.pickle
    └── requirements.txt
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* An unknown image with `person1.jpg` in it.
    *   *Output:* The image is displayed with a label "person1" over the face.

### Subgroup C: Advanced Python Concepts

#### 49. Asynchronous URL Checker
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** Master asynchronous programming, a key topic in advanced Python. Write a script to check the HTTP status of 100 URLs from a text file. First, write it sequentially using `requests`. Second, rewrite it concurrently using `asyncio` and `httpx`. The goal is to compare the total execution time and understand the power of async.
*   **Possible Folder Structure:** `async_checker/main.py`, `async_checker/urls.txt`, `async_checker/requirements.txt`
*   **Inputs and Expected Outputs:**
    *   *Input:* `urls.txt` (containing 100 URLs).
    *   *Output:* A printout: `Checked 100 URLs (Sequential) in 15.2s.`, `Checked 100 URLs (Async) in 1.1s.`

#### 50. Build a Simple Blockchain
*   **Difficulty Level:** Advanced (Est. 4-6 Hours)
*   **Project Description:** A capstone project in pure Python and OOP. Create a `Block` class (attributes: index, timestamp, data, previous_hash, hash) and a `Blockchain` class (attributes: a list of Blocks). Implement a proof_of_work algorithm (e.g., finding a hash that starts with "0000") and a `hash_block` method. This demonstrates a deep understanding of OOP and cryptographic concepts.
*   **Possible Folder Structure:**
    ```text
    py_chain/
    ├── main.py         # (Runs simulation)
    ├── block.py        # (Block class)
    ├── blockchain.py   # (Blockchain class)
    ```
*   **Inputs and Expected Outputs:**
    *   *Input:* (In main.py) `my_chain.add_block("Transaction 1")`, `my_chain.add_block("Transaction 2")`.
    *   *Output:* The script prints the entire valid, hashed blockchain to the console, showing the linked "previous_hash" values.

---

## Conclusion: Leveraging Your 50-Project Portfolio

Completing this 50-project sprint is a significant achievement. This curriculum is designed to take a developer from basic scripting to architecting and building professional, specialized applications. The journey moves from simple, single-file scripts in Part I, to building modular, object-oriented libraries in Part II, and culminates in constructing professionally-structured, integrated systems in Part III.

### How to Present This Portfolio

The 10 advanced projects should be the centerpiece of a professional portfolio. When presenting them, the `README.md` for each project is as important as the code. Highlight the **Architecture**: Do not just "upload the code." Explicitly state in the README.md why the project is structured the way it is.

*   **For FastAPI projects:** "This project follows the official FastAPI 'Bigger Applications' layout to ensure scalability and separation of concerns using APIRouter."
*   **For Data Science projects:** "This data science project adheres to the cookiecutter-data-science template, separating raw data (`data/raw`), processed data (`data/processed`), and analysis (`notebooks/`) for a reproducible workflow."
*   **For Deep Learning projects:** "This Keras project uses a modular, OOP-based structure to separate data loading (`data_loader/`), model definition (`model/`), and training (`main.py`)."

This demonstrates intent, maturity, and an understanding of how to work on a professional development team.