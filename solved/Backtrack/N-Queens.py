class NQueens:    #Generates all valid solutions for n-queen puzzle
    def __init__(self,size):
        self.size=size         #size of board
        self.solutions=0         
        self.solve()           
    
    def solve(self):
        positions=[-1]*self.size
        self.put_queen(positions,0)     #this functions solve problem and print number of solutions found
        print('Found',self.solutions,"solutions")
        
    def put_queen(self,positions,target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row==self.size:
            self.show_full_board(positions)
            self.solutions+=1
        else:
            # For all N columns positions try to place a queen
            for col in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions,target_row,col):
                    positions[target_row]=col
                    self.put_queen(positions,target_row+1)
                    
    def check_place(self,positions,occupied_rows,column):
        """
         Check if a given position is under attack from any of
         the previously placed queens (check column and diagonal positions)
        """
        for i in range(occupied_rows):
            if positions[i]==column or positions[i]-i==column-occupied_rows or positions[i]+i==column+occupied_rows:
                return False
        return True
    
    def show_full_board(self,positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row]==column:
                    line+="Q"
                else:
                    line+="."
            print(line)
        print()
        
                    
n=int(input())
obj = NQueens(n)
         
         
    