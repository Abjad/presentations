# Outline

## A canonical description of Abjad formatting

Traverse and collect.

As we collect, there are rules determining what is collected.

From where do the rules derive? Western Notation and LilyPond.

Code generation and domain-specific knowledge govern the collection system at traversal-time.

- Input is a score tree - an Abjad data structure.
- Output is a string in a subset of LilyPond syntax.
- Formatting involves mapping the input into the output.
- We perform a depth-first traversal of the score tree.
- At each node in the tree, collect its contributions into a bundle.
- Contributions are strings, or string-generators.
- Contributions are determined by node specific logic.
- Contributions are also determined by node attachments.
- The bundle contains semantic and location information about the strings.
- As we exit each node during traversal, construct a single string from the bundle.
- Return that constructed string to the node's parent.
- Continue until all nodes have been visited.
- A single string results.

## Items of note

- The process is a kind of object-oriented delegation.
- Very similar to the visitor pattern.
  - Analyze this pattern.
  - Abjad's datastructures are based on a normalized tree.
  - But with some nodes - spanners - able to span, group nodes.
  - This introduces cyclicity via bi-directional references.
  - Non-spanner attachments hold no references: flyweights.
- `LilyPondFormatManager` visits each node in the formatted subtree.
- The format bundle is encapsulated in a class.

## Discrepancies
