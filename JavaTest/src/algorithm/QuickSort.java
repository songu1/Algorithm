package algorithm;

public class QuickSort {
  public static void quickSort(int[] arr, int left, int right) {
        if (left >= right) return;

        int pivot = arr[(left + right) / 2];
        int l = left;
        int r = right;

        while (l <= r) {
            while (arr[l] < pivot) l++;
            while (arr[r] > pivot) r--;

            if (l <= r) {
                swap(arr, l, r);
                l++;
                r--;
            }
        }

        quickSort(arr, left, r);
        quickSort(arr, l, right);
    }

    private static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
