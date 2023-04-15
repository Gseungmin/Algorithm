//8:13
//대기실운 5개이며 각 대기실은 5*5 크기
//거리가 2이하로 안지는 말아야 함, 단 파티션으로 막혀있는 경우 가능
//P는 응시자, 0은 빈 테이블, X는 파티션
//각 대기실별로 거리두기를 지키고 있는지 확인

import java.util.*;

class Node {
    
    int x;
    int y;
    int d;
    
    public Node(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }
}

class Solution {
    public int[] solution(String[][] places) {
        int[] answer = {0,0,0,0,0};
        boolean[][] check;
        int cnt;
        Deque<Node> queue;
        String[] row;
        Node now; //현재 위치
        int[] dx = {0,0,-1,1};
        int[] dy = {1,-1,0,0};
        String[][] graph;
        int x;
        int y;
        int nx;
        int ny;
        
        //각 장소에서 거리두기 확인
        //P에서 2이하의 거리로 다른 P로 이동할 수 있으면 안됨
        cnt = 0;
        for (String[] place : places) {
            graph = new String[5][5];
            for (int i=0; i<5; i++) {
                row = place[i].split("");
                graph[i] = row;
            }
            //경우의수 돌면서 P이면 queue에 추가
            queue = new LinkedList<Node>();
            for (int i=0; i<5; i++) {
                for (int j=0; j<5; j++) {
                    if (graph[i][j].equals("P")) {
                        check = new boolean[5][5];
                        queue.add(new Node(i,j,0));
                        check[i][j] = true;
                        
                        while (queue.size() > 0) {
                            now = queue.pop();
                            x = now.x;
                            y = now.y;
                            
                            //다른 P와 만나면 거리두기 x
                            if ((graph[x][y].equals("P")) & (now.d != 0)) {
                                answer[cnt] = 1;
                                break;
                            }
                            
                            //2이면 더이상 진행 X
                            if (now.d == 2) {
                                continue;
                            }
                            
                            for (int k=0; k<4; k++) {
                                nx = x+dx[k];
                                ny = y+dy[k];
                                
                                if ((0<=nx)&(nx<5)&(0<=ny)&(ny<5)) {
                                    if (check[nx][ny] == false) {
                                        if (!graph[nx][ny].equals("X")) {
                                            check[nx][ny] = true;
                                            queue.add(new Node(nx,ny,now.d+1));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            cnt++;
        }
        
        for (int i=0; i<5; i++) {
            if (answer[i] == 0) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        
        return answer;
    }
}