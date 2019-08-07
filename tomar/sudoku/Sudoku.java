/*
	Sudoku
 */

import java.applet.*;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.*;
import java.net.*;
import java.util.Date;

public class SUD extends Applet 
				implements MouseListener
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public static int WIDTH;
	public static int HEIGHT;
	private int puzzleIndex;
	public static final int COLUMNMARGIN = 5;
	public static final int ROWMARGIN = 5;
	public static final int TOPMARGIN = 10;
	private static final int NOTSTARTED = 0;
	private static final int GAMEINPROGRESS = 1;
	private static final int GAMEOVER = 2;
	public static final int SIZE = 50;
	public static final int LEFTMARGIN = 10;
	public static final int RIGHTMARGIN = 540;
	int gameStage;
	private Image offscreenImg;
	private Graphics og;
	private SudokuPuzzle game;
	ToMarButton giveUpButton;
	ToMarButton clearButton;
	HighlightButton[] highlightButtons;
	String message = "";
	int[] highlightedList;
	String[] playModes =  {"Hardcore (***)", "Relaxed (**)", "Easy (*)", "TEST"};
	int award = 0;

	public void init()
	{
	    gameStage = NOTSTARTED;
	    clearButton = new ToMarButton(RIGHTMARGIN, 225, 90, "Clear");
	    giveUpButton = new ToMarButton(RIGHTMARGIN, 300, 90, "Easier");
		WIDTH = Integer.parseInt(getParameter("WIDTH"));
	    HEIGHT = Integer.parseInt(getParameter("HEIGHT"));
	    setSize(WIDTH,HEIGHT);
	    this.setBackground(tmColors.CREAM);
	    this.addMouseListener(this);
	    offscreenImg = createImage(WIDTH, HEIGHT);
	    og = offscreenImg.getGraphics();
		//Come in one of three ways:
		//   PUZZLE = TEST -- read input file, play in TEST mode, generate code when puzzle is solved
		//   PUZZLE = #### -- bypass randomizer, and bring up that puzzle number
		//   PUZZLE = anything else, bring up a random puzzle
		try
	    {
		   	puzzleIndex = Integer.parseInt(getParameter("PUZZLE"));
	    }
	    catch (Exception e)
	    {
	    	puzzleIndex = 9999;
	    }
		message = this.getParameter("message");
		message = (message == null) ? "Welcome to Sudoku!" : message;
	    reInit();
	}

	public void reInit()
	{
		if ("TEST".equalsIgnoreCase(getParameter("PUZZLE")))
		{
			game = new SudokuPuzzle(this, true);
	   		giveUpButton.setLabel("Code");
		}
		else
		{
			game = new SudokuPuzzle(this, false);
		}
		clearButton.setLabel("Clear");
		highlightButtons = new HighlightButton[SudokuPuzzle.GRIDSIZE];
		for (int i = 0; i < SudokuPuzzle.GRIDSIZE; i++)
		{
			highlightButtons[i] = new HighlightButton(game, i);
		}
		highlightedList = null;
		gameStage = GAMEINPROGRESS;
		repaint();
	}
	public void paint(Graphics g)
	{
		if (gameStage > NOTSTARTED) 
		{
			og.setColor(Color.red);
			og.fillRect(LEFTMARGIN - COLUMNMARGIN, TOPMARGIN - ROWMARGIN, (SIZE + COLUMNMARGIN) * SudokuPuzzle.GRIDSIZE + COLUMNMARGIN, (SIZE + ROWMARGIN) * SudokuPuzzle.GRIDSIZE + ROWMARGIN);
			og.setColor(new Color(125,125,125));
			og.fillRect(LEFTMARGIN, TOPMARGIN, (SIZE + COLUMNMARGIN) * (SudokuPuzzle.GRIDSIZE) - COLUMNMARGIN, (SIZE + ROWMARGIN) * (SudokuPuzzle.GRIDSIZE) - ROWMARGIN);
			og.setColor(Color.red);
			og.fillRect(LEFTMARGIN +(SIZE + COLUMNMARGIN) * 3 - COLUMNMARGIN, TOPMARGIN, COLUMNMARGIN, (SIZE + ROWMARGIN) * SudokuPuzzle.GRIDSIZE);
			og.fillRect(LEFTMARGIN +(SIZE + COLUMNMARGIN) * 6 - COLUMNMARGIN, TOPMARGIN, COLUMNMARGIN, (SIZE + ROWMARGIN) * SudokuPuzzle.GRIDSIZE);
			og.fillRect(LEFTMARGIN, TOPMARGIN + (ROWMARGIN + SIZE) * 3 - ROWMARGIN, (COLUMNMARGIN + SIZE) * SudokuPuzzle.GRIDSIZE, ROWMARGIN);
			og.fillRect(LEFTMARGIN, TOPMARGIN + (ROWMARGIN + SIZE) * 6 - ROWMARGIN, (COLUMNMARGIN + SIZE) * SudokuPuzzle.GRIDSIZE, ROWMARGIN);
			game.draw(og);
			if (gameStage == GAMEINPROGRESS)
			{	
				og.setColor(Color.black);
				og.setFont(new Font("Verdana",Font.PLAIN,20));
				if (game.getPlayMode() > SudokuPuzzle.NOHELP)
				{	
					og.drawString("Highlight", RIGHTMARGIN + 150, 30);
					for (int i = 0; i < SudokuPuzzle.GRIDSIZE; i++)
					{
						highlightButtons[i].draw(og);
					}
				}	
				giveUpButton.draw(og);
			}	
			clearButton.draw(og);
			og.setColor(Color.black);
			og.setFont(new Font("Verdana",Font.PLAIN,16));
			og.drawString("Puzzle: " + puzzleIndex, RIGHTMARGIN, 30);
			og.drawString("Open: " + game.getOpenSquares(), RIGHTMARGIN, 70);
			og.drawString(message, RIGHTMARGIN, 110);
			og.drawString(playModes[game.getPlayMode()], RIGHTMARGIN, 150);
		}
		g.drawImage(offscreenImg, 0, 0, this);
	}
	public void setUpEnding(boolean gaveUp)
	{
		if  (game.getPlayMode() == SudokuPuzzle.TEST)
		{	
			game.writeCode();
		}
		gameStage = GAMEOVER;
		message = "Game Over";
		clearButton.setLabel("Click");
		repaint();
		award = (gaveUp) ? 0 : 3 - game.getPlayMode();
		puzzleIndex = 9999;
	}
	public void update(Graphics g)
	{
		og.setColor(tmColors.CREAM);
		og.fillRect(0, 0, WIDTH, HEIGHT);
		paint(g);
	}
	public static void log(String s)
	{
		System.out.println(s);
	}
	public void mousePressed(MouseEvent e)
	{
		int x = e.getX();
		int y = e.getY();
		message = "";
		if (highlightedList != null)
		{
			highlightedList = game.clearHighlight(highlightedList);
		}
		if (clearButton.clicked(x, y))
		{
			if (gameStage == GAMEOVER)
			{	
				if (award > 0)
				{	
					try	
					{
						Thread.sleep(1000);
						String encName = (this.getParameter("nm")).replaceAll(" ", "%20");
						String fwd = this.getParameter("site") + "SUD?score=" + award + "&id=" + this.getParameter("id") + "&nm=" + encName + "&tsp=" + tmFormatting.getDateTimeStamp();
						this.getAppletContext().showDocument(new URL(fwd));
					}
					catch(Exception ex)
					{
						log("Error 2: " + ex);
					}
				}
				else
				{
					reInit();
				}
			}	
			else if (gameStage == NOTSTARTED)
			{
				reInit();
			}
			else if (game.getPlayMode() > SudokuPuzzle.NOHELP)
			{
				game.eraseWrong();
			}
			else 
			{
				game.clearSet();
			}
		}
		else if (giveUpButton.clicked(x, y))
		{
			if (gameStage == GAMEINPROGRESS)			// should always be true, but just in case
			{	
			// playMode			button label			action
			//   HARD				Easier				change playMode to EASIER
			//	 EASIER				Easier				change playMode to EASIEST, label to Give Up
			//	 EASIEST			Give Up				change button label to Confirm
			//						Confirm				show solution
				if (game.getPlayMode() == SudokuPuzzle.NOHELP)
				{
					clearButton.setLabel("Check");
					game.setPlayMode(SudokuPuzzle.EASIER);
					giveUpButton.setLabel("Easiest");
				}
				else if (game.getPlayMode() == SudokuPuzzle.EASIER)
				{
					game.setPlayMode(SudokuPuzzle.EASIEST);
					giveUpButton.setLabel("Give Up");
				}
				else if (game.getPlayMode() == SudokuPuzzle.EASIEST)
				{
					if ("Confirm".equals(giveUpButton.getLabel()))
					{	
						game.showSolution();
						setUpEnding(true);
					}	
					else 
					{
						giveUpButton.setLabel("Confirm");
					}
				}
			}	
		}
		else if (gameStage == GAMEINPROGRESS)
		{
			if ("Confirm".equalsIgnoreCase(giveUpButton.getLabel()))
			{
				giveUpButton.setLabel("Give Up");
			}
			else if (game.getPlayMode() > SudokuPuzzle.NOHELP)
			{	
				for (int i = 0; i < SudokuPuzzle.GRIDSIZE; i++)
				{
					if (highlightButtons[i].clicked(x, y))
					{
						highlightedList = highlightButtons[i].highlight();
					}
				}
			}	
			for (int i = 0; i < game.getGrid().length; i++)
			{
				if (game.getGrid()[i].clicked(x, y))
				{
					if (game.flipValue(i))
					{
						setUpEnding(false);
					}
					break;
				}
			}
		}
		repaint();
	}
	public void mouseClicked(MouseEvent arg0)
	{
	}
	public void mouseReleased(MouseEvent arg0)
	{
	}
	public void mouseEntered(MouseEvent arg0)
	{
	}
	public void mouseExited(MouseEvent arg0)
	{
	}
	public void setMessage(String message)
	{
		this.message = message;
	}
	public int getPuzzleIndex()
	{
		return puzzleIndex;
	}

	public void setPuzzleIndex(int puzzleIndex)
	{
		this.puzzleIndex = puzzleIndex;
	}
}
