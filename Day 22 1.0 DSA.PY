class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        result = []
        friends_set = set(friends)  # Faster lookup

        for x in order:
            if x in friends_set:
                result.append(x)

        return result
