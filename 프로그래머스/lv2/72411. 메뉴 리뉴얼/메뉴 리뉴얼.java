//5:52
//메뉴를 새로 구성하려고 고민
//기존 단품을 코스요리 형태로 제공
//최소 2가지 이상의 단품 메뉴로 구성
//최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합만 메뉴 후보에 포함
//orders는 배열의 크기
//course는 배역의 크기가 10이하

//각 주문자에 맞춰 주문 건수 Map에 저장 그래서 Map 2개 이상인거 새로운 Map에 추가
//새로운 맵에서 각각 추가
//새로운 Map을 리스트 넣고 리스트 첫 값보다 큰 경우 새로운 리스트로 대체

import java.util.*;
class Solution {
    public String[] solution(String[] orders, int[] course) {
        String[] answer;
        String[] str;
        Map<String, Integer> info = new HashMap<>(); //메뉴마다 조회 수
        Map<Integer, List<String>> check = new HashMap<>(); //길이마다 최대 값 가지는 것으로 구현
        List<String> m;
        
        //문자열 초기화하면서 RC 실행
        for (String order : orders) {
            str = order.split("");
            Arrays.sort(str);
            RC(0, str, "", 0, info);
        }
        
        for (int cs : course) {
            m = new ArrayList();
            check.put(cs, m);
        }
        
        int k; //사이즈
        //키를 돌면서
        for (String key : info.keySet()) {
            
            if (info.get(key) == 1) {
                continue;
            }            
            
            //k는 길이
            k = key.length();
            
            if (!check.containsKey(k)) {
                continue;
            }
            
            if (check.get(k).size() == 0) {
                check.get(k).add(key);
                continue;
            }
            
            //리스트의 첫번째를 빼서 비교후 더 크면 새로 파고 작으면 
            if (info.get(check.get(k).get(0)) < info.get(key)) {
                m = new ArrayList<>();
                m.add(key);
                check.put(k,m);
            } else if (info.get(check.get(k).get(0)) == info.get(key)) {
                check.get(k).add(key);
            }
        }
        
        int total = 0;
        for (int key : check.keySet()) {
            total += check.get(key).size();
        }
        
        answer = new String[total];
        int c = 0;
        for (int key : check.keySet()) {
            for (String i : check.get(key)) {
                answer[c] = i;
                c++;
            }
        } 
        
        Arrays.sort(answer);
        return answer;
    }
    
    //각 문자열마다 실행되는 함수
    public void RC(int index, String[] str, String menu, int cnt, Map<String, Integer> info) {
        
        String nm = new String(menu);
        
        //모든 탐색이 끝났으면
        if (index == str.length) {
            
            if (cnt < 2) {
                return;
            }
            
            if (!info.containsKey(nm)) {
                info.put(nm, 0);
            }
            info.put(nm, info.get(nm)+1);
            return;
        }
        
        nm += str[index];
        RC(index+1, str, nm, cnt+1, info);
        RC(index+1, str, menu, cnt, info);
        return;
    }   
}