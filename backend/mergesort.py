def mergeSort(frag, index):
    if len(frag) > 1:
        midLen = len(frag) // 2

        right = frag[midLen:]
        mergeSort(right, index)

        left = frag[:midLen]
        mergeSort(left, index)

        i = 0
        j = 0
        n = 0

        while j < len(right) and i < len(left):
            if left[i][index] >= right[j][index]:
                frag[n] = right[j]
                j = j + 1

            else:
                frag[n] = left [i]
                i = i + 1

            n = n + 1

        while j < len(right):
            frag[n] = right[j]
            n = n + 1
            j = j + 1

        while i < len(left):
            frag[n] = left[i]
            n = n + 1
            i = i + 1
