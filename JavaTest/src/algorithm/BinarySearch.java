package algorithm;
import java.util.*;

public class BinarySearch {

    public static int BSearch(int[] arr, int target, int start, int end){
        int mid;

        while(start <= end) {
            mid = (start+end)/2;
            if(arr[mid] == target)
                return mid
            else if(arr[mid] < target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1
    }
    
    public int[] solution(int []arr) {
        int[] answer = {};
        return answer;
    }


}