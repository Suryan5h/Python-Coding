class Solution:
  # Capitalize (title() case ) for each word in the string
  #   Input : i love programming
  #   Output : I Love Programming
    def transform(self, s):
        # code here
        s = s.split(" ")
        s = [i.title() for i in s]
        ans = " ".join(s)
        return ans
