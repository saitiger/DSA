class Solution:
    def removeAllDuplicates(self, s: str) -> str:
        stack = []  # Each element is [char, count]

        for ch in s:
            # If stack not empty and top character matches current, increment count
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                # If the previous group had more than 1 char, remove it (duplicate group)
                if stack and stack[-1][1] > 1:
                    stack.pop()

                # After popping, re-check the top
                if stack and stack[-1][0] == ch:
                    stack[-1][1] += 1
                else:
                    stack.append([ch, 1])  # New character, start with count 1

        # Final check: last group might still be a duplicate
        if stack and stack[-1][1] > 1:
            stack.pop()

        # Build the result string using only non-duplicate characters
        return ''.join(ch for ch, count in stack)
