def insert_sort(List: list):
    """
    在要排序的一组数中，假定前n-1个数已经排好序，现在将第n个数插到前面的有序数列中，使得这n个数也是排好顺序的。如此反复循环，直到全部排好顺序。
    """
    if len(List) < 2:
        return List
    res = [List[0]]
    for i in range(1, len(List)):
        for j in range(len(res)):
            if List[i] > List[j]:
                res.append(List[i])


if __name__ == "__main__":
    from test import Test
    test_data = Test().test_data()
    for value in test_data:
        print(value)
        print(insert_sort(value))
        print('\n')

