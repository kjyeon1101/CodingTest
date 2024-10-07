import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i=0;i<n+1;i++) {
            graph.add(new ArrayList<>());
        }
        for(int[] e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        Node node = new Node(0,0);
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int[] distance = new int[n+1];
        for(int i=1;i<n+1;i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        distance[1] = 0;
        pq.offer(new Node(0,1));
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            int dist = now.getDist();
            int v = now.getV();
            if (distance[v] < dist) {
                continue;
            }
            for(int i=0;i<graph.get(v).size();i++) {
                int next = graph.get(v).get(i);
                if (distance[next] > dist + 1) {
                    distance[next] = dist + 1;
                    pq.offer(new Node(distance[next],next));
                }
            }
        }
        List<Integer> distanceList = Arrays.stream(distance).boxed().collect(Collectors.toList());
        System.out.println(Collections.max(distanceList));
        answer = Collections.frequency(distanceList, Collections.max(distanceList));
        
        return answer;
    }
}

class Node implements Comparable<Node> {
    int dist;
    int v;
    public Node (int dist, int v) {
        this.dist = dist;
        this.v = v;
    }
    public int getDist() {
        return this.dist;
    }
    public int getV() {
        return this.v;
    }
    @Override
    public int compareTo(Node node) {
        return Integer.compare(this.dist, node.dist);
    }
}