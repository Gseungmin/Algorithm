//10:48
//입차 및 출차 기록을 통해 차량별 주차 요금 계산
//입차된 이후 출차 내역이 없다면 23:59에 출차된 것으로 산주
//기본 시간 이하라면 기본 요금 청구
//기본 시간 초과시 기본 요금 + 단위시간마다 단위요금 청구
//단위시간 올림해서 구함
//잘못된 입력이 주어지지 않음

import java.util.*;
class Solution {
    public int[] solution(int[] fees, String[] records) {
        
        //차량 번호가 작은 자동차부터 주차요금 차례로
        //주차요금 구하고
        //주차요금을 map으로 저장해놓을 후
        //keySet()을 받아서 정렬한 후 answer 초기화 하면 될듯
        HashMap<String, Integer> money = new HashMap<>(); //요금을 정리할 Map
        HashMap<String, Integer> time = new HashMap<>(); //입차 시간을 정리할 Map
        HashMap<String, Integer> total = new HashMap<>(); //전체 시간을 정리할 Map
        String[] s1; //split
        String[] s2; //split
        String num; //차량 번호
        int pt; //입차시간
        int t; //시간
        int f; //요금
        int tf; //전체 요금
        int ft = 23*60+59; //마지막 시간
        
        for (String i : records) {
            s1 = i.split(" ");
            num = s1[1];
            s2 = s1[0].split(":");
            t = Integer.parseInt(s2[0])*60+Integer.parseInt(s2[1]); //현재 시각
            
            if (s1[2].equals("IN")) {
                if (!money.containsKey(num)) {
                    money.put(num, 0);
                }
                if (!total.containsKey(num)) {
                    total.put(num, 0);
                }
                time.put(num, t); //입차시간 입력
            } else if (s1[2].equals("OUT")) {
                
                pt = time.get(num); //입차한 시간
                total.put(num, total.get(num)+(t-pt));
                
                //입차한 차 제거
                time.remove(num);
            }
        }
        
        //출차 안한 차 시간 더하기
        for (String i : time.keySet()) {
            t= ft;
            pt = time.get(i); //입차한 시간
            total.put(i, total.get(i)+(t-pt));
        }
        
        //출차 안한 차 시간 더하기
        for (String i : total.keySet()) {
            
            t = total.get(i); //총 시간
            if (fees[0] < t) { //기본 시간보다 긴 경우
                
                //추가 요금
                if (((t-fees[0])%fees[2]) == 0) {
                    tf = ((t-fees[0])/fees[2])*fees[3];
                } else {
                    tf = (((t-fees[0])/fees[2])+1)*fees[3];
                }
                
                money.put(i, fees[1]+tf);
            } else { //기본 요금만 내면 됨
                money.put(i, fees[1]);
            }
        }
        
        List<String> key = new ArrayList<>();
        for (String i : money.keySet()) {
            key.add(i);
        }
        Collections.sort(key);
        
        int[] answer = new int[key.size()];
        
        for (int i=0; i<key.size(); i++) {
            answer[i] = money.get(key.get(i));
        }
        
        return answer;
    }
}