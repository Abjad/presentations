# Outline

## A canonical description of Abjad formatting

Input is a score tree - an Abjad data structure.
Output is a text file in a subset of LilyPond syntax.
Formatting involves mapping the input into the output.

- We perform a depth-first traversal of the score tree
- At each node in the tree, collect its contributions into a bundle
- Contributions are strings, or string-generators
- Contributions are determined by node specific logic
- Contributions are also determined by node attachments
- The bundle contains semantic and location information about the strings
- As we exit each node during traversal, construct a single string from the bundle
- Return that constructed string to the node's parent
- Continue until all nodes have been visited
- A single string results
