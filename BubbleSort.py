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
    test_data = Test().test_data()
    for value in test_data:
        print(value)
        print(bubble_sort(value))
        print('\n')
