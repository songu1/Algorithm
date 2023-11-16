package BOJ.greedy;
//수리공 항승
//왼쪽에서 정수만큼 떨어진 거리만 물이 샘
//길이가 l인 테이프 무한개 가지고 있음
//테이프를 이용하여 물을 막음
//그 위치의 좌우 0.5마늠 간격을 줘야 물이 안샘
//물이 새는 곳의 위치 , 테이프의 길이 l => 필요한 테이프의 최소 개수를 구하는 프로그램
//테이프 자를 수 없음, 겹쳐서 붙이는 것은 가능
//
//입력 : 물이 새는 곳의 개수 n, 테이프의 길이 l
//물이 새는 곳의 위치 (1~1000)
//출력 : 항승이가 필요한 테이프 개수
import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy1449 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int[] leak =  new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            leak[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(leak);
        int count = 0;
        int start = -1;
        for(int lk:leak){
            if(lk < start)
                continue;
            count += 1;
            start = lk + l;
        }
        System.out.println(count);
    }
}
