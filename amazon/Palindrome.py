def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < (len(s) // 2 + 1):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True



def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    if len(s) < 2:
        return s

    max_size = 0
    temp = ""
    lo = -1
    for i in range(len(s)):
        j = i
        k = i
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1

        if max_size < k - j - 1:
            lo = j + 1
            max_size = k - j - 1

        j = i
        k = i+1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if max_size < k - j - 1:
            lo = j + 1
            max_size = k - j - 1

    return s[lo:lo + max_size]


if __name__ == '__main__':
    print(longestPalindrome("abccba"))
