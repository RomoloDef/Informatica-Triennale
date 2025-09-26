package CampoMinato;

import java.util.Scanner;
import java.util.Random;

public class CampoMinato {
	
	Scanner scanner = new Scanner(System.in);
	private int N; // N del campo
	private int M; // M del campo
	private int[][] campo;
	private boolean[][] scoperto;
	
	// Costruttore
	public CampoMinato(int N, int M, int m) {
		this.N = N;
		this.M = M;
		this.campo = new int[N][M];
		this.scoperto = new boolean[N][M];

        Random rand = new Random();
        for (int i = 0; i < m; i++) {
            int x, y;
            do {
                x = rand.nextInt(N);
                y = rand.nextInt(M);
            } while (campo[x][y] == -1);

            campo[x][y] = -1;

            for (int dx = -1; dx <= 1; dx++) {
                for (int dy = -1; dy <= 1; dy++) {
                    int nx = x + dx, ny = y + dy;
                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && campo[nx][ny] != -1) {
                        campo[nx][ny]++;
                    }
                }
            }
        }
    }
	
	// Metodo scopri
	public int scopri(int x, int y) {
	        if (x < 0 || x >= N || y < 0 || y >= M) {
	            return 0;
	        }

	        if (scoperto[x][y]) {
	            return campo[x][y];
	        }

	        scoperto[x][y] = true;

	        if (campo[x][y] == -1) {
	            return -1;
	        }

	        if (campo[x][y] == 0) {
	            for (int dx = -1; dx <= 1; dx++) {
	                for (int dy = -1; dy <= 1; dy++) {
	                    scopri(x + dx, y + dy);
	                }
	            }
	        }

	        return campo[x][y];
	    }
	
	// Metodo toString
	public String toString() {
	    String result = "";
	    for (int i = 0; i < N; i++) {
	        for (int j = 0; j < M; j++) {
	            if (scoperto[i][j]) {
	                if (campo[i][j] == -1) {
	                    result += 'M'; // M per mina
	                } else {
	                    result += campo[i][j]; // numero di mine adiacenti
	                }
	            } else {
	                result += '.'; // . per casella non scoperta
	            }
	            result += ' ';
	        }
	        result += '\n';
	    }
	    return result;
	}
	
	// Metodo vinto
	public String vinto() {
	    for (int i = 0; i < N; i++) {
	        for (int j = 0; j < M; j++) {
	            if (campo[i][j] != -1 && !scoperto[i][j]) {
	                return "In gioco"; // Se c'è una casella non scoperta che non è una mina, il gioco è ancora in corso
	            }
	        }
	    }

	    for (int i = 0; i < N; i++) {
	        for (int j = 0; j < M; j++) {
	            if (campo[i][j] == -1 && scoperto[i][j]) {
	                return "Perso"; // Se c'è una mina scoperta, il giocatore ha perso
	            }
	        }
	    }

	    return "Vinto"; // Se tutte le caselle che non sono mine sono state scoperte e nessuna mina è stata scoperta, il giocatore ha vinto
	}
	
}

	


	
	
	

