def singleNumber(self, bro: List[int]) -> int:
        return 2 * sum(set(bro)) - sum(bro)
