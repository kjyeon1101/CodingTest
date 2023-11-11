import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        List<String> pList = new ArrayList<>(Arrays.asList(participant));
        List<String> cList = new ArrayList<>(Arrays.asList(completion));
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String p : pList) {
            if (map.containsKey(p)) {
                map.put(p, map.get(p)+1);
            } else {
                map.put(p, 1);
            }
        }
        
        for (String c : cList) {
            map.put(c, map.get(c)-1);
        }
        
        for (String k : map.keySet()) {
            if (map.get(k) == 1) {
                answer = k;
            }
        }
        return answer;
    }
}