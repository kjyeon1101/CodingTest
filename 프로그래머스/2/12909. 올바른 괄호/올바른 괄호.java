import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            Character str = s.charAt(i);
            if (stack.size() == 0) {
                stack.push(str);
            } else {
                if (str == '(') {
                    stack.push(str);
                } else {
                    Character top = stack.peek();
                    if (top == '(') {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }
        }
                    
        if (stack.size() > 0) {
            answer = false;
        }
        
        return answer;
    }
}