import java.util.*;
class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        
        //변수 초기화
        int[] answer = new int[sources.length];
        int k = -1;
        int value = -1;
        Integer x = -1, y = -1;
        boolean[] True = new boolean[n+1];
        int[] dist = new int[n+1];
        
        //graph 초기화
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        
        for (int[] road : roads) {
            x = road[0];
            y = road[1];
            graph.get(x).add(y);
            graph.get(y).add(x);
        }
        
        //BFS 시작
        True[destination] = true;
        Deque<Integer> queue = new LinkedList<Integer>();
        queue.add(destination);
        
        while (queue.size() > 0) {
            x = queue.pollFirst();
            
            for (Integer nx : graph.get(x)) {
                if (True[nx] == false) {
                    dist[nx] = dist[x] + 1;
                    True[nx] = true;
                    queue.add(nx);
                }    
            }
        }
        
        for (int i = 0; i < sources.length; i++) {
            value = dist[sources[i]];
            if (value != 0) {
                answer[i] = dist[sources[i]];
                continue;
            }
            if (sources[i] != destination) {
                answer[i] = -1;
            }
        }
        return answer;
    }
}