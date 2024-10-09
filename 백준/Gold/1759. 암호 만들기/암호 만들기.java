import java.util.*;

class Main {
    static List<String> alphabet = new ArrayList<>();
    static boolean[] visited;
    static int L;
    static int C;
    static List<String> moeumList = new ArrayList<>();
    public static void main(String[] args) {
        solution();
    }

    public static void solution() {
        Scanner sc = new Scanner(System.in);
        L = sc.nextInt();
        C = sc.nextInt();
        visited = new boolean[C];
        for(int i=0;i<C;i++) {
            visited[i] = false;
        }
        char[] arr = new char[C];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.next().charAt(0);
        }
        for(String a : String.valueOf(arr).split("")) {
            alphabet.add(a);
        }
        Collections.sort(alphabet);
        List<Integer> path = new ArrayList<>();
        moeumList.add("a");
        moeumList.add("e");
        moeumList.add("i");
        moeumList.add("o");
        moeumList.add("u");
        for(int i=0;i<C;i++) {
            if (visited[i] == false) {
                path.add(i);
                visited[i] = true;
                backtracking(i,path);
                visited[i] = false;
                path.remove(path.size()-1);
            }
        }
    }

    public static void backtracking(int v, List<Integer> path) {
        if (path.size() == L) {
            int moeum = 0;
            int jaeum = 0;
            for(Integer p : path) {
                if (moeumList.contains(alphabet.get(p))) {
                    moeum += 1;
                } else {
                    jaeum += 1;
                }
            }
            if (moeum >= 1 && jaeum >= 2) {
                for(Integer p : path) {
                    System.out.print(alphabet.get(p));
                }
                System.out.println();
            }
            return;
        } else {
            for(int i=v+1;i<C;i++) {
                if (visited[i] == false) {
                    path.add(i);
                    visited[i] = true;
                    backtracking(i,path);
                    visited[i] = false;
                    path.remove(path.size()-1);
                }
            }
        }
    }
}