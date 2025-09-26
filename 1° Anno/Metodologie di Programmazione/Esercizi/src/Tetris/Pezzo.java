package Tetris;

public abstract class Pezzo {
	
	// costruisco le coordinate
	private int x;
	private int y;
	protected int[][] forma;
	
	public Pezzo(int x, int y, int[][] forma) {
		this.x = x;
		this.y = y;
		this.forma = forma;
	}
	
	// Getters
	public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public int[][] getForma() {
    	return forma;
    }
    
    // Setters
    public void setX(int x) {
		this.x = x;
	}

	public void setY(int y) {
		this.y = y;
	}

	public void setForma(int[][] forma) {
		this.forma = forma;
	}
	
	// metodo Left
	public void Left(int x, int y) {
		x--;
	}

	// metodo Right
	public void Right(int x, int y) {
		x++;
	}
	
	// metodo Down
	public void Down(int x, int y) {
		y--;
	}
	
	// metodo Rotate
	public abstract void Rotate();
	
}