from typing import List, Dict, Set

class TwoHashMaps:
    def __init__(self, pattern: str, s: str) -> None:
        # 🛠️ Store the original inputs
        self.__pattern: str = pattern
        self.__s: str       = s
        
        # ✂️ Split the sentence into a list of individual words
        self.__words: List[str]     = self.__s.split()
        
        # 📏 Count how many words and how many letters we are working with
        self.__words_length: int    = len(self.__words)
        self.__pattern_length: int  = len(self.__pattern)

    def apply(self) -> bool:
        # 🚫 Quick check: If lengths don't match, they can never pair up perfectly!
        if self.__words_length != self.__pattern_length:
            return False
        
        # 🪞 The "Two-Way Mirror": One map for Word->Letter, one for Letter->Word
        word_to_letter_map: Dict = {}
        letter_to_word_map: Dict = {}

        # 🚶‍♂️ Walk through every word and letter pair one by one
        for current_index in range(self.__words_length):
            current_word: str   = self.__words[current_index]
            current_letter: str = self.__pattern[current_index]
            
            # 🤝 If BOTH the word and the letter are currently single (not in our maps)...
            if(
                word_to_letter_map.get(current_word,    None) is None   and
                letter_to_word_map.get(current_letter,  None) is None
            ):
                # 💍 Pair them up! Write it down in both dictionaries.
                word_to_letter_map[current_word]    = current_letter
                letter_to_word_map[current_letter]  = current_word
                
            # 💔 Otherwise, if they are already paired... check if either one is cheating!
            # (Note: Changed 'and' to 'or' here, because if EVEN ONE side doesn't match, it's a fail)
            elif(
                word_to_letter_map.get(current_word,    None) != current_letter  or
                letter_to_word_map.get(current_letter,  None) != current_word
            ):
                # 🙅‍♂️ Someone is breaking the rules! Not a valid pattern.
                return False
        
        # ✅ We checked every pair and no rules were broken!
        return True
    
    
class SingleHashMap:
    def __init__(self, pattern: str, s: str) -> None:
        # 🛠️ Setup is exactly the same as above
        self.__pattern: str = pattern
        self.__s: str       = s
        self.__words: List[str]     = self.__s.split()
        self.__words_length: int    = len(self.__words)
        self.__pattern_length: int  = len(self.__pattern)

    def apply(self) -> bool:
        # 🚫 Instant fail if the lengths don't match
        if self.__words_length != self.__pattern_length:
            return False
        
        # 📖 A single dictionary to map Letter -> Word
        letter_to_word_map: Dict    = {}
        # 🛑 A "watchlist" of words that are already taken by a letter
        used_words: Set[str]        = set()

        # 🚶‍♂️ Walk through the pairs
        for current_index in range(self.__words_length):
            current_word: str   = self.__words[current_index]
            current_letter: str = self.__pattern[current_index]

            # 🕵️‍♂️ Has this letter already been paired up before?
            if current_letter in letter_to_word_map: # (Note: Fixed from current_word to current_letter)
                # 💔 If yes, does its current partner match the one we recorded?
                if letter_to_word_map[current_letter] != current_word:
                    return False # 🙅‍♂️ It's trying to map to a different word!
            
            # 🌟 This is a brand new letter!
            else:
                # 🚨 But wait, is the word already taken by someone else?
                if current_word in used_words:
                    return False # 🙅‍♂️ Two different letters can't share the same word!
                
                # 💍 Both are free! Make the match and add the word to our "taken" list.
                letter_to_word_map[current_letter] = current_word
                used_words.add(current_word)
        
        # ✅ Perfect sync!
        return True
    