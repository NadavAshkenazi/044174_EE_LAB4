
def is_palindrome(s):
    l = [i.lower() for i in list(s) if i.isalpha()]
    s = "".join(l)
    l.reverse()
    reversedS = "".join(l)
    return s == reversedS



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert(is_palindrome("abs") is False)
    assert (is_palindrome("") is True)
    assert (is_palindrome("a") is True)
    assert (is_palindrome("abba ") is True)
    assert (is_palindrome("a man, a plan, a canal: Panama") is True)
    assert (is_palindrome("Delia saw I was ailed") is True)
    assert (is_palindrome("abcdefghji") is False)
