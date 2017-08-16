Design Patterns
===============

For many readers, the techniques that we use in GUI programming might
seem odd. Frequently, the reader may have used objects mainly to model
the entities and structures in their code fairly directly; if we have a
program that uses points, we will have a 'point' class, and its methods
will be the operations that we can perform on 'points'. In contrast, in
GUI programming, we will frequently use language features to achieve
organizational and structural ends; we will build classes that are
designed to be composed into trees, or designed to contain instances of
other classes, or perform other purely 'structural' ends.

Many of these structural techniques are in fact not unique to GUI
programming; they are in fact common techniques. There are some
organizational problems that are common; they recur frequently in
different programs. For some of these common problems, software
engineers have developed schematic common solutions; we call these
'design patterns'.

Many of the organizational techniques that we use in GUI programming are
in fact instances of general design patterns; it may be to the reader's
general benefit to discuss these patterns in a general context.

Students should consult the Wikipedia article on [Software Design
Patterns](wikipedia:Software_design_pattern "wikilink"). Perhaps the
seminal text on the subject of design patterns is the book *[Design
Patterns](wikipedia:Design_Patterns "wikilink")*.

The Compositor
--------------

We use the [Compositor](wikipedia:Composite_pattern "wikilink") design
pattern in the design of the `BasicWidget` class.

The Decorator
-------------

We use the [Decorator](wikipedia:Decorator_pattern "wikilink") pattern
extensively in GUI toolkits; many container widgets are Decorators.

The Observer
------------

Most toolkits use some variant of the
[Observer](wikipedia:Observer_pattern "wikilink") pattern to implement
their event systems.
