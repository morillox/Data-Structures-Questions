Active Directory Explanation

In this problem, we are going to search if the user is present in a group and
return either True or False. If a group contains a subgroup, then it will use recursion 
to search for the user again.

I used recursion because is the best way since we are facing the same piece of problem 
each time a group have a subgroup. 

Time complexity for this will be O(n!) and space complexity O(n). 