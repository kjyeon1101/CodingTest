import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0;i<scoville.length;i++) {
            pq.offer(scoville[i]);
        }
        
        while (true) {
            if (pq.peek() >= K) {
                break;
            }
            if (pq.size() >= 2) {
                int k1 = pq.poll();
                int k2 = pq.poll();
                if (k1 == 0 && k2 == 0) {
                    answer = -1;
                    break;
                }
                pq.offer(k1 + k2 * 2);
                answer += 1;
            } else {
                if (pq.peek() < K) {
                    answer = -1;
                }
                break;
            }
        }
        
        return answer;
    }
}