def get_permutations(lst):
    if len(lst) == 0:
        return [[]]  # 빈 리스트의 순열은 자기 자신입니다.
    else:
        permutations = []
        for i in range(len(lst)):
            current_element = lst[i]
            remaining_elements = lst[:i] + lst[i+1:]
            # 나머지 요소들의 순열을 재귀적으로 구합니다.
            remaining_permutations = get_permutations(remaining_elements)
            # 현재 요소를 각 순열의 맨 앞에 추가하여 모든 순열을 만듭니다.
            for perm in remaining_permutations:
                permutations.append([current_element] + perm)
        return permutations
    

N, M = map(int, input().split())

num_list = list(range(1,N+1))

print(get_permutations(num_list))