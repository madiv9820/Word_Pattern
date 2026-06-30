# [✨ The Word Pattern Challenge ✨](https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150)

Think of this problem like cracking a secret code where your pattern and sentence must speak the exact same language! 🕵️‍♂️💬

The core question asks if a given string **`s`** follows a specific **`pattern`**. Here, "follow" means finding a full match by establishing a "bijection" between the letters and the words. That is just a fancy math term for a perfect, two-way mirror relationship. 🪞✨

Think of it like pairing up dancers for a dance! To solve it, you need to verify two golden rules:

### 🎭 The Rules of the Dance

- **1️⃣ Strict Loyalty (Letter ➡️ Word):** Each letter in your pattern (like 'a') must hold hands with exactly one word in the string (like "dog"). If 'a' is dancing with "dog," it can never dance with "cat". It must stick with its partner forever! 🤝

- **2️⃣ Exclusive Partners (Word ➡️ Letter):** The words are just as picky! Each word can only have one partner letter. If "dog" is already dancing with 'a', no other letter (like 'b') can try to cut in and dance with "dog". 🚫💃 Absolutely no two letters can map to the same word, and no two words can map to the same letter.

### 💡 How It Works in Action

- **✅ A Perfect Match:** If your pattern is **`"abba"`** and your string is **`"dog cat cat dog"`**, it outputs true. The perfect pairs are made because **`'a'`** successfully maps to **`"dog"`** , and **`'b'`** successfully maps to **`"cat"`**.

- **❌ The Cheater:** If your pattern is **`"abba"`** but your string is **`"dog cat cat fish"`**, it outputs false. Why? Because the second **`'a'`** at the end tries to dance with **`"fish"`** instead of its loyal partner **`"dog"`**.

- **❌ The Double-Dater:** If your pattern is **`"aaaa"`** but your string is **`"dog cat cat dog"`**, it outputs false. Why? Because **`'a'`** tries to unfairly claim both **`"dog"`** and **`"cat"`** as its partners.

### 📏 The Boundaries (Constraints)

- Your pattern will be short and sweet (between **`1 and 300`** characters) and only use lower-case English letters.
- Your string sentence will be up to **`3000`** characters long, containing only lowercase letters and single spaces.
- It is perfectly clean—no sneaky leading or trailing spaces, and all words are separated by exactly one space.

In short: If every letter has exactly one unique word, and every word has exactly one unique letter, you have a perfect match! ✅

----
### 🪞 Approach 1: The "Two-Way Mirror" (Two Hash Maps)

#### 💡 Intuition
Think of this approach like pairing up partners for a dance. Every letter (like **`'a'`**) must hold hands with exactly one word (like **`"dog"`**).

- Strict Loyalty: If **`'a'`** dances with **`"dog"`**, it can never dance with **`"cat"`**.
- Exclusive Partners: If **`"dog"`** is already dancing with **`'a'`**, no other letter can cut in.

To enforce this, we use two separate dictionaries (our "Two-Way Mirror"). One dictionary remembers the mapping from *Letter ➡️ Word*, and the other remembers the mapping from 8. If either side tries to break the rules, we catch them instantly! 🙅‍♂️

#### 🛠️ Steps
1. **Split & Count:** Break the string **`s`** into a list of individual words.

2. **The Fast Fail:** If the number of letters in the pattern doesn't perfectly match the number of words, they can't possibly pair up perfectly. Return **`False`**.

3. **Walk the Pairs:** Loop through the letters and words side-by-side.

4. **Make the Match:** If both the letter and word are brand new (not in our dictionaries), pair them up and record the relationship in both maps.

5. **Catch the Cheaters:** If they are already in the dictionaries, check their recorded partners. If the letter's mapped word or the word's mapped letter doesn't match the current pair, the pattern is broken. Return **`False`**.

6. **Success:** If we check every pair without any rule breaks, return **`True`**! ✅

#### 💻 Pseudocode
```
function two_hash_maps(pattern, s):
    words = split(s, " ")
    
    if length(pattern) != length(words):
        return False
        
    word_to_letter = {}
    letter_to_word = {}
    
    for i from 0 to length(words) - 1:
        current_word = words[i]
        current_letter = pattern[i]
        
        if current_word not in word_to_letter AND current_letter not in letter_to_word:
            word_to_letter[current_word] = current_letter
            letter_to_word[current_letter] = current_word
            
        else if word_to_letter[current_word] != current_letter OR letter_to_word[current_letter] != current_word:
            return False
            
    return True
```
#### ⏱️ Complexity Analysis
- Time Complexity: $\mathcal{O}(N)$, where $N$ is the total length of the string **`s`**. Splitting the string takes $\mathcal{O}(N)$ time, and iterating through the words/characters takes $\mathcal{O}(W)$ time (where $W$ is the number of words). Dictionary lookups are lightning fast at $\mathcal{O}(1)$.

