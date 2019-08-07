#!/Users/tomar/Anaconda3/python.exe
"""
Created on Monday, April 16, 2018 by marie
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
"""
import Sudoku
print("Content-type: text/html \n")
print('''
<html><head><title>Sudoku</title>
<script src="/python/utils.js"></script>
<LINK REL='StyleSheet' HREF='/python/tomar.css?'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<body>
<div id="app" align="center">
	<canvas id="dbCanvas" width="1100" height="650">
		Your browser does not support the canvas element.
	</canvas>
		''')
sud = Sudoku.Sudoku()
print(sud.setUpScript(authT))
print('''
	</tbody></table>
  </form></dialog>
	<script src="/python/sudoku.js"></script>
</div>				''')
print('''
</body>
</html>
		''')
