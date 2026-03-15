from solutions.two_pointers.valid_palindrome import Solution


def test_basic():
    assert Solution().isPalindrome("racecar")


def test_not():
    assert not Solution().isPalindrome("asdf")


def test_one():
    assert Solution().isPalindrome("a")


def test_uppercase():
    assert Solution().isPalindrome("RaCeCar")
