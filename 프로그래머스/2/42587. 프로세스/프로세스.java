import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        Queue<Integer> queue2 = new LinkedList<>();
        for(int i=0;i<priorities.length;i++) {
            queue.offer(priorities[i]);
            queue2.offer(i);
        }
        while (!queue.isEmpty()) {
            Integer process = queue.poll();
            Integer loc = queue2.poll();
            if (!queue.isEmpty()) {
                if (process >= Collections.max(queue)) {
                    answer += 1;
                    if (loc == location) {
                        return answer;
                    }
                } else {
                    queue.offer(process);
                    queue2.offer(loc);
                }
            } else {
                return answer + 1;
            }
        }
        return answer;
    }
}