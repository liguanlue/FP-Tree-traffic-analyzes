# FP-Tree-traffic-analyzes
## Frequent pattern mining analyzes taxi traffic

### Algorithm steps: 
 1. Process the original data
 
	a. Delete the invalid data 
 
	b. Extract the taxi position of each time period to form the transaction item set
  
 2. Using FP-Tree algorithm for frequent pattern mining
  
	a. Build FP-Tree
	
		* Traverse the data set for the first time, get the frequency of each item, remove the items that do not meet the minimum support, and generate a head pointer table
  		* Sort the elements of each transaction in the data set, and remove the items that do not meet the minimum support
  
   		* Traverse the data set, for each transaction, if FP-Tree does not have the path, add the path, and if there is, add the count to the Item
  
   	b. Mining frequent itemsets from FP-Tree
  
   		* For each Item in the head pointer table, extract the condition mode base, that is, the path set ending with item
		
   		* Construction condition FP-Tree
		
   		* Find frequent itemsets recursively, knowing that the condition FP-Tree has only one item set
  
#### result:

1. The result of frequent pattern mining, such as result.txt, shows the locations of taxis that appear more frequently in the same period of time

Heat map showing frequent patterns:

![image](https://github.com/liguanlue/FP-Tree-traffic-analyzes/blob/main/IMG/frequent%20pattern.png)

2. The result of association rule mining, such as result.txt, shows the relevance of the position of the taxi at the same time.
 
