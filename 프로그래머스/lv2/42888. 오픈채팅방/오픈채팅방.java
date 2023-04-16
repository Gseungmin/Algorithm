//7:40
//가상의 닉네임으로 채팅방에 입장
//닉네임을 변경하려면 채팅방을 나갔다 입장하거나 채팅방에서 변경
//닉네임을 변경할때는 기존에 채팅방에 출력되어 있던 메시지의 이름도 전부 변경
//중복 닉네임 허용
//최종 메시지를 문자열 배열형태로 나타내라

import java.util.*;
class Node {
    
    String id;
    int k;
    
    public Node(String id, int k) {
        this.id = id;
        this.k = k;
    }
}

class Solution {
    public String[] solution(String[] record) {
        String[] command;
        String id;
        int k;
        List<Node> arrays = new ArrayList<>();
        HashMap<String, String> match = new HashMap<>();
        
        //기록을 돌면서 저장
        for (String i : record) {
            command = i.split(" ");
            
            //입장한 경우
            if (command[0].equals("Enter")) {
                match.put(command[1], command[2]);
                arrays.add(new Node(command[1], 0));
            }
            
            //퇴장한 경우
            if (command[0].equals("Leave")) {
                arrays.add(new Node(command[1], 1));
            }
            
            //변경한 경우
            if (command[0].equals("Change")) {
                match.put(command[1], command[2]);
            }
        }
        
        String[] answer = new String[arrays.size()];
        
        int cnt = 0;
        for (Node node : arrays) {
            
            id = node.id;
            k = node.k;
            
            if (k == 0) {
                answer[cnt] = match.get(id) + "님이 들어왔습니다.";
            }
            
            if (k == 1) {
                answer[cnt] = match.get(id) + "님이 나갔습니다.";
            }
            
            cnt++;
        }
        
        return answer;
    }
}