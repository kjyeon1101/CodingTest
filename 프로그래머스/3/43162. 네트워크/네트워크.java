import java.util.*;
class Solution {
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        for(int i=0;i<n;i++) {
            graph.add(new ArrayList<>());
            visited[i] = false;
        }
        for(int i=0;i<n;i++) {
            for(int j=i+1;j<n;j++) {
                if (computers[i][j] == 1) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        for(int i=0;i<n;i++) {
            if (visited[i] == false) {
                dfs(i);
                answer += 1;
            }
        }
        return answer;
    }
    
    public void dfs(int v) {
        visited[v] = true;
        for(int next : graph.get(v)) {
            if (visited[next] == false) {
                dfs(next);
            }
        }
    }
}