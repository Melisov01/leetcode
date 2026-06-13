build map of brackets, add opening brackets to stack, if the next character is not an opening bracket we do the following:

1. check if stack is not empty, if it's empty it means it didn't have opening bracket and we return false
2. pop the last opening bracket
3. compare the value of the map with closed bracket, if doesn't match return False


at the end if stack is empty then everything is fine