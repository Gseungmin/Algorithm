//45중 6개를 찍어서 맞춰야 함
//로또로 가능했던 최고 순위와 최저 순위를 알고 싶어짐
//순서와 상관없음
//lottos는 내가 뽑은 수
//win_nums는 로또 번호
//lottos 돌면서 0의 개수 세고 맞는 개수 세기, 맞는 개수가 최저, 0의 개수 + 맞는 개수가 최고 개수

import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        
        //로또 번호 정리
        HashSet<Integer> nums = new HashSet<Integer>();
        for (int i = 0; i< win_nums.length; i++) {
            nums.add(win_nums[i]);
        }
        
        //당첨 매칭
        HashMap<Integer, Integer> match = new HashMap<Integer, Integer>();
        int[] a = {6,5,4,3,2,1,0};
        int[] b = {1,2,3,4,5,6,6};
    
        for (int i = 0; i<a.length; i++) {
            match.put(a[i], b[i]);
        }
        
        //0의 개수
        int count = 0;
        //맞은 번호의 개수
        int lottoCount = 0;
        for (int i : lottos) {
            if (i == 0) {
                count += 1;
            } else if (nums.contains(i)) {
                lottoCount ++;
            }
        }
        
        int[] answer = {match.get(lottoCount + count), match.get(lottoCount)};
        return answer;
    }
}