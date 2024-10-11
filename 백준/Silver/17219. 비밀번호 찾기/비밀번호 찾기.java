import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String []args) throws IOException {
        String[] answer = solution();
        for(int i=0;i<answer.length;i++) {
            System.out.println(answer[i]);
        }
    }
    
    public static String[] solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        HashMap<String, String> map = new HashMap<>();
        String[] answer = new String[M];
        for (int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            map.put(input[0],input[1]);
        }
        for (int i = 0; i < M; i++) {
            answer[i] = map.get(br.readLine());
        }
        return answer;
    }

}