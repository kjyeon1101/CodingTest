class Solution {
    public boolean[] dfs(int[][] graph, int v, boolean[] visited) {
        visited[v] = true;
        for(int i=0;i<visited.length;i++) {
            if (graph[v][i] == 1 && visited[i] == false) {
                dfs(graph, i, visited);
            }
        }
        return visited;
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for(int i=0;i<n;i++) {
            visited[i] = false;
        }
        
        for(int i=0;i<n;i++) {
            if (visited[i] == false) {
                visited = dfs(computers, i, visited);
                answer += 1;
            }
        }
        
        return answer;
    }
}