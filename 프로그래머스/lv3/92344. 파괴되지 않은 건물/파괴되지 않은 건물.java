//N*M 크기 행렬
//내구도가 감소하고 내구도가 0이하면 파괴
//내구도는 계속 하락
//파괴되지 않은 건물의 수

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        
        //skill 변수 초기화
        int type;
        int r1;
        int c1;
        int r2;
        int c2;
        int N = board.length;
        int M = board[0].length;
        int degree;
        int[][] graph = new int[N+1][M+1];
        
        for (int[] k : skill) {
            
            type = k[0];
            r1 = k[1];
            c1 = k[2];
            r2 = k[3];
            c2 = k[4];
            degree = k[5];           
            
            //적의 공격일 경우
            if (type == 1) {
                graph[r1][c1] -= degree;
                graph[r1][c2+1] += degree;
                graph[r2+1][c1] += degree;
                graph[r2+1][c2+1] -= degree;
            } else { //아군의 회복인 경우
                graph[r1][c1] += degree;
                graph[r1][c2+1] -= degree;
                graph[r2+1][c1] -= degree;
                graph[r2+1][c2+1] += degree;
            }
        }
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                graph[i][j+1] += graph[i][j];   
            }            
        }
        
        for (int j=0; j<M; j++) {
            for (int i=0; i<N; i++) {
                graph[i+1][j] += graph[i][j];    
            }            
        }
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                board[i][j] += graph[i][j];    
                if (board[i][j] > 0) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}