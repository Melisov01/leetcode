count character frequencies, have fixed window size, if length and frequencies match return True, if we need to keep going then we delete element from the left, add +1 to the left and expand the window to the right. 

If nothing was found after the loop return False