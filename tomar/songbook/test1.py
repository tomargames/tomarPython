#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import sys
try:
	import gUtils
except:
	sys.path.append("..")
	import gUtils
import Songs

print("Content-type: text/html \n")
print('''
<script>
// Get the modal, the close element, and the nDisplay element
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
var nDisplay = document.getElementById('nDisplay');
// When the user clicks on <span> (x), close the modal
span.onclick = function()
{
	modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event)
{
	if (event.target == modal)
	{
		modal.style.display = "none";
	}
}
// When the user clicks the button, open the modal
function showNote(x)
{
	nDisplay.innerHTML = noteDisplays[x];
	modal.style.display = "block";
}
function fetch(x)
{
	gForm.oper.value = x;
	gForm.submit();
}
function newSearch()
{
	gForm.oper.value = '';
	gForm.submit();
}
function sortTable(col)
{
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("detailTable");
  switching = true;
  /*Make a loop that will continue until no switching has been done:*/
  while (switching)
  {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++)
	{
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[col];
      y = rows[i + 1].getElementsByTagName("TD")[col];
      //check if the two rows should switch place:
      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
        //if so, mark as a switch and break the loop:
        shouldSwitch= true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}
function toggleDiv(id)
{
	var div = document.getElementById(id);
	if(div.style.display != 'none')
	{
		div.style.display = 'none';
	}
	else
	{
		div.style.display = 'block'
	}
}
</script>
''')
songbook = Songs.Songs()
results = songbook.displaySongList(songbook.getSongsByTag('ABeatles'), 3)
print(results[1])
print(results[0])
# print(songbook.getSongsByTag('ALauraNyro'))
# print(songbook.displaySongList(songbook.getSongsByTag('Min3'), 3))
# print(songbook.displayTagsByType('K'))
#print(songbook.displayTagsByType('A'))
