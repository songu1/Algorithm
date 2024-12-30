/* 출퇴근길 단방향그래프 (1~n 정점, m개의 단방향 간선)
    집 :S, 회사 : T , 출퇴근길 : S~T사이 경로
    S->T와 T->S에서 모두 포함되는 정점의 개수 (도착지를 제외한 지점은 돌아가도 됨) */
// 팁************************************
// S->T와 ?->T + T->S와 ?->S 경로를 포함해야함 (?는 나머지 지점은 중복 가능하므로)
// ?->T/S 경로는 T->S, S->T의 역방향으로 구하기
import java.io.*;
import java.util.*;

public class Main {
    public static ArrayList<ArrayList<Integer>> forwardGraph = new ArrayList<>();
    public static ArrayList<ArrayList<Integer>> backwardGraph = new ArrayList<>();
    public static boolean[] sT,sTr, tS, tSr;

    private static void dfs(ArrayList<ArrayList<Integer>> graph,int start, int end, boolean[] visited) {
        visited[start] = true;
        // if (start==end)
        //     return;
        for (int i:graph.get(start)) {
            if (!visited[i]) {
                dfs(graph,i,end,visited);
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        int answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for (int i=0; i<=n; i++) {
            forwardGraph.add(new ArrayList<>());
            backwardGraph.add(new ArrayList<>());
        }
        sT = new boolean[n+1];
        tS = new boolean[n+1];
        sTr = new boolean[n+1];
        tSr = new boolean[n+1];
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            forwardGraph.get(a).add(b);
            backwardGraph.get(b).add(a);
        }
        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        sT[T] = true;
        tS[S] = true;
        dfs(forwardGraph,S,T,sT);    // S에서 출발해서 갈 수 있는 모든 노드
        dfs(backwardGraph,T,S,sTr);  // T로 도착할 수 있는 모든 노드
        dfs(forwardGraph,T,S,tS);    // T에서 출발해서 갈 수 있는 모든 노드
        dfs(backwardGraph,S,T,tSr);  // S로 도착할 수 있는 모든 노드
        // System.out.println(Arrays.toString(sT));
        // System.out.println(Arrays.toString(sTr));
        // System.out.println(Arrays.toString(tS));
        // System.out.println(Arrays.toString(tSr));

        for (int i=1; i<=n; i++) {
            if (i==S || i==T)
                continue;
            if (sT[i] && sTr[i] && tS[i] && tSr[i]) 
                answer++;
        }
        System.out.println(answer);
    }
}
