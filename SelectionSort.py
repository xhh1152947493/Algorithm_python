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

