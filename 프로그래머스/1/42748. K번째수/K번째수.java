import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int c=0;c<commands.length;c++){
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];
            List<Integer> subArray = new ArrayList<>();
            for(int a=i-1;a<j;a++) {
                subArray.add(array[a]);
            }
            Collections.sort(subArray);
            answer[idx++] = subArray.get(k-1);
        }
        return answer;
    }
}