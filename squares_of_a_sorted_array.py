class Solution:
    """https://leetcode.com/problems/squares-of-a-sorted-array/submissions/"""
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        if self.list_starts_with_a_non_negative_integer(A) or len(A) == 1:
            return self.get_squares_of_numbers_in_a_list(A)
        elif A[-1] <= 0:
            return self.get_squares_of_numbers_in_a_list(A[::-1])
        else:
            return self.create_sorted_list_of_absolutes(A)

    def list_starts_with_a_non_negative_integer(self, A):
        return True if A[0] >= 0 else False

    def get_squares_of_numbers_in_a_list(self, int_list):
        return [i ** 2 for i in int_list]

    def create_sorted_list_of_absolutes(self, integers):
        result = []
        negative_index, positive_index = self.find_inices_of_two_smallest_absolutes(integers)
        while negative_index > -1 and positive_index < len(integers):
            if abs(integers[negative_index]) < abs(integers[positive_index]):
                result.append(integers[negative_index] ** 2)
                negative_index -= 1
            else:
                result.append(integers[positive_index] ** 2)
                positive_index += 1

        if negative_index >= 0:
            for i in range(negative_index + 1)[::-1]:
                result.append(integers[i] ** 2)
        elif positive_index <= len(integers) - 1:
            for i in range(positive_index, len(integers)):
                print(i)
                result.append(integers[i] ** 2)

        return result

    def find_inices_of_two_smallest_absolutes(self, integers):
        for index, num in enumerate(integers):
            if num > 0:
                return index - 1, index

