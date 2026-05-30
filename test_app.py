from app import is_palindrome

def is_palindrome_true():
    assert is_palindrome("madam") == True
    assert is_palindrome("kavak") == True

def is_palindrome_false():
    assert is_palindrome("madm") == False
    assert is_palindrome("kavk") == False
