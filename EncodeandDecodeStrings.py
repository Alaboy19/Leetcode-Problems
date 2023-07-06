'''
271. Encode and Decode Strings - Medium
Given:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).
'''
'''
Solution:
1) the key idea here is to get to know the start of first str and its length(length is seperated by value with some symbol)
2) first point garantees that length and symbol will help to determine the length and symbol of next string by right offset 
3) then encode function will make it one whole string
4) decode will iterate and append the length after # symbol every time and reconstruct the orig string back 
'''
def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for each_str in strs:
            res += str(len(each_str)) + "#" + each_str

        return res 

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    res = []
    i = 0 
    while i < len(s):
        j = i  
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        res.append(s[j+1:j+1+length])
        i = j + 1 + length 
    return res

