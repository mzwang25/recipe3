# This script reads from stdin a pr (price) file and creates BaseIngredient
# typed objects for each.
#
# Example 
#   cat Vegtables.pr | python parsePr.py > Vegtables.py
# 

import sys

def createObject( buffer ):
  ingredientName = buffer[0]
  ingStr = ""
  code = "class {} ( BaseIngredient ):\n" + \
         "  def __init__( self, amountNeeded, units ):\n" + \
         "    super().__init__( amountNeeded, units," + \
         " {}\n" + \
         "  )"

  for i in range( 1, len( buffer ) ):
    sep = buffer[i].split()
    ingStr += "      \"{}\" : ( {}, \"{}\" ),\n".format( 
      sep[ 0 ], 
      sep[ 1 ], 
      sep[ 2 ] )

  print(code.format( ingredientName, "{\n" + ingStr + "    }" ) )
    

if __name__ == "__main__":
  print( "from BaseIngredient import BaseIngredient\n" )
  buffer = []
  rawLines = sys.stdin.readlines()

  for line in rawLines:
    if line[0] != "=":
      buffer.append( line.strip() )

    else:
      createObject( buffer )
      buffer = []

