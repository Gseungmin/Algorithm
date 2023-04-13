//특정 범위의 보석을 모두 구매
//진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
//맨 끝에서부터 하나씩 제외하면 될듯?
import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {-1, -1};
        Deque<String> queue = new LinkedList<String>();
        
        HashSet<String> cnt = new HashSet<String>();
        for (String k : gems) {
            cnt.add(k);
        }
        
        //개수 정보 초기화
        HashMap<String, Integer> count = new HashMap<String, Integer>();

        //index
        int left = 0;
        int right = 0;
        int len = gems.length;
        String value;
        String gem;
        while (right < gems.length){
            
            gem = gems[right]; //추가할 보석
            queue.add(gem);
            
            //보석 추가
            if (count.containsKey(gem)) {
                count.put(gem, count.get(gem)+1);
            } else {
                count.put(gem, 1);
            }
            
            //맨 앞 보석 삭제할 수 있으면 삭제
            while (true) {
                value = queue.getFirst();
                if (count.get(value) > 1) { //하나가 더 커지면
                    count.put(value, count.get(value)-1);
                    queue.poll();
                    left++;
                } else {
                    break;
                }
            }
            
            //만약 모든 보석을 다 모았으면 자르기
            if (count.size() == cnt.size()) {
                if (len > right-left+1) {
                    len = right-left+1;
                    answer[0] = left+1;
                    answer[1] = right+1;
                }
            }
            right++;
        }
        
        if (answer[0] == -1) {
            answer[0] = left+1;
            answer[1] = right;
        }
        
        return answer;
    }
}