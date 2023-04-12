//11:43
//칫솔 판매 시 이익이 조직을 타고 분배
//누가 얼마큼의 이익을 가졌는지 파악
//발생 이익의 10%를 추천인에게 배분하고 나머지 가짐
//리프노드에서 10%반환
//부모노드는 자식 노드에서 반환 받은 값 % 10를 부모 노드에 보냄

import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];
        
        //트리 초기화
        HashMap<String, List<String>> tree = new HashMap<String, List<String>>();
        
        for (int i = 0; i < enroll.length; i++) {
            if (!tree.containsKey(referral[i])){
                tree.put(referral[i], new ArrayList<String>());
            }
            tree.get(referral[i]).add(enroll[i]);
        }
        
        //수익 초기화
        HashMap<String, List<Integer>> money = new HashMap<String, List<Integer>>();
        for (int i = 0; i < seller.length; i++) {
            if (!money.containsKey(seller[i])) {
                money.put(seller[i], new ArrayList<Integer>());
            }
            money.get(seller[i]).add(amount[i]);
        }
        
        //index 초기화
        HashMap<String, Integer> index = new HashMap<String, Integer>();
        int cnt = 0;
        for (String i : enroll) {
            index.put(i, cnt);
            cnt++;
        }
        
        rc("-", index, answer, tree, money);
        
        return answer;
    }
    
    //재귀함수
    public List<Integer> rc(String x, HashMap<String, Integer> index, int[] answer, HashMap<String, 
                      List<String>> tree, HashMap<String, List<Integer>> money) {
        
        List<Integer> arr = new ArrayList<Integer>();
        List<Integer> returnArr = new ArrayList<Integer>();
        int ind = -1; //인덱스
        int all = 0; //판매가
        int amount = 0; //저장 값
        int value = 0; //퍼센트 값

        if (index.containsKey(x)) {
            ind = index.get(x);    
        }
        
        //수익이 있을 경우
        if (money.containsKey(x)) {
            for (int i : money.get(x)) {
                all = i*100; //판매가
                value = all/10; //반환할 값 넣기
                arr.add(value);
                amount += all-value;
            }
        }
        
        //리프노드일 경우
        if (!tree.containsKey(x)) {
            answer[ind] = amount;
            return arr;
        }
        
        //리프 노드가 아닐 경우
        for (String next : tree.get(x)) {
            returnArr = rc(next, index, answer, tree, money);
            
            //k는 반환받은 값
            for (int k : returnArr) {
                value = k/10;
                if (value != 0) {
                    arr.add(value);
                }
                amount += k-value;
            }
        }
        
        if (ind != -1) {
            answer[ind] = amount;
        }
        
        return arr;
    }
}