def solution(n, arr1, arr2):
    answer = []
    arr1_bin = [bin(a1)[2:].rjust(n,"0") for a1 in arr1]
    arr2_bin = [bin(a2)[2:].rjust(n,"0") for a2 in arr2]
    for a1, a2 in zip(arr1_bin, arr2_bin):
        answer.append("".join(["#" if str(int(b1) or int(b2))=="1" else " " for b1, b2 in zip(a1,a2)]))
    return answer