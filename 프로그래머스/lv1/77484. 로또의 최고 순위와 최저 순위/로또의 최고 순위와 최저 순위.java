//10:47
//당첨 번호순으로 순위가 정해짐
//당첨이 가능했던 최고 및 최저 순위를 알고 싶다 -> Map을 통해 맞춘 양에 따라 순위 값 구해주면 될듯

import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0, 0};
        
        //score 초기화
        HashMap<Integer, Integer> score = new HashMap<Integer, Integer>();
        
        int[] a = {1,2,3,4,5,6,6};
        int[] b = {6,5,4,3,2,1,0};
        
        for (int i = 0; i<a.length; i++) {
            score.put(b[i], a[i]);
        }
        
        //Set으로 당첨 번호 초기화, 시간복잡도를 위해 초기화
        HashSet<Integer> nums = new HashSet<Integer>();
        for (int i : win_nums) {
            nums.add(i);
        }
        
        int count = 0; //0의 수
        int right = 0; //맞은 수
        
        for (int i : lottos) {
            
            if (i == 0) {
                count++;
            }
            
            if (nums.contains(i)) {
                right++;
            }
        }
        
        answer[0] = score.get(count+right);
        answer[1] = score.get(right);
        
        return answer;
    }
}