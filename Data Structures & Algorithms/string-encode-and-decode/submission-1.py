class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY_LIST__"
        encoded_string=[s.encode("utf-8") for s in strs]
        return "|||".join([b.decode("latin1") for b in encoded_string])
    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY_LIST__":
            return []
        if not s:
            return [""]
        reconstruct=[item.encode("utf-8") for item in s.split("|||")]
        return [b.decode("utf-8") for b in reconstruct]