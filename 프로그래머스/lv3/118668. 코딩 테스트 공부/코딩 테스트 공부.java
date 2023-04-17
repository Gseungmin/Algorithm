//9:7
//알고력, 코딩력이 존재
//문제를 풀기 위해서는 일정 수준 이상의 알고력과 코딩력이 필요
//알고력과 코딩력은 1의 시간을 통해 1 높일 수 있음
//각 문제마다 올라가는 알고력과 코딩력이 정해져 있음
//같은 문제를 여러번 푸는 것이 가능함
//주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단 시간

import java.util.*;

class Node {
    
    int d;
    int al;
    int co;
    
    public Node(int d, int al, int co) {
        this.d = d;
        this.al = al;
        this.co = co;
    }
}

class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0; //답
        int max_al = 0; //목표 알고력
        int max_co = 0; //목표 코딩력
        int value = 0; //목표 코딩력
        Node now;
        int k;
        int x;
        int y;
        int nk;
        int nx;
        int ny;
        
        // //모든 문제들을 돌면서 최대 알고력과 코딩력 구하기
        // for (int[] problem : problems) {
        //     max_al = Math.max(max_al, problem[0]);
        //     max_co = Math.max(max_co, problem[1]);
        // }
        
        //다익스트라 초기화
        PriorityQueue<Node> queue = new PriorityQueue<Node>((o1, o2) -> {
            return o1.d - o2.d;
        });
        int Max = 10000000;
        boolean[][] check = new boolean[151][151];
        int[][] dist = new int[151][151];
        
        for (int i=0; i<151 ; i++) {
            for (int j=0; j<151 ; j++) {
                dist[i][j] = Max;
            }
        }
        
        dist[alp][cop] = 0;
        queue.add(new Node(0,alp,cop));
        
        //다익스트라 알고리즘
        while (queue.size() > 0) {
            now = queue.poll();
            k = now.d;
            x = now.al;
            y = now.co;
            
            //이미 최단거리 구해짐
            if (check[x][y] == true) {
                continue;
            }
            check[x][y] = true;
            
            // //종료조건
            // if ((x == max_al) & (y == max_co)) {
            //     answer = k;
            //     break;
            // }
            
            value = 0;
            //문제들 돌면서 풀 수 있으면 풀기
            for (int[] problem : problems) {
                if ((x >= problem[0]) & (y >= problem[1])) {
                    value += 1;
                    nx = Math.min(150, x+problem[2]);
                    ny = Math.min(150, y+problem[3]);
                    if (check[nx][ny] == false) {
                        if (dist[nx][ny] > k+problem[4]) {
                            dist[nx][ny] = k+problem[4];
                            queue.add(new Node(dist[nx][ny], nx, ny));
                        }
                    }
                }
            }
            
            if (value == problems.length) {
                answer = k;
                break;
            }

            if (x < 150) {
                nx = x+1;
                //알고리즘 공부
                if (check[nx][y] == false) {
                    if (dist[nx][y] > k+1) {
                        dist[nx][y] = k+1;
                        queue.add(new Node(dist[nx][y], nx, y));
                    }
                }
            }
            
            if (y < 150) {
                ny = y+1;
                //코딩 공부
                if (check[x][ny] == false) {
                    if (dist[x][ny] > k+1) {
                        dist[x][ny] = k+1;
                        queue.add(new Node(dist[x][ny], x, ny));
                    }
                } 
            }
        }
        return answer;
    }
}