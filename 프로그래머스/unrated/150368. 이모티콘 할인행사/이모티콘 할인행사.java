//9:43
//이모티콘 플러스 서비스 가입자 수 늘리기
//서비스 가입자 최대한 늘리기 + 판매액 최대한 늘리기, 1이 우선
//n명의 카카오톡 사용자들에게 m개를 할인하여 판매
//할인율은 10, 20, 30, 40중 하나
//이모티콘을 사거나 플러스에 가입함
//자신의 기준으로 일정 비율 이상 할인하는 이모티콘 모두 구매
//자신의 기준에 따라 구매 비용 합이 일정 가격 이상이면 이모티콘 플러스에 가입함

//각 인원마다 4가지 할인율을 적용해서 할인 가능 여부 및 최대 금액 구하면 될듯

import java.util.*;
class Solution {
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {0, 0};
        int[] dc = {10,20,30,40};
        Stack<Integer> dc_emo = new Stack<Integer>();
        
        //RC를 통해 할인율 정하면 될듯
        RC(0, dc_emo, dc, users, emoticons, answer);
        return answer;
    }
    
    //인덱스 값
    public void RC(int index, Stack<Integer> dc_emo, int[] dc, int[][] users, int[] emoticons, int[] answer) {
        
        //값 구하는 로직
        if (index == emoticons.length) {
            
            int price; //할인 가격
            int upper;
            int lower;
            int num = 0; //멤버쉽 가입 수
            int total = 0; //최고 금액 수
            
            
            //user를 돌면서 user가 현 상황에서 어떤 값을 가지는지 결정
            for (int[] user : users) {
                price = 0;
                lower = user[0]; //최소 비율, 이 비율 넘으면 구매
                upper = user[1]; //최대 금액, 이 금액 넘으면 멤버십 가입
                
                //lower보다 높으면 이모티콘을 구매
                for (int i=0; i<emoticons.length; i++) {
                    if (dc_emo.get(i) >= lower) { //i번째 이모티콘 할인율이 lower보다 높거나 같으면
                        price += (emoticons[i]*(100-dc_emo.get(i))/100); //구매
                    }
                    
                    //최대 금액을 넘으면
                    if (price >= upper) {
                        num += 1;
                        price = 0;
                        break;
                    }
                }
                total += price;
            }

            
            if (answer[0] < num) {
                answer[0] = num;
                answer[1] = total;
            } else if (answer[0] == num) {
                answer[1] = Math.max(answer[1], total);
            }
            
            return;
        }
        
        //4개중 하나 선택
        for (int i=0; i < 4; i++) {
            dc_emo.add(dc[i]);
            RC(index+1, dc_emo, dc, users, emoticons, answer);
            dc_emo.pop();
        }
        return;
    }
}