class Solution {
  public int findContentChildren(int[] childrenHunger, int[] cookieSizes) {
        Arrays.sort(childrenHunger);
        Arrays.sort(cookieSizes);

        // Corner case: If cookieSizes is empty || max cookie size < min child hunger 
        if (cookieSizes.length == 0 || cookieSizes[cookieSizes.length - 1] < childrenHunger[0]){
            return 0;
        }

        // Using binary search, find the first index in cookieSizes which satisfies minimum hunger
        int low = 0, high = cookieSizes.length - 1;
        while (low < high){
            int mid = low + (high - low)/2;
            if (cookieSizes[mid] >= childrenHunger[0]){
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }

        int satisfiedChildren = 0, cookieIndex = high;
        while (cookieIndex < cookieSizes.length && satisfiedChildren < childrenHunger.length){
            if (childrenHunger[satisfiedChildren] <= cookieSizes[cookieIndex]){
                satisfiedChildren++;
            }
            cookieIndex++;
        }

        return satisfiedChildren;
    }

}