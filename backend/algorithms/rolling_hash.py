def rolling_hash(text, pattern, base=256, mod=101):
    m, n = len(pattern), len(text)
    h, t, d = 1, 0, 0

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        t = (t * base + ord(text[i])) % mod
        d = (d * base + ord(pattern[i])) % mod

    for i in range(n - m + 1):
        if t == d and text[i:i + m] == pattern:
            return True
        if i < n - m:
            t = (t - h * ord(text[i])) * base + ord(text[i + m])
            t %= mod
            if t < 0:
                t += mod
    return False
