numbers_present = set(arr)
        count = 0
        for num in arr:
            if num+1 in numbers_present:
                count += 1 
        return count
