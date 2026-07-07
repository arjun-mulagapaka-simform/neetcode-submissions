class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ै"
        s = "ढ".join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == "ै":
            return []
        strs = s.split("ढ")
        return strs