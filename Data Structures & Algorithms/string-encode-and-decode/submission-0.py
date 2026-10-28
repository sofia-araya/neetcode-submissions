class Solution:

    def encode(self, strs: List[str]) -> str:
        str = "".join([f"{len(s)}#{s}" for s in strs])
        return str


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        current_location = 0

        while current_location < len(s):
            hashtag_index = s.index('#', current_location)
            this_string_length = s[current_location:hashtag_index]
            string_length = int(this_string_length)

            string = s[hashtag_index+1:hashtag_index+string_length+1]
            decoded_strings.append(string)
            current_location = hashtag_index + 1 + string_length

        return decoded_strings
