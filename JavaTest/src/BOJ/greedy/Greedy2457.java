package BOJ.greedy;
//공주님의 정원
//n개의 꽃 : 모두 같은해에 피어서 같은해에 짐
//하나의 꽃은 피는날과 지는날이 정해져있음
//1,3,5,7,8,10,12 : 31일
//4,6,9,11 : 30일
//2 : 28일
//조건
//꽃은 피는날 ~ 지는날-1 까지 피어있음 :*****문제 똑바로 읽기*****
//3월 1일~11월 30일 : 매일 꽃이 1가지 이상 피어있도록
//정원의 꽃수 최소한으로
//n개의 꽃들 중 3/1~11/30 매일 꽃이 한가지 이상 피어있도록 선택 : 선택한 꽃들의 최소개수 출력
//3.01 ~ 12.01까지
//
//입력 : n (1~100,000)
//n개의 줄에 꽃이 피는날짜 월,일 / 꽃이 지는날짜 월 일
//출력 : 선택한 꽃들의 최소개수 (두조건을 만족하는 꽃을 선택할 수 없으면 0)
import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy2457 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<double[]> flower = new ArrayList<>();
        int m1,d1,m2,d2;
        double start,end;
        StringTokenizer st;
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            m1 = Integer.parseInt(st.nextToken());
            d1 = Integer.parseInt(st.nextToken());
            m2 = Integer.parseInt(st.nextToken());
            d2 = Integer.parseInt(st.nextToken());
            start = m1+d1*0.01;
            end = m2+d2*0.01;
            if (end <= 3.01 | start >= 12.01)
                continue;
            else if(start < 3.01)
                start = 3.01;
            else if(end > 12.01)
                end = 12.01;
            flower.add(new double[]{start,end});
        }
        double[][] fwr = flower.toArray(new double[flower.size()][2]);
        Arrays.sort(fwr,Comparator.comparingDouble((double[] o) -> o[0])
                .thenComparingDouble(o -> o[1]));

        Stack<double[]> result = new Stack<>();
        start = fwr[0][0];
        end = fwr[0][1];
        double rstart, rend;
        boolean plant;
        if (start > 3.01)
            System.out.println(0);
        else{
            result.push(new double[]{start,end});
            for(int k=1;k<fwr.length;k++){
                start = fwr[k][0];
                end = fwr[k][1];
                plant = false;
                for(int i=result.size()-1;i>-1;i--){
                    rstart = result.get(i)[0];
                    rend = result.get(i)[1];
                    if (rstart == start & rend < end){
                        result.pop();
                        plant=true;
                    }else if(rstart < start & rend < end & rend >= start){
                        if(i<result.size()-1)
                            for(int j=result.size()-1;j>i;j--)
                                result.pop();
                        plant = true;
                    }
                    if(!plant)
                        break;
                }
                if (plant)
                    result.push(new double[]{start,end});
            }
            if (result.get(result.size()-1)[1] < 12.01)
                System.out.println(0);
            else
                System.out.println(result.size());
        }


    }
}