- Space Complexity: $\mathcal{O}(N)$, because we store the split words in an array, and our two dictionaries will store at most $W$ unique word/letter pairings.

### 🕵️‍♂️ Approach 2: The "Partner Watchlist" (Single Hash Map + Set)

#### 💡 Intuition
This approach streamlines our logic. Instead of keeping two massive record books, what if we just keep one primary dictionary for the *Letter ➡️ Word* mapping, and a simple "Watchlist" (a Set) to track which words are already taken? 🔒

If a letter is new, we just quickly check our Watchlist. If the word is on the list, it means another letter has already claimed it—a clear violation! It’s a cleaner, highly efficient way to manage uniqueness.

#### 🛠️ Steps
1. **Split & Count:** Just like before, split the string into words.

2. **The Fast Fail:** If lengths don't match, return **`False`**.

3. **Prepare the Tools:** Create one dictionary (**`letter_to_word_map`**) and one Set (**`used_words`** watchlist).

4. **Walk the Pairs:** Loop through each letter and word.

5. **Verify Existing Letters:** If we've seen the letter before, ensure it still maps to the exact same word. If not, return **`False`**.

6. **Check New Letters:** If the letter is brand new, check the Watchlist. Is the current word already claimed by someone else?

    - If yes: Return **`False`** (No sharing allowed!).
    - If no: Record the new match in the dictionary and add the word to the Watchlist.

7. **Success:** If we make it to the end smoothly, return **`True`**! ✅

#### 💻 Pseudocode
```
function single_hash_map(pattern, s):
    words = split(s, " ")
    
    if length(pattern) != length(words):
        return False
        
    letter_to_word = {}
    used_words_watchlist = Set()
    
    for i from 0 to length(words) - 1:
        current_word = words[i]
        current_letter = pattern[i]
        
        if current_letter in letter_to_word:
            if letter_to_word[current_letter] != current_word:
                return False
        else:
            if current_word in used_words_watchlist:
                return False 
            
            letter_to_word[current_letter] = current_word
            used_words_watchlist.add(current_word)
            
    return True
```

#### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of string **`s`**. String splitting is $\mathcal{O}(N)$ and we do a single pass over the elements. Both hash map and hash set lookups happen in $\mathcal{O}(1)$ average time.

- **Space Complexity:** $\mathcal{O}(N)$, because we store the array of words, one dictionary, and one set. While the theoretical memory boundary is the same as Approach 1, this method usually has a slightly smaller memory footprint in practice because storing a single string in a Set has less overhead than storing key-value pairs in a second dictionary.

Here is a quick and clear comparison table breaking down the two approaches! 🚀

| Feature / Aspect | 🪞 Approach 1: Two Hash Maps | 🕵️‍♂️ Approach 2: Single Hash Map + Set |
| --- | --- | --- |
| **Analogy** | The "Two-Way Mirror" | The "Partner Watchlist" |
| **Data Structures Used** | Two Dictionaries (`Dict`) | One Dictionary (`Dict`), One Hash Set (`Set`) |
| **Mapping Strategy** | Records *Letter ➡️ Word* **and** *Word ➡️ Letter* explicitly. | Records *Letter ➡️ Word* explicitly, but just tracks if a Word is "taken". |
| **Validation Logic** | Checks if both partners point to each other. If either side is unfaithful, it fails. | Checks if a Letter points to the right Word. If it's a new Letter, it checks if the Word is already on the taken list. |
| **Time Complexity** | **$\mathcal{O}(N)$** - Lightning fast, single pass with $\mathcal{O}(1)$ dictionary lookups. | **$\mathcal{O}(N)$** - Lightning fast, single pass with $\mathcal{O}(1)$ dictionary/set lookups. |
| **Space Complexity** | **$\mathcal{O}(N)$** - Stores every unique pairing twice (once in each dictionary). | **$\mathcal{O}(N)$** - Stores mappings once in the dictionary, and just the word strings in the Set. |
| **Memory Efficiency** | 🧱 Slightly heavier in practice due to the overhead of maintaining two full key-value dictionaries. | ⚡ Slightly lighter in practice because storing a single string in a Set has less overhead than a full Dictionary entry. |
| **Code Cleanliness** | Very explicit and easy to conceptualize directly from the definition of a "bijection". | More streamlined logic; prevents redundancy by not storing the reverse mapping entirely. |

#### 🏆 Which one to choose?

Both are perfectly optimal for an interview setting!

* Choose **Approach 1** if you want the logic to visually map exactly to the mathematical definition of a bijection (it's very easy to explain).
* Choose **Approach 2** if you want to show off a slightly more optimized, memory-conscious architecture by recognizing that a Set is enough to enforce uniqueness!
---