//8:6
//n발을 다 쏜 후 n발을 발싸
//10~0점이 있음
//k점을 a발 b말 맞출 경우 더 많이 k점에 화살을 맞춘 사람이 가져감, 같을 경우 어피치가 가져감
//여러발 맞추더라도 k점만 가져감
//모든 과녁 점수에 대하여 각 선수의 최종 점수를 계산
//최종 점수가 같을 경우 어피치의 승리
//라이언은 어피치를 이기기 위해 가장 큰 점수 차이로 이기기 위해 어떤 과녁에 점수를 맞춰야 하는지 구하려 함
//n은 화살의 개수
//info는 어피치의 과녁 점수
//가장 낮은 점수를 더 많이 맞힌 경우를 리턴
//백트레킹으로 풀어보자

import java.util.*;
class Solution {
    public int[] solution(int n, int[] info) {
        int[] answer = new int[11];
        int[] lion = new int[11];
        int[] dif = {-1};
        
        //RC 시작
        RC(n, 10, lion, info, answer, dif);
        
        if (dif[0] == -1) {
            return dif;
        }
        
        return answer;
    }
    
    //k는 남은 화살 수
    public void RC(int k, int index, int[] lion, int[] info, int[] answer, int[] dif) {
        
        //모든 화살을 다 쏜 경우
        if (k == 0) {
            
            int a = 0; //어피치 점수
            int l = 0; //라이언 점수
            
            //점수 계산
            for (int i=0; i<answer.length; i++) {
                if (lion[i] > info[i]) {
                    l += 10-i;
                } else {
                    if (info[i] != 0) {
                        a += 10-i;    
                    }
                }
            }
            
            //라이언이 더 큰 점수
            if (l > a) {
                
                if (dif[0] == -1) {
                   
                    //배열 정리
                    dif[0] = l-a;
                    for (int i=0; i<answer.length; i++) {
                        answer[i] = lion[i];    
                    }
                    
                } else {
                    if (dif[0] < l-a) {
                        dif[0] = l-a;
                        
                        //배열 정리
                        for (int i=0; i<answer.length; i++) {
                            answer[i] = lion[i];
                        }
                    }    
                }
            }
            
            return;
        }
        
        //마지막 인덱스인 경우
        if (index == 0) {
            lion[index] = k;
            RC(0, index-1, lion, info, answer, dif);
            lion[index] = 0;
        } else {            
            //마지막 인덱스가 아닌 경우
            for (int i=k; i>=0; i--) {
                lion[index] = i;
                RC(k-i, index-1, lion, info, answer, dif);
                lion[index] = 0;
            }
        }
        return;
    }
}