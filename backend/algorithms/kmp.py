def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    matches = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches
