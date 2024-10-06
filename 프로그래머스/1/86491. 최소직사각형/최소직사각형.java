import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        List<Integer> small = new ArrayList<>();
        List<Integer> big = new ArrayList<>();
        for(int i=0;i<sizes.length;i++) {
            if (sizes[i][0] <= sizes[i][1]) {
                small.add(sizes[i][0]);
                big.add(sizes[i][1]);
            } else {
                small.add(sizes[i][1]);
                big.add(sizes[i][0]);
            }
        }
        
        answer = Collections.max(small) * Collections.max(big);
        return answer;
    }
}