## Decision Tree

Structure
> A decision tree is a hierarchy of if/else questions leading to a decision built by learning from data  

> Inner node: feature  
> Edge : condtion of a feature value  
> Leaf node: prediction  

Strength
> extracted knowledge can be easily understood, interpreted, controlled by humans in the form of a readable decision tree

- Finitely many different decision trees can exist. But too many possible tree can exist
    - Optimal algorithm generates all possible trees and choose the best one.
    - Heuristic algorithms with greedy strategy  
### Procedure
1. Repeatedly split a node into two parts so as to minimize the impurity of outcome within the new pars

### How to determine the best split?

    - Classification
<img width="50%" alt="image" src="https://github.com/user-attachments/assets/a8de12b5-0fbb-4715-9889-62c87a79e998"> <img width="432" alt="image" src="https://github.com/user-attachments/assets/247aa143-57bd-479f-84bd-d2cab33fb14b">

### Problem below
<img width="728" alt="image" src="https://github.com/user-attachments/assets/7cb0997b-dc6b-4a65-99ad-4432ebb3b7bd">

- Very complex, overfitted
- So we can use greedy strategy, and use majority class for Classification, mean target for Regression.  

Solution
    - Pre-pruning:
    - Post-pruning: