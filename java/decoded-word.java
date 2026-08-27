//import java.util.Scanner;  --> if user input had to be taken

public class NotePassing {

    public static String decipher(String codedMessage) {
        String decm = "";
        
        for (int i = 0; i < codedMessage.length(); i++) {
            char ch = codedMessage.charAt(i);
            
            if (ch == 'A') decm += 'H';
            else if (ch == 'a') decm += 'h';
            else if (ch == 'B') decm += 'I';
            else if (ch == 'b') decm += 'i';
            else if (ch == 'C') decm += 'J';
            else if (ch == 'c') decm += 'j';
            else if (ch == 'D') decm += 'K';
            else if (ch == 'd') decm += 'k';
            else if (ch == 'E') decm += 'L';
            else if (ch == 'e') decm += 'l';
            else if (ch == 'F') decm += 'M';
            else if (ch == 'f') decm += 'm';
            else if (ch == 'G') decm += 'N';
            else if (ch == 'g') decm += 'n';
            else if (ch == 'H') decm += 'O';
            else if (ch == 'h') decm += 'o';
            else if (ch == 'I') decm += 'P';
            else if (ch == 'i') decm += 'p';
            else if (ch == 'J') decm += 'Q';
            else if (ch == 'j') decm += 'q';
            else if (ch == 'K') decm += 'R';
            else if (ch == 'k') decm += 'r';
            else if (ch == 'L') decm += 'S';
            else if (ch == 'l') decm += 's';
            else if (ch == 'M') decm += 'T';
            else if (ch == 'm') decm += 't';
            else if (ch == 'N') decm += 'U';
            else if (ch == 'n') decm += 'u';
            else if (ch == 'O') decm += 'V';
            else if (ch == 'o') decm += 'v';
            else if (ch == 'P') decm += 'W';
            else if (ch == 'p') decm += 'w';
            else if (ch == 'Q') decm += 'X';
            else if (ch == 'q') decm += 'x';
            else if (ch == 'R') decm += 'Y';
            else if (ch == 'r') decm += 'y';
            else if (ch == 'S') decm += 'Z';
            else if (ch == 's') decm += 'z';
            else if (ch == 'T') decm += 'A';
            else if (ch == 't') decm += 'a';
            else if (ch == 'U') decm += 'B';
            else if (ch == 'u') decm += 'b';
            else if (ch == 'V') decm += 'C';
            else if (ch == 'v') decm += 'c';
            else if (ch == 'W') decm += 'D';
            else if (ch == 'w') decm += 'd';
            else if (ch == 'X') decm += 'E';
            else if (ch == 'x') decm += 'e';
            else if (ch == 'Y') decm += 'F';
            else if (ch == 'y') decm += 'f';
            else if (ch == 'Z') decm += 'G';
            else if (ch == 'z') decm += 'g';
            else decm += ch;
        }

        return decm;
    }

/*
public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter your text: ");
        String userText = scanner.nextLine(); 
        
        String result = decipher(userText); 
        System.out.println("Decoded message: " + result);
        
        scanner.close();
    }
}
*/
