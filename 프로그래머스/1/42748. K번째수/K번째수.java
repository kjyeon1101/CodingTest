import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int i=0;
        int j=0;
        int k=0;
        List<Integer> arrayList = new ArrayList<>();
        for(int idx=0;idx<array.length;idx++) {
            arrayList.add(array[idx]);
        }
        
        for(int idx=0;idx<commands.length;idx++) {
            i = commands[idx][0];
            j = commands[idx][1];
            k = commands[idx][2];
            List<Integer> subList = new ArrayList<>();
            for (Integer n : arrayList.subList(i-1,j)) {
                subList.add(n);
            }
            Collections.sort(subList);
            answer[idx] = subList.get(k-1);
        }
        return answer;
    }
}