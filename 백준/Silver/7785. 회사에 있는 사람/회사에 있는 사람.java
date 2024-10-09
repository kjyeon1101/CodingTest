import java.util.*;

class Main {
    public static void main(String[] args) {
        String[] answer = solution();
        for(String a : answer) {
            System.out.println(a);
        }
    }

    public static String[] solution() {
        Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
        HashMap<String, String> map = new HashMap<>();
		for (int i = 0; i < n; i++) {
			String name = sc.next();
			String state = sc.next();
            if (state.equals("enter")) {
                map.put(name, state);
            } else {
                map.remove(name);
            }
		}
        List<String> list = new ArrayList<>();
        for (String key : map.keySet()) {
            list.add(key);
        }
        Collections.sort(list, Collections.reverseOrder());
        String[] answer = list.toArray(new String[list.size()]);
        return answer;
    }
}