//11:00
//테두리 부분을 시계방향으로 회전, 

import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        
        //graph 초기화
        int count = 1;
        int[][] graph = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                graph[i][j] = count;
                count++;
            }
        }
        
        int ans_index = 0;
        
        //쿼리 실행
        for (int[] query : queries) {
            
            //인덱스 정리
            int x1 = query[0]-1, y1 = query[1]-1, x2 = query[2]-1, y2 = query[3]-1;
            
            int value = 100000000;
            
            //큐 초기화
            Deque<Integer> queue = new LinkedList<Integer>();
            for (int i = y1; i <= y2; i++) {
                queue.add(graph[x1][i]);
                value = Math.min(value, graph[x1][i]);
            }
            
            for (int i = x1+1; i < x2; i++) {
                queue.add(graph[i][y2]);
                value = Math.min(value, graph[i][y2]);
            }
            
            for (int i = y2; i >= y1; i--) {
                queue.add(graph[x2][i]);
                value = Math.min(value, graph[x2][i]);
            }
            
            for (int i = x2-1; i > x1; i--) {
                queue.add(graph[i][y1]);
                value = Math.min(value, graph[i][y1]);
            }
            
            
            queue.addFirst(queue.pollLast());

            //배열 초기화
            for (int i = y1; i <= y2; i++) {
                graph[x1][i] = queue.pollFirst();
            }
            
            for (int i = x1+1; i < x2; i++) {
                graph[i][y2] = queue.pollFirst();
            }
            
            for (int i = y2; i >= y1; i--) {
                graph[x2][i] = queue.pollFirst();
            }
            
            for (int i = x2-1; i > x1; i--) {
                graph[i][y1] = queue.pollFirst();
            }
            
            answer[ans_index] = value;
            ans_index++;
        }
        
        return answer;
    }
}