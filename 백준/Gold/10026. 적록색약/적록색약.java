import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    static int N;
    static char[][] arr;
    static boolean[][] visited;
    public static void main(String []args) throws IOException {
        int[] answer = solution();
        System.out.println(answer[0]+" "+answer[1]);
    }
    
    public static int[] solution() throws IOException {
        int[] answer = new int[2];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new char[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String S = br.readLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = S.charAt(j);
                visited[i][j] = false;
            }
        }

        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                if (visited[i][j] == false) {
                    BFS(i,j,arr[i][j]);
                    answer[0] += 1;
                }
            }
        }

        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                visited[i][j] = false;
                if (arr[i][j] == 'G') {
                    arr[i][j] = 'R';
                }
            }
        }

        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                if (visited[i][j] == false) {
                    BFS(i,j,arr[i][j]);
                    answer[1] += 1;
                }
            }
        }
        
        return answer;
    }

    public static void BFS(int r, int c, char color) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r,c});
        visited[r][c] = true;
        int[][] direct = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int now_r = now[0];
            int now_c = now[1];
            for(int i=0;i<4;i++) {
                int next_r = now[0] + direct[i][0];
                int next_c = now[1] + direct[i][1];
                if (next_r >= 0 && next_r < N && next_c >= 0 && next_c < N) {
                    if (visited[next_r][next_c] == false && arr[next_r][next_c] == color) {
                        queue.offer(new int[]{next_r,next_c});
                        visited[next_r][next_c] = true;
                    }
                }
            }
        }
    }
}