'''
22. Generate Parentheses - Medium
Given:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

'''
Solution:
0) use dfs and track the already number of openB, closedB in path
1) base case is when openb == closedb == n: append global ans with path
2) recursive case: if openb < n:  dfs(openb + 1, closedB stays, path + '(' )
3) if open > closed (then can closed by closed, openb, closeb + 1, path + ')')
4) run dfs (0,0,'') and return global ans 
'''
def generateParenthesis(self, n: int) -> List[str]:
    ans = []

    def dfs(openN, closedN, path):
        # base case
        if openN == closedN == n:
            ans.append(path)
            return 
        # recursive case 
        if openN < n:
            dfs(openN + 1, closedN, path + '(')

        if openN > closedN:
            dfs(openN, closedN + 1, path + ')')

    dfs(0, 0, '')
    return ans 
