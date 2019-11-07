def bubble_sort(List: list):
    """
    比较相邻的两个数据，如果第二个数小，就交换位置。
    从后向前两两比较，一直到比较最前两个数据。最终最小数被交换到起始的位置，这样第一个最小数的位置就排好了。
    继续重复上述过程，依次将第2.3...n-1个最小数排好位置。
    时间复杂度：O(n2)
    空间复杂度：原地排序O(n)
    """
    for i in range(len(List)-1):
        for j in range(i+1, len(List)):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    return List


if __name__ == "__main__":
    from test import Test
    test_date = Test().test_date()
    for value in test_date:
        print(bubble_sort(value))


"""
[23, 44, 56, 56, 57, 64, 72, 77, 80, 91]
[4, 12, 13, 23, 28, 32, 46, 46, 56, 96]
[11, 38, 38, 43, 54, 63, 66, 70, 96, 100]
[11, 13, 16, 34, 40, 44, 49, 63, 94, 100]
[21, 34, 50, 64, 73, 80, 81, 89, 95, 95]
[6, 21, 40, 45, 47, 51, 64, 90, 92, 96]
[2, 7, 8, 9, 18, 36, 60, 66, 71, 81]
[11, 13, 15, 16, 19, 24, 41, 67, 95, 97]
[3, 12, 35, 38, 44, 55, 78, 85, 93, 96]
[1, 12, 16, 25, 48, 52, 71, 90, 93, 95]
"""