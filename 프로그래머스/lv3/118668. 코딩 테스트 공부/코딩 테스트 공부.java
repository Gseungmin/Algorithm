import java.util.*;

class Node {
    
    int d; //거리
    int al; //알고력
    int co; //코딩력
    
    //생성자
    public Node(int d, int al, int co) {
        this.d = d;
        this.al = al;
        this.co = co;
    }
}

class Solution {

    public static int k;
    
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;
        boolean[][] check = new boolean[151][151];
        int[][] dist = new int[151][151];
        
        int Max = 100000000;
        for (int i=0; i<151; i++) {
            for (int j=0; j<151; j++) {
                dist[i][j] = Max;
            }
        }
        dist[alp][cop] = 0;
        
        PriorityQueue<Node> heap = new PriorityQueue<>((o1, o2) -> {
            return o1.d-o2.d;
        });
        
        
        heap.add(new Node(0,alp,cop));
        
        int d;
        int al;
        int co;
        int nal;
        int nco;
        Node now;
        boolean c;
        //다익스트라 시작
        while (heap.size() > 0) {
            now = heap.poll();
            d = now.d;
            al = now.al;
            co = now.co;
            
            
            if (check[al][co] == true) {
                continue;
            }
            
            check[al][co] = true;
            
            c = true;
            //모든 경우 다 할 수 있는지 파악
            for (int[] problem : problems) {
                //풀수 있다면
                if ((problem[0] <= al) && (problem[1] <= co)) {
                    nal = Math.min(al+problem[2], 150);
                    nco = Math.min(co+problem[3], 150);
                    
                    if (check[nal][nco] == false) {
                        
                        if (dist[nal][nco] > d + problem[4]) {
                            dist[nal][nco] = d + problem[4];
                            heap.add(new Node(dist[nal][nco], nal, nco));
                        }
                    }

                } else {
                    c = false;
                }
            }
            
            if (c == true) {
                answer = d;
                return answer;
            }
            
            nal = Math.min(al+1, 150);
            nco = Math.min(co+1, 150);

            if (check[nal][co] == false) {

                if (dist[nal][co] > d + 1) {
                    dist[nal][co] = d + 1;
                    heap.add(new Node(dist[nal][co], nal, co));
                }
            }
            
            if (check[al][nco] == false) {

                if (dist[al][nco] > d + 1) {
                    dist[al][nco] = d + 1;
                    heap.add(new Node(dist[al][nco], al, nco));
                }
            }
        }
        
        
        
        return answer;
    }
}