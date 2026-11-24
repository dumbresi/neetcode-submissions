class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        rev=''
        for i in range(len(s)):
            rev+=s[len(s)-i-1]
        print(s)
        print(rev)
        if rev==s:
            return True
        return False
        