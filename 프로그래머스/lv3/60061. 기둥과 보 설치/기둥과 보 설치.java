//12:5
//기둥과 보를 이용해 구조물 세울려 함, 기둥과 보는 길이가 1인 선분으로 표시
//기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 었거나 또는 다른 기둥 위
//보는 한쪽 끝부분이 기둥위거나 양쪽 끝 부분이 다른 보와 연결되어 있어야 함
//보는 오른쪽을 기준으로 설치
//삭제도 가능한데 삭제하려면 규칙을 만족해야 함
//설치나 삭제시 규칙을 어긴다면 무시
//보는 좌표기준 오른쪽으로, 즉 (1,1) -> (2,1) 
//기둥은 좌표기준 위쪽으로, 즉 (1,0) -> (1,1)

import java.util.*;
class Solution {
    public int[][] solution(int n, int[][] build_frame) {
        
        //좌표 및 삭제 설치
        int x;
        int y;
        int s; //구조물, 0이면 기둥, 1은 보
        int c; //삭제나 설치, 0이면 삭제 1이면 설치
        
        //기둥과 보 체크, key는 좌표, value는 기둥 또는 보
        Map<List<Integer>, Integer> col = new HashMap<>();
        Map<List<Integer>, Integer> row = new HashMap<>();
            
        for (int[] arr : build_frame) {
            x = arr[0];
            y = arr[1];
            s = arr[2];
            c = arr[3];
            
            //삭제일 경우
            if (c == 0) {
                delete(x,y,s,col,row);
            }
            
            //설치일 경우
            if (c == 1) {
                create(x,y,s,col,row);
            }
        }
        
        int[][] answer = new int[col.size()+row.size()][3];
        int[] each;
        int cnt = 0;
        for (List<Integer> k : col.keySet()) {
            each = new int[3];
            each[0] = k.get(0);
            each[1] = k.get(1);
            each[2] = 0;
            answer[cnt] = each;
            cnt++;
        }
        
        for (List<Integer> k : row.keySet()) {
            each = new int[3];
            each[0] = k.get(0);
            each[1] = k.get(1);
            each[2] = 1;
            answer[cnt] = each;
            cnt++;
        }
        
        Arrays.sort(answer, (o1, o2)->{
            if ((o1[0] == o2[0]) && (o1[1] == o2[1])) {
                return o1[2] - o2[2];
            } else if (o1[0] == o2[0]) {
                return o1[1]-o2[1];
            } else {
                return o1[0]-o2[0];
            }
        });
        
        return answer;
    }
    
    //유지 가능성
    public boolean check(int x, int y, int s, Map<List<Integer>, Integer> col, Map<List<Integer>, Integer> row) {
        
        //기둥일 경우
        if (s == 0) {
            
            //바닥일 경우 
            if ((y == 0)) {
                return true;
            }
            
            //아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x,y-1))) {
                return true;
            }
            
            //왼쪽에 보가 설치된 경우
            if (row.containsKey(Arrays.asList(x-1,y))) {
                return true;
            }
            
            //오른쪽에 보가 설치된 경우
            if (row.containsKey(Arrays.asList(x,y))) {
                return true;
            }
        } else {
            
            //왼쪽 아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x,y-1))) {
                return true;
            }
            
