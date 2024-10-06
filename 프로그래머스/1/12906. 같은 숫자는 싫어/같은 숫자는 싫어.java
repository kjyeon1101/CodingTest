import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        for (int num : arr) {
            if (stack.size() == 0) {
                stack.add(num);
            } else {
                Integer top = stack.peek();
                if (top != num) {
                    stack.add(num);
                }
            }
        }
        
        int[] answer = new int[stack.size()];
        for(int i=0;i<stack.size();i++) {
            answer[i] = stack.get(i);
        }

        return answer;
    }
}