import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0;i<scoville.length;i++) {
            pq.offer(scoville[i]);
        }
        while (!pq.isEmpty()) {
            Integer food = pq.poll();
            if (food >= K) {
                break;
            }
            if (pq.size() > 0) {
                Integer food2 = pq.poll();
                pq.offer(food + food2*2);
                answer += 1;
            } else {
                return -1;
            }
        }
        return answer;
    }
}