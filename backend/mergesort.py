def mergeSort(frag, index):
    # checks if there is more than one element in the list
    if len(frag) > 1:
        # finds the index for the middle of the list
        midLen = len(frag) // 2
        # based on midLen, the list is divided into a right side and left side
        right = frag[midLen:]
        mergeSort(right, index)

        left = frag[:midLen]
        mergeSort(left, index)

        # sets the pointers = 0
        # left
        i = 0
        # right
        j = 0
        # merged
        n = 0

        while j < len(right) and i < len(left):
            # checks the indexes
            # in the right section of the list, this fixes the ordering
            if left[i][index] >= right[j][index]:
                frag[n] = right[j]
                j = j + 1
            # in the left section of the list, this fixes the ordering
            else:
                frag[n] = left [i]
                i = i + 1
            # increments the merged
            n = n + 1
        # right section is completed
        while j < len(right):
            frag[n] = right[j]
            n = n + 1
            j = j + 1
        # left section is completed
        while i < len(left):
            frag[n] = left[i]
            n = n + 1
            i = i + 1