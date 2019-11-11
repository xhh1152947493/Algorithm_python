def selection_sort(List: list):
    """
    在长度为N的无序数组中，第一次遍历n-1个数，找到最小的数值与第一个元素交换；
    第二次遍历n-2个数，找到最小的数值与第二个元素交换；
    。。。
    第n-1次遍历，找到最小的数值与第n-1个元素交换，排序完成。
    时间复杂度：O(n2)
    """
    for i in range(len(List)-1):
        min_index = i
        for j in range(i+1, len(List)):
            if List[j] < List[min_index]:
                min_index = j
        if min_index != i:
            List[i], List[min_index] = List[min_index], List[i]
    return List


if __name__ == "__main__":
    from test import Test
    test_data = Test().test_data()
    for value in test_data:
        print(value)
        print(selection_sort(value))
        print('\n')

"""
[32, 38, 39, 46, 61, 80, 83, 83, 87, 92]
[12, 30, 56, 56, 59, 66, 76, 77, 78, 81]
[1, 2, 8, 22, 34, 34, 43, 68, 69, 95]
[1, 13, 14, 20, 31, 62, 64, 81, 83, 100]
[1, 13, 17, 29, 48, 52, 57, 72, 82, 89]
[10, 14, 36, 43, 66, 71, 73, 86, 86, 90]
[0, 19, 22, 35, 48, 60, 60, 69, 86, 87]
[12, 15, 16, 32, 48, 51, 58, 61, 86, 95]
[15, 19, 31, 32, 48, 53, 62, 62, 70, 76]
[0, 4, 16, 19, 24, 50, 52, 53, 63, 63]
"""