import java.util.*;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();
        
        for(int num: nums1){
            map1.put(num, map1.getOrDefault(num, 0) + 1);
        }
        
        for(int num: nums2){
            map2.put(num, map2.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> diff1 = new ArrayList<>();
        for(int num: nums1){
            if(map2.getOrDefault(num, 0) == 0){
                diff1.add(num);
                map2.put(num, 1);
            }
        }
        
        List<Integer> diff2 = new ArrayList<>();
        for(int num: nums2){
            if(map1.getOrDefault(num, 0) == 0){
                diff2.add(num);
                map1.put(num, 1);
            }
        }
        
        return Arrays.asList(diff1, diff2);
    }
}
