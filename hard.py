#hard 2
# given a string s. You can convert s to a palindrome by adding characters in front of it.Return the shortest palindrome you can find by performing this transformation

def shortest_palindrome(s: str) -> str:
    rev_s = s[::-1]
    for i in range(len(s)):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s



#Example 1
s="aacecaaa"
print(shortest_palindrome(s))

# Example 2
s = "abcd"
print(shortest_palindrome(s))

