class CascadingPalindrome:
    """
    This class encapsulates the functionality to find cascading palindromes.
    """

    def __init__(self, input_string):
        """
        Initializes an instance of the CascadingPalindrome class with the provided input string.

        - input_string (str): The input string to be analyzed for cascading palindromes.
        """
        self.input_string = input_string

    def is_palindrome(self, substring):
        """
        Checks if a given substring is a palindrome.
    
        substring (str): The substring to be checked.
        
        Returns:
        - bool: True if the substring is a palindrome, False otherwise.
        """
        return substring == substring[::-1]

    def get_cascading_palindrome(self):
        """
        Finds the longest cascading palindrome within the input string.
    
        Returns:
        - str: The longest cascading palindrome found in the input string.
        """
        input_words = self.input_string.split()
        longest_cascading_palindrome = ""

        for i in range(len(input_words)):
            for j in range(i, len(input_words)):
                current_substring = " ".join(input_words[i:j + 1])
                if self.is_palindrome(current_substring) and len(current_substring) > len(longest_cascading_palindrome):
                    longest_cascading_palindrome = current_substring

        return longest_cascading_palindrome


def main():
    """
    The main entry point of the script. It takes user input, validates it, and then finds and displays the longest cascading palindrome.
    """
    while True:
        input_string = input("Enter the input string: ")

        """Validate the input string"""
        if not input_string:
            print("The input string cannot be empty.")
        elif not isinstance(input_string, str):
            print("The input string must be a string.")
        else:
            break

    cascading_palindrome = CascadingPalindrome(input_string).get_cascading_palindrome()

    if not cascading_palindrome:
        print("There is no cascading palindrome in the input string.")
    else:
        print(f"The cascading palindrome is: {cascading_palindrome}")


if __name__ == "__main__":
    main()
