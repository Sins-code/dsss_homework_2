import random

# TODO
#  better readability: variables and functions
#  comments: add comments to code
#  docstrings: for every function
#  error handling: at least one try/except on user input
#  fix bugs: with unit tests


def get_random_integer(min, max):
    """ Returns a random integer between a minimum and maximum value.
    Args:
        min (int): The minimum value of returned integer.
        max (int): The maximum value of returned integer.

    Returns:
        int: random integer
    """
    try:
        assert type(min) == int
    except AssertionError:
        print("Wrong input type")
    return random.randint(min, max)


def select_random_operation():
    """ Returns randomly either the mathematical operation '+', '-' or '*'.

        Returns:
            str: The randomly selected operation.
        """
    return random.choice(['+', '-', '*'])


def compute_math_result(number1, number2, operation):
    """ Computes the result of the mathematical operation between two numbers.
        Args:
            number1 (int): First number.
            number2 (int): Second Number.
            operation (str): Mathematical operation.

        Returns:
            int: Result of mathematical operation.
        """
    # Create problem statement
    problem = f"{number1} {operation} {number2}"
    # Depending on operation compute result and return it
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer


def math_quiz():
    """ Runs a mathematical quiz on the command line."""
    score = 0
    amount_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # run quiz
    for _ in range(amount_questions):
        # get two random numbers and an operation
        number_1 = get_random_integer(1, 10); number_2 = get_random_integer(1, 5); operation = select_random_operation()

        # get problem statement and solution
        problem, correct_answer = compute_math_result(number_1, number_2, operation)
        print(f"\nQuestion: {problem}")
        # collect user answer
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            useranswer = None

        # compare answers
        if useranswer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # print final score
    print(f"\nGame over! Your score is: {score}/{amount_questions}")


if __name__ == "__main__":
    math_quiz()
