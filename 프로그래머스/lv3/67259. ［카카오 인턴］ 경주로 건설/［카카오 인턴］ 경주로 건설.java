// N*N, 상하좌우, 1은 벽, 0은 이동가능 경로, 직선도로 100, 코너 500
// 가려는 경로 및 이전에 이동한 경로 필요

import java.util.*;

class Node {
    
    int cost;
    int prev;
    int x;
    int y;
    
    public Node(int cost, int prev, int x, int y) {
        this.cost = cost;
        this.prev = prev;
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int solution(int[][] board) {
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        int px;
        int py;
        int nx;
        int ny;
        int pd;
        int nd;
        int c;
        int Max = 1000000000;
        int answer = Max;
        int len = board.length;
        Node now;
        
        //큐 정의
        PriorityQueue<Node> queue = 
            new PriorityQueue<Node>((o1,o2) -> {
                return o1.cost - o2.cost;
            });
        
        //우선순위 큐 초기화
        queue.add(new Node(0,0,0,0));
        queue.add(new Node(0,1,0,0));
        queue.add(new Node(0,2,0,0));
        queue.add(new Node(0,3,0,0));
        boolean[][][] check = new boolean[len][len][4];
        int[][][] dist = new int[len][len][4];
        
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                for (int k = 0; k < 4; k++) {
                    dist[i][j][k] = Max;
                }    
            }    
        }
        
        dist[0][0][0] = 0;
        dist[0][0][1] = 0;
        dist[0][0][2] = 0;
        dist[0][0][3] = 0;
        
        while (queue.size() > 0) {
            now = queue.poll();
            
            px = now.x;
            py = now.y;
            pd = now.prev;
            c = now.cost;
            
            if (check[px][py][pd] == true) {
                continue;
            }
            
            check[px][py][pd] = true;
            
            //이동
            for (int i = 0; i < 4; i++) {
                nx = px+dx[i];
                ny = py+dy[i];
                nd = i;
                
                if ((0 <= nx) & ( nx < len) & (0 <= ny) & ( ny < len)) {
                    //이동 가능할 경우
                    if (board[nx][ny] == 0) {

                        if (check[nx][ny][nd] == false) {

                            if (pd == nd) { //방향이 같은 경우
                                if (dist[nx][ny][nd] > c + 100) {
                                    dist[nx][ny][nd] = c + 100;
                                    queue.add(new Node(dist[nx][ny][nd],nd,nx,ny));
                                }
                            }

                            if (pd != nd) { //방향이 다른 경우
                                if (dist[nx][ny][nd] > c + 600) {
                                    dist[nx][ny][nd] = c + 600;
                                    queue.add(new Node(dist[nx][ny][nd],nd,nx,ny));
                                }
                            }                    
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < 4; i++) {
            answer = Math.min(answer, dist[len-1][len-1][i]);
        }
        return answer;
    }
}