import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystr = re.sub(r'[^a-zA-Z0-9]', '', s)
        mystr = mystr.lower()
        print(mystr[::-1],mystr)
        if mystr[::-1] == mystr:
            return True
        return False