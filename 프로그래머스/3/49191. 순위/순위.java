import java.util.*;
class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int maxValue = (int)Math.pow(10,9);
        int[][] distance = new int[n+1][n+1];
        for(int i=0;i<n+1;i++) {
            for(int j=0;j<n+1;j++) {
                distance[i][j] = maxValue;
            }
            distance[i][i] = 0;
        }
        for(int[] result : results) {
            distance[result[0]][result[1]] = 1;
        }
        for(int k=1;k<n+1;k++) {
            for(int a=1;a<n+1;a++) {
                for(int b=1;b<n+1;b++) {
                    distance[a][b] = Math.min(distance[a][b], distance[a][k]+distance[k][b]);
                }
            }
        }
        for(int i=1;i<n+1;i++) {
            int cnt = 0;
            for(int j=1;j<n+1;j++) {
                if (i != j && distance[i][j] < maxValue) {
                    cnt += 1;
                }
                if (i != j && distance[j][i] < maxValue) {
                    cnt += 1;
                }
            }
            if (cnt == n-1) {
                answer += 1;
            }
        }
        return answer;
    }
}