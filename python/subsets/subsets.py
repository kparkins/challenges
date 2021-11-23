def find_subsets(nums):
    subsets = [[]]
    for n in nums:
        num_subsets = len(subsets)
        for i in range(num_subsets):
            subsets.append(subsets[i] + [n])
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


if __name__ == '__main__':
    main()
