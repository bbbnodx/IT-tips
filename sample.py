def is_palindrome(s):
    '''
    Palindrome determination

    Parameters
    ----------
    s : str
        target string.

    Returns
    -------
    bool
        is s palindrome?
    '''

    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz ':
                letters += c
            return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

if __name__ == '__main__':
    statement = 'Some men interpret nine memos.'
    print('')
    print('About to return {} for {}'.format(is_palindrome(statement), statement))
