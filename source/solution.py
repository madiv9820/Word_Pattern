from .approaches import TwoHashMaps, SingleHashMap

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 🛠️ Initialize both of our strategic approaches with the given inputs
        approach_01 =   TwoHashMaps(pattern = pattern, s = s)
        approach_02 = SingleHashMap(pattern = pattern, s = s)
        
        # 🚀 Execute our chosen approach! 
        # Here we are using SingleHashMap (approach_02) since it's slightly more optimized.
        ans: bool = approach_02.apply()
        
        # ✅ Return the final verdict (True if it's a perfect match, False if it breaks the rules)
        return ans