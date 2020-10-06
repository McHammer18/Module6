"""
Morgan Christensen

Module6: Validate_input)in_functions
prompts user for name and score then prints values

10/06/20
"""


def score_input(test_name, test_score = 0, invalid_message="Invalid test score try again"):
    """
    Function that accepts params and returns a string
    :param test_name: the name of the test taker
    :type test_name String
    :param test_score: the score that they recieved
    :type test_score int
    :param invalid_message: Message displayed when an invalid score is provided
    :type invalid_message: String
    :return: formmated string with test_name, and test_score
    :rtype String
    """
    #print("{}: {}".format(test_name, test_score))
    return "{}: {}".format(test_name, test_score)


if __name__ == '__main__':
    print(score_input("morgan", 65))