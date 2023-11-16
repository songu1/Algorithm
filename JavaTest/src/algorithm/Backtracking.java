package algorithm;
import java.util.*;

public class Backtracking {

	
	public static void main(String[] args) {
		int n = 2;
		int[] array = {1,2,3};
        int[] arr = new int[n];
        int[] arr2 = new int[n];
		boolean[] visited = new boolean[n];
		
//		perm(array, arr, visited, 0, n);
//        comb(array,arr2,0, n, 0);

		//배열, 뽑아낼 원소들 배열, 방문 배열, depth, n, r)
		
		//이미 들어간 값은 visited 값을 true로 바꾸어 중복하여 넣지 않도록 합니다.
		//depth 값은 output에 들어간 숫자의 길이라고 생각하면 된다.
		//depth의 값이 r만큼 되면 output에 들어있는 값을 출력.
	}
	
	// 순열 구하기
    // 중복 순열은 visited 배열 제외
//	static public void perm(int[] array, int[] arr, boolean[] visited, int depth, int n) {
//		if(depth == n){
//            return;
//        }
//        else{
//            for(int i = 0 ; i <array.length; i++){
//                if (!visited[i]){
//                    visited[i] = true;
//                    arr[depth] = array[i];
//                    perm(array,arr,visited,depth+1,n);
//                    visited[i] = false;
//                }
//            }
//        }
//
//
//	}
//
//    // 조합
//    static public void comb(int[] array, int[] arr, int depth, int n, int idx){
//        if(depth == n){
//            return;
//        }
//        else{
//            for(int i = idx; i <array.length; i++){
//                arr[depth] = array[i];
//                comb(array, arr, depth+1, n, idx+1);
//                // 중복 조합
//                // comb(array, arr, depth+1, n, idx);
//            }
//        }
//    }


}