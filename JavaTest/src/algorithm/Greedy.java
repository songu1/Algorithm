package algorithm;

/* 그리디 문제 - 거스룸돈 문제 */
public class Greedy {
    public static void main(String[] args) {
        int n=1260;
        int cnt=0;
        int[] coinTypes={500,100,50,10};

        for(int i=0;i<4;i++){
            cnt += n/coinTypes[i];
            n %= coinTypes[i];
        }
        System.out.println(cnt);
    }
}
// 시간복잡도 O(K) : k는 화폐의 종류
