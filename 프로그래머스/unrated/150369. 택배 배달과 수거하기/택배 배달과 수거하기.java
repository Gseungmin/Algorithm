//9:10
//일렬로 나열된 n가의 집에 택배 배달
//배달을 다니면서 빈 재활용 택배 상자들을 수거
//i번째 집은 물류창고에서 i만큼 떨어짐
//트럭에는 최대 cap 개의 택배 상자를 실음
//물류창고에서 출발해 각 집에 배달하고 수거하옴
//최소 이동 거리

//1. 물류 <= 수거인경우
//물류 다 배달하고 수거까지 가면 됨
//2. 물류 > 수거
//물류 다 배달하고 수거까지 가면 됨

//그냥 물류 다 배달하고 수거하면 될듯?
//모든 상자 인덱스를 스택에 저장하고 매번 최대 스택값 더하면 될듯

import java.util.*;
class Solution {
    
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int dist = 0; //최대 거리
        int pick_count = 0; //수거할 박스 수
        int put_count = 0; //내려 놓을 박스 수
        
        Stack<Integer> put = new Stack<>();
        Stack<Integer> pick = new Stack<>();
        
        //배달할 곳 인덱스 추가
        for (int i = 0; i < deliveries.length; i++) {
            for (int j = 0; j < deliveries[i]; j++) {
                put.add(i);
            }
        }
        
        //수거할 곳 인덱스 추가
        for (int i = 0; i < pickups.length; i++) {
            for (int j = 0; j < pickups[i]; j++) {
                pick.add(i);
            }
        }
        
        //택배 배송 및 수거 완료
        while (true) {
        
            //최대 이동 값 구하기
            while (true) {

                //주울게 있을 경우
                if (pick.size() > 0) {
                    dist = Math.max(dist, pick.pop()+1);
                    pick_count++;
                }

                //최대로 주운 경우
                if (pick_count == cap) {
                    break;
                }

                //주울게 없는 경우
                if (pick.size() == 0) {
                    break;
                }
            }

            //최대 이동 값 구하기
            while (true) {

                //주울게 있을 경우
                if (put.size() > 0) {
                    dist = Math.max(dist, put.pop()+1);
                    put_count++;
                }

                //최대로 놓은 경우
                if (put_count == cap) {
                    break;
                }

                //놓을게 없는 경우
                if (put.size() == 0) {
                    break;
                }
            }

            answer += dist;
            pick_count = 0;
            put_count = 0;
            dist = 0;
            
            if ((put.size() == 0) & (pick.size() == 0)) {
                break;
            }
        }
        
        
        return answer*2;
    }
}