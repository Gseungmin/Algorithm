//6:43
//가장 많이 보는 구간에 공익광고를 넣음
//삽입될 최적의 위치
import java.util.*;
class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        String answer = "";
        int p;
        int n;
        int end;
        String ps;
        String ns;
        String[] k;
        long[] total;
        Map<Integer, Integer> info = new HashMap<>();
        
        //로그 돌면서 정보 반영
        for (String log : logs) {
            k = log.split("-");
            ps = k[0];
            ns = k[1];
            
            p = Integer.parseInt(ps.substring(0,2))*60*60 + 
                Integer.parseInt(ps.substring(3,5))*60 + Integer.parseInt(ps.substring(6,ps.length()));
            
            n = Integer.parseInt(ns.substring(0,2))*60*60 + 
                Integer.parseInt(ns.substring(3,5))*60 + Integer.parseInt(ns.substring(6,ns.length()));
            
            if (!info.containsKey(p)) {
                info.put(p, 0);
            }
            info.put(p, info.get(p)+1);
            
            if (!info.containsKey(n)) {
                info.put(n, 0);
            }
            info.put(n, info.get(n)-1);
        }
        
        int left = 0;
        int right = 0;
        long time = 0;
        
        right = Integer.parseInt(adv_time.substring(0,2))*60*60 + 
            Integer.parseInt(adv_time.substring(3,5))*60 + Integer.parseInt(adv_time.substring(6,adv_time.length()));
        
        right -= 1;
        
        end = Integer.parseInt(play_time.substring(0,2))*60*60 + 
            Integer.parseInt(play_time.substring(3,5))*60 + Integer.parseInt(play_time.substring(6,play_time.length()));
        
        total = new long[end+1];
        
        long Sum = 0;
        for (int i=0; i<=end; i++) {
            if (info.containsKey(i)) {
                Sum += info.get(i);
            }
            total[i] = Sum;
            if (i <= right) {
                time += Sum;
            }
        }
        
        //최댓값 기준 설정
        long mx = time;
        int ml = 0;
        int mr = right;
        
        //end까지 실행
        while (right < end) {
            time -= total[left];
            left++;
            right++;
            time += total[right];
            
            if (time > mx) {
                ml = left;
                mr = right;
                mx = time;
            }
        }
        
        int a = (ml/60)/60;
        int b = (ml-(a*60*60))/60;
        int c = ml-(a*60*60)-(b*60);
        String as = Integer.toString(a);
        String bs = Integer.toString(b);
        String cs = Integer.toString(c);
        if (as.length() < 2) {
            as = "0"+as;
        }
        if (bs.length() < 2) {
            bs = "0"+bs;
        }
        if (cs.length() < 2) {
            cs = "0"+cs;
        }
        answer = as + ":";
        answer += bs;
        answer += ":";
        answer += cs;
        
        return answer;
    }
}