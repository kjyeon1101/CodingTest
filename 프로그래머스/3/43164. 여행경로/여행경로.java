import java.util.*;
class Solution {
    boolean[] visited;
    List<String> path = new ArrayList<>();
    boolean answerFlag = false;
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        visited = new boolean[tickets.length];
        for(int i=0;i<tickets.length;i++) {
            visited[i] = false;
        }
        List<String[]> ticketList = new ArrayList<>(Arrays.asList(tickets));
        Collections.sort(ticketList, new Comparator<String[]>(){
            public int compare(String[] o1, String[] o2) {
                if (o1[0].equals(o2[0])) {
                    return o1[1].compareTo(o2[1]);
                } else {
                    return o1[0].compareTo(o2[0]);
                }
            }
        });
        path.add("ICN");
        List<String> answerPath = backtracking(ticketList,"ICN");
        answer = answerPath.toArray(new String[answerPath.size()]);
        return answer;
    }
    
    public List<String> backtracking(List<String[]> ticketList, String now) {
        if (answerFlag) {
            return path;
        }
        if (path.size() == ticketList.size()+1) {
            answerFlag = true;
            return path;
        }
        for(int i=0;i<ticketList.size();i++) {
            if (ticketList.get(i)[0].equals(now) && visited[i] == false) {
                path.add(ticketList.get(i)[1]);
                visited[i] = true;
                backtracking(ticketList,ticketList.get(i)[1]);
                if (answerFlag) {
                    return path;
                }
                visited[i] = false;
                path.remove(path.size()-1);
            }
        }
        return path;
    }
}