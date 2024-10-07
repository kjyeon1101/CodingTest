import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0,0,1});
        maps[0][0] = 2;
        int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int next_x = 0;
        int next_y = 0;
        int N = maps.length;
        int M = maps[0].length;
        
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            if (now[0] == M-1 && now[1] == N-1) {
                return now[2];
            }
            for(int i=0;i<4;i++) {
                next_y = now[1] + directions[i][0];
                next_x = now[0] + directions[i][1];
                if ((next_x >= 0 && next_x < M) && (next_y >= 0 && next_y < N) && (maps[next_y][next_x] == 1)) {
                    queue.offer(new int[]{next_x,next_y,now[2]+1});
                    maps[next_y][next_x] = 2;
                }
            }
        }
        
        return answer;
    }
}