import java.awt.Graphics;
import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Vector;

public class SudokuPuzzle 
{
	public static final int GRIDSIZE = 9;
	private NumberButton[] grid;
	private Entity[] columns;
	private Entity[] rows;
	private Entity[] boxes;
	private String[] puzzleStrings;
	private String[] patternStrings;
	private int openSquares;
	public static final int NOHELP = 0;
	public static final int EASIER = 1;
	public static final int EASIEST = 2;
	public static final int TEST = 3;
	private int playMode = 0;
	private SUD applet;

	public SudokuPuzzle(SUD sud, boolean testMode)
	{
		applet = sud;
		makeEntities();
		if (testMode)
		{
			String input = "";
	        try
	        {
			    BufferedReader br = new BufferedReader(new InputStreamReader(new URL(applet.getDocumentBase().toString().substring(0, applet.getDocumentBase().toString().lastIndexOf("/") + 1) + "input.txt").openStream()));
                input = br.readLine();
	            br.close();
			}	
			catch   (Exception e)
			{
	            System.out.println("Exception on input = " + e);
			}
			for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
			{
				grid[i] = new NumberButton(i, this, new Integer(input.substring(i, i + 1)).intValue());
				if (!("0".equals(input.substring(i, i + 1))))
				{
					grid[i].setPermanent(this);
				}
			}
			playMode = TEST;
		}
		else
		{	
			loadPuzzles(applet.getDocumentBase().toString());
			SUD.log("Number of puzzles loaded: " + puzzleStrings.length);
			// pick a puzzle
			if (9999 == applet.getPuzzleIndex())
			{	
				applet.setPuzzleIndex(tmFormatting.getRnd(puzzleStrings.length));
			}	
			String puzzleString = puzzleStrings[applet.getPuzzleIndex()];
			String patternString = patternStrings[applet.getPuzzleIndex()];
			// establish cipher for the puzzle
			int[] digits = tmFormatting.randomPicks(GRIDSIZE, GRIDSIZE);
			for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
			{
				grid[i] = new NumberButton(i, this, digits[(new Integer(puzzleString.substring(i, i + 1))).intValue() - 1] + 1);
				if ("1".equals(patternString.substring(i, i+1)))
				{
					grid[i].setPermanent(this);
				}	
			}
		}
		for (int i = 0; i < GRIDSIZE; i++)
		{
			rows[i].setArray();
			columns[i].setArray();
			boxes[i].setArray();
		}
	}
	public void writeCode()
	{
		String pattern = "";
		String puzzle = "";
		// generate strings for puzzleString and patternString
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			puzzle += getGrid()[i].getValue();
			pattern += (getGrid()[i].getStatus() == NumberButton.PERMANENT) ? "1" : "0";
		}
		System.out.println(puzzle);
		System.out.println(pattern);
	}
	private void loadPuzzles(String path)
	{
		String filename = path.substring(0, path.lastIndexOf("/") + 1) + "puzzles.txt";
		Vector puzzles = new Vector();
		Vector patterns = new Vector();
        String s = new String();
        try
        {
            URL url = new URL(filename);
		    BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
            while (true)
            {
                s = br.readLine();
                if  (s == null)
                {
                    break;
                }
                puzzles.addElement(s);
                s = br.readLine();
                patterns.addElement(s);
            }
            br.close();
		}	
		catch   (MalformedURLException me)
		{
            System.out.println("Malformed URL = " + me);
		}
		catch   (Exception e)
		{
            System.out.println("Exception on puzzles = " + e);
		}
		puzzleStrings = new String[puzzles.size()];
		patternStrings = new String[patterns.size()];
		for (int i = 0; i < patterns.size(); i++)
		{
			puzzleStrings[i] = (String) puzzles.elementAt(i);
			patternStrings[i] = (String) patterns.elementAt(i);
		}
	}
	private void makeEntities()
	{
		openSquares = GRIDSIZE * GRIDSIZE;
	    columns = new Entity[GRIDSIZE];
	    rows = new Entity[GRIDSIZE];
	    boxes = new Entity[GRIDSIZE];
	    grid = new NumberButton[GRIDSIZE * GRIDSIZE];
		for (int i = 0; i < GRIDSIZE; i++)
		{
			rows[i] = new Entity();
			columns[i] = new Entity();
			boxes[i] = new Entity();
		}
	}
	public int[] highlight(int value)
	{
		int[] temp = new int[GRIDSIZE * GRIDSIZE];
		int counter = 0;
		int found = 0;
		int hp = 0;
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			if (grid[i].getValue() == value + 1)
			{
				temp[counter++] = i;
				grid[i].setHighlighted(true);
				found += 1;
				hp = (playMode > EASIER) ? hp + 5 : hp + 2; 
			}
			else if (playMode > EASIER && grid[i].getStatus() == NumberButton.UNUSED)
			{
				// set it to value
				grid[i].setValue(value + 1);
				if (!grid[i].isValid(this))
				{
					grid[i].setHighlighted(true);
					temp[counter++] = i;
					hp += 1;
//					ToMarSudoku.log("Possible: " + i);
				}
				grid[i].setValue(0);
			}
		}
		applet.setMessage("Found " + found + " tiles.");
		int[] returnArray = new int[counter];
		for (int i = 0; i < counter; i++)
		{
			returnArray[i] = temp[i];
		}
//		ToMarSudoku.log("****************Size: " + counter);
		return returnArray;
	}
	public int[] clearHighlight(int[] list)
	{
		for (int i = 0; i < list.length; i++)
		{
			grid[list[i]].setHighlighted(false);
		}
		return null;
	}
	private void fix(int sq)
	{
		if (grid[sq].getStatus() == NumberButton.SET)
		{
			grid[sq].setStatus(NumberButton.FIXED);
		}
	}
	private void erase(int sq)
	{
		if (grid[sq].getStatus() == NumberButton.SET)
		{
			grid[sq].setStatus(NumberButton.UNUSED);
			grid[sq].setValue(0);
			openSquares += 1;
		}
	}
	public void eraseWrong()
	{
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			if (grid[i].getStatus() < NumberButton.FIXED)
			{
				if (grid[i].getValue() == grid[i].getSolution() || playMode == TEST)
				{
					fix(i);
				}
				else 
				{
					erase(i);
				}
			}
		}	
	}
	public boolean flipValue(int sq)
	{
		getGrid()[sq].nextValue(this);
		int counter = 0;
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			if (grid[i].getValue() == grid[i].getSolution())
			{
				counter += 1;
			}
		}
		if (counter == GRIDSIZE * GRIDSIZE)
		{
			return true;
		}
		if (openSquares > 0)
		{
			return false;
		}
		else
		{	
			for (int i = 0; i < GRIDSIZE; i++)
			{
				if (!rows[i].isValid(this) || !boxes[i].isValid(this) || !columns[i].isValid(this))
				{
					return false;
				}	
			}
		}	
		return true;
	}
	public void showSolution()
	{
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			grid[i].setValue(grid[i].getSolution());
		}
	}
	public void clearSet()
	{
		for (int i = 0; i < GRIDSIZE * GRIDSIZE; i++)
		{
			if (grid[i].getStatus() == NumberButton.SET)
			{	
				grid[i].setValue(0);
				grid[i].setStatus(NumberButton.UNUSED);
				openSquares += 1;
			}
		}	
	}
	public Entity[] getBoxes() 
	{
		return boxes;
	}

	public void setBoxes(Entity[] boxes) 
	{
		this.boxes = boxes;
	}

	public Entity[] getColumns() 
	{
		return columns;
	}

	public void setColumns(Entity[] columns) 
	{
		this.columns = columns;
	}

	public NumberButton[] getGrid() 
	{
		return grid;
	}

	public void setGrid(NumberButton[] grid) 
	{
		this.grid = grid;
	}

	public Entity[] getRows() 
	{
		return rows;
	}

	public void setRows(Entity[] rows) 
	{
		this.rows = rows;
	}
	public void draw(Graphics og)
	{
		for (int i = 0; i < grid.length; i++)
		{
			grid[i].draw(og);
		}
	}
	public int getPlayMode()
	{
		return playMode;
	}
	public void setPlayMode(int playMode)
	{
		this.playMode = playMode;
	}
	public int getOpenSquares()
	{
		return openSquares;
	}
	public void setOpenSquares(int openSquares)
	{
		this.openSquares = openSquares;
	}
}