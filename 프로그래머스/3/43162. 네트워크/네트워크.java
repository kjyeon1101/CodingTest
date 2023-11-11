class Solution {
    boolean[] visited;
    
    void dfs(int[][] graph, int v) {
        visited[v] = true;
        for(int i=0;i<visited.length;i++) {
            if (graph[v][i] == 1 && visited[i] == false) {
                dfs(graph, i);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for(int i=0;i<n;i++) {
            if (visited[i] == false) {
                dfs(computers, i);
                answer += 1;
            }
        }
        
        return answer;
    }
}