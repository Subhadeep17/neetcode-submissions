class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = "".join(f"{len(s)}#{s}" for s in strs)   

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i<len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            
            i=j+1
            word = s[i:i+length]
            decoded_list.append(word)

            i=i+length

        return decoded_list
        