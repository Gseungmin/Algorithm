//10:8
//길이가 같은 두개의 큐
//하나의 큐를 골라 원소 추출해서 다른 큐에 집어 넣음
//각 큐의 원소의 합이 같도록
//먼저 집어넣은 원소가 나오는 구조

import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -1;
        long l = 0; //왼쪽 합
        long r = 0; //오른쪽 합
        long s = 0; //총 합
        long d = 0;
        
        //큐 초기화
        List<Long> q = new ArrayList<>();
        
        for (long i : queue1) {
            l += i;
            q.add(i);
        }
        
        for (long i : queue2) {
            r += i;
            q.add(i);
        }
        
        s = l+r;
        
        //조기 종료 조건
        if (s%2 != 0) {
            return -1;
        }
        
        //목표 값
        d = s/2;
        
        int cnt = 0;
        int left = 0;
        int right = q.size()/2-1;
        long k = l; //값
        
        while (left < q.size()) {
            
            //종료 조건
            if (k == d) {
                return cnt;
            }
            
            // k값이 더 작다면
            while (k < d) {
                right++;
                if (right == q.size()) {
                    right = 0;
                }
                k += q.get(right);
                cnt++;
            }
            
            //k값이 더 크다면
            while (k > d) {
                k -= q.get(left);
                left++;
                cnt++;
                if (left == q.size()) {
                    return -1;
                }
            }
            
            //종료 조건
            if (k == d) {
                return cnt;
            }
        }
        return answer;
    }
}