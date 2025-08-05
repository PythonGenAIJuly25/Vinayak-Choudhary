def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for s,e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged

# Test Case 1: Basic overlapping intervals
test1 = [[1,3],[2,6],[8,10],[15,18]]
result1 = merge_intervals(test1)
print(result1)
# Expected: [[1,6],[8,10],[15,18]]

# Test Case 2: Adjacent intervals (touching endpoints)
test2 = [[1,4],[4,5]]
result2 = merge_intervals(test2)
print(result2)
# Expected: [[1,5]]

# Test Case 3: Completely contained intervals
test3 = [[1,4],[2,3]]
result3 = merge_intervals(test3)
print(result3)
# Expected: [[1,4]]

# Test Case 4: No overlapping intervals
test4 = [[1,2],[3,4],[5,6]]
result4 = merge_intervals(test4)
print(result4)
# Expected: [[1,2],[3,4],[5,6]]

# Test Case 5: All intervals overlap
test5 = [[1,4],[2,5],[3,6]]
result5 = merge_intervals(test5)
print(result5)
# Expected: [[1,6]]

# Test Case 6: Unsorted input
test6 = [[6,7],[2,4],[5,9]]
result6 = merge_intervals(test6)
print(result6)
# Expected: [[2,4],[5,9]]

# Test Case 7: Single interval
test7 = [[1,4]]
result7 = merge_intervals(test7)
print(result7)
# Expected: [[1,4]]

# Test Case 8: Complex overlapping case
test8 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
result8 = merge_intervals(test8)
print(result8)
# Expected: [[1,10]]