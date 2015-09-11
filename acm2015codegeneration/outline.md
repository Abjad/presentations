# Outline

## Possible Titles
Generating LilyPond Code via Python to Create Music Notation Documents

##Abstract (not more than 500 words)
LilyPond is a modular, extensible, programmable music notation document compiler that converts text input into automatically formatted graphic output. The Abjad API for Formalized Score Control -- which extends the Python programming language with an open-source, object-oriented model of common-practice music notation that enables users to build music notation documents through the aggregation of elemental music notation objects -- generates well-formed LilyPond input syntax. Abjad traverses a tree-like document representation to collect formatting information from each encountered node. A hybrid set of rules derived from graph theory, western music notation, and the constraints of LilyPond's domain-specific language enables Abjad to organize this collected information into a LilyPond input string.

## Regarding LilyPond syntax



## A canonical description of Abjad formatting

Traverse and collect.

As we collect, there are rules determining what is collected.

From where do the rules derive? Western Notation and LilyPond.

Code generation and domain-specific knowledge govern the collection system at traversal-time.

Traversal is not informed by music notation, but the collection rules are and the resulting lexical ordering of format contributions is.

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

## Items of note / Desiderata

- The process is a kind of object-oriented delegation.
- Very similar to the visitor pattern.
  - Analyze this pattern.
  - Abjad's datastructures are based on a normalized tree.
  - But with some nodes - spanners - able to span, group nodes.
  - This introduces cyclicity via bi-directional references.
  - Non-spanner attachments hold no references: flyweights.
- `LilyPondFormatManager` visits each node in the formatted subtree.
- The format bundle is encapsulated in a class.

LilyPond code is designed to be human-readable.

Abjad's output is deterministic and performs no compaction or optimization.

Music notation prioritizes structure. The unique constraint of music notation requires that the structure of temporarally successive or simultaneous elements be maximally clear and preserves that structure and renders it manifest.

Perhaps Abjad formatting is a kind of serialization? We serialize according to sequence in time. This is not an event stream, like MIDI. This is motivated by nesting.

Abjad sets up a correspondence between the temporal events in music and graph theoretic tree structure.

The tree sets up the start and stop times of objects in the score.

The lexical positioning of format contributions allows the syntax to locate the arbitrary objects of Western notation relative to the start and stop times of nodes in the tree.

Secondary objects (spanners and attachments) located relative to manditorally-durated primary objects (leaves and containers).

## Discrepancies

Abjad uses a tree model, while LilyPond uses both a tree and an event-stream model.

Abjad formatted scores make use of a constrained subset of syntax.

Attachment vs stream events.

##paper conclusion: Design Challenges for Code Generation in Music Notation Applications
Hey! We can generalize stuff!