            //오른쪽 아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x+1,y-1))) {
                return true;
            }
            
            //양쪽에 보가 있는 경우
            //오른쪽 아래에 기둥이 설치된 경우
            if ((row.containsKey(Arrays.asList(x-1,y))) && (row.containsKey(Arrays.asList(x+1,y)))) {
                return true;
            }
        }
        
        return false;
    }
    
    
    //삭제 모듈화
    public void delete(int x, int y, int s, Map<List<Integer>, Integer> col, Map<List<Integer>, Integer> row) {
        
        boolean b = false;
        
        //기둥일 경우
        if (s == 0) {
            
            //기둥 삭제
            col.remove(Arrays.asList(x,y));
            
            if (col.containsKey(Arrays.asList(x,y+1))) {
                //바로 위 기둥이 안전한지 판단
                b = check(x,y+1,0,col,row);

                //기둥이 안전하지 않으면 무시
                if (b == false) {
                    col.put(Arrays.asList(x,y), 0);
                    return;
                }
            }
            
            //바로 위 오른쪽 보가 안전한지 판단
            if (row.containsKey(Arrays.asList(x,y+1))) {
                b = check(x,y+1,1,col,row);

                //기둥이 안전하지 않으면 무시
                if (b == false) {
                    col.put(Arrays.asList(x,y), 0);
                    return;
                }
            }
            
            if (row.containsKey(Arrays.asList(x-1,y+1))) {
                //바로 위 왼쪽 보가 안전한지 판단
                b = check(x-1,y+1,1,col,row);

                //기둥이 안전하지 않으면 무시
                if (b == false) {
                    col.put(Arrays.asList(x,y), 0);
                    return;
                }
            }
            
        } else {

            //보 삭제
            row.remove(Arrays.asList(x,y));
            
            if (col.containsKey(Arrays.asList(x,y))) {
                //보 왼쪽 위 기둥이 안전한지 판단
                b = check(x,y,0,col,row);

                //기둥이 안전하지 않으면 무시
                if (b == false) {
                    row.put(Arrays.asList(x,y), 1);
                    return;
                }
            }
            
            if (col.containsKey(Arrays.asList(x+1,y))) {
                //보 오른쪽 기둥이 안전한지 판단
                b = check(x+1,y,0,col,row);

                //기둥이 안전하지 않으면 무시
                if (b == false) {
                    row.put(Arrays.asList(x,y), 1);
                    return;
                }
            }
            
            if (row.containsKey(Arrays.asList(x-1,y))) {
                //왼쪽 보가 안전한지 판단
                b = check(x-1,y,1,col,row);

                //보가 안전하지 않으면 무시
                if (b == false) {
                    row.put(Arrays.asList(x,y), 1);
                    return;
                }
            }
            
            if (row.containsKey(Arrays.asList(x+1,y))) {
                //왼쪽 보가 안전한지 판단
                b = check(x+1,y,1,col,row);

                //보가 안전하지 않으면 무시
                if (b == false) {
                    row.put(Arrays.asList(x,y), 1);
                    return;
                }
            }
        }
    }
    
    //설치 모듈화
    public void create(int x, int y, int s, Map<List<Integer>, Integer> col, Map<List<Integer>, Integer> row) {
        
        //기둥일 경우
        if (s == 0) {
            //1,1에 설치하려면 1,0에 기둥이 설치되어 있거나, 0,1 또는 1,1에 보가 있어야 함
            
            //바닥일 경우 
            if ((y == 0)) {
                col.put(Arrays.asList(x,y), 0);
                return;
            }
            
            //아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x,y-1))) {
                col.put(Arrays.asList(x,y), 0);
                return;
            }
            
            //왼쪽에 보가 설치된 경우
            if (row.containsKey(Arrays.asList(x-1,y))) {
                col.put(Arrays.asList(x,y), 0);
                return;
            }
            
            //오른쪽에 보가 설치된 경우
            if (row.containsKey(Arrays.asList(x,y))) {
                col.put(Arrays.asList(x,y), 0);
                return;
            }
        } else {
            
            //왼쪽 아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x,y-1))) {
                row.put(Arrays.asList(x,y), 1);
                return;
            }
            
            //오른쪽 아래에 기둥이 설치된 경우
            if (col.containsKey(Arrays.asList(x+1,y-1))) {
                row.put(Arrays.asList(x,y), 1);
                return;
            }
            
            //양쪽에 보가 있는 경우
            //오른쪽 아래에 기둥이 설치된 경우
            if ((row.containsKey(Arrays.asList(x-1,y))) && (row.containsKey(Arrays.asList(x+1,y)))) {
                row.put(Arrays.asList(x,y), 1);
                return;
            }
        }
    }
}