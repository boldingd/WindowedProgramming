The Model-Viewer-Controller Pattern
===================================

The Model-Viewer-Controller pattern is a major design pattern in GUI
design. Fundamentally, it is about separating the process of *displaying
information* from the process of controlling the *state* of the
application and from the *work* that the application actually does. It
is so useful (and thus valuable to know) because it makes it very easy
to make changes to *one* of those areas without having to make changes
in the other two; this allows us, for example, to completely rebuild the
graphical parts of our GUI, while keeping the same *state* and
*business* logic.

Design Patterns
---------------

The Model-Viewer-Controller pattern is itself a *design pattern*; since
many students will never have encountered design patterns before, it is
worth taking a moment to discuss what they are.

In software engineering, there are some problems that you will see again
and again. You might have some complex system, say a sound transcoder,
and you want to provide a functional "default" system, but allow users
to over-ride parts of it with their own code. Or, you might have some
class that uses some expensive global resource, and you want to make
sure that only one instance of that class can exist at a time. Design
patterns are essentially abstract, template solutions for these common
problems; the idea behind them is that, since these problems are common,
other engineers have already worked out good strategies for solving
them.

It is important to understand that design patterns are simply abstract
strategies. As such, their implementations will look very different in
different languages and different applications. It is also important to
understand that they are *only* strategies; they give us certain insight
on how a problem is usually solved, which we can reuse or not.

Separating Concerns in Complex Widgets
--------------------------------------

So, what common problem does the Model-Viewer-Controller (or MVC)
pattern solve?

Consider the following example: imagine that you are working at a
scientific-computing firm, and that you have some "expensive" task that
is currently implemented as a FORTRAN command-line program. Suppose that
this FORTRAN program has a lot of external switches that you provide on
the command line, but most of them usually get one of a few common
values. Someone might reasonably want to write a GUI to automate setting
up and running this program.

Consider that this GUI will have several *states*. There will be a state
where the GUI is being *configured*, there will be a separate state for
when the FORTRAN program is *running*, and there will be a third state
for when the program has finished. The probably should also be states
for displaying an error if the FORTRAN program crashed, and displaying
the results that it generated, but for our purposes, these three states
are enough. The GUI that you are building also needs to have some
*understanding* of the options that the FORTRAN binary expects, and
ideally some idea of what *good* and *bad* configurations look like - if
some sets of options do not work together, we would rather tell the user
before the program starts, after all. Finally, your program will have to
arrange to actually start the FORTRAN job and monitor it's progress,
presumably using facilities that the underlying OS or GUI library
provides.

While it might be complex enough to manage all these moving parts, an
additional complexity is introduce if any of these things *change*.
Consider the case where the scientists that maintain this program make
frequent changes. Imagine that the FORTRAN binary has many, many
options, only the most common of which you have captured in your GUI.
What if the work that the team uses the FORTRAN program for changes,
such that a switch that they previously did not use much suddenly
becomes very important? What if they add entirely new command line
options, or remove some that had previously existed? What if they the
initial GUI you give them difficult to use, and request changes? (In
real software projects, clients will *very frequently* request changes.)

If you have implemented your GUI as one *tightly-coupled* entity, with
the code that manages all these separate tasks shoved together into one
giant class, you might find these changes very difficult to make.

This is exactly where the Model-Viewer-Controller pattern steps in.

The Model-Viewer-Controller Pattern Itself
==========================================

Problems like the example are common; you will frequently encounter
situations where there is some kind of entity that your GUI represents,
and you will have to accomplish three fundamentally separate tasks
regarding that entity:

-   displaying its state to the user,
-   controlling and monitoring its state, and
-   translating between the behaviors of that entity and the states of
    your display.

The Model-Viewer-Controller pattern is about separating these three
concerns.

The MVC pattern suggests that we split our large GUIs into several
smaller components, each focused on a single one of these sub-tasks:

-   the **View**, which displays information to the user. It "knows"
    nothing about where this information comes from. Likewise, if it is
    *multi-state*, it know nothing about when state transitions occur -
    only how to represent the different states.
-   The **Model**, which represents (and *abstracts*) the task that the
    GUI is managing - which we frequently refer to as the *business
    logic* for the GUI. While the model might generate events (like
    status reports), it knows nothing about where those events go, if
    they go anywhere.
-   The **Controller**, which mediates the interaction between the View
    and the Model. The Controller knows how to translate user
    interaction with the View into operations on the Model, and it knows
    how to map feedback from the Model into updates and state-changes in
    the GUI.

It's worth noting that the barriers between these components are
somewhat "fuzzy"; this is an interface design problem, and interface
design is more an art form then a science. Experience, intuition and the
details of the specific problem will often determine whether a specific
function belongs in the View or the Controller, or the Controller or the
Model. These choices may change as the project evolves.

It is also worth remembering that design patterns are "more suggestions
than rules"; this is also true of the MVC pattern. A particularly common
reduction occurs when the Controller or Model are very simple; in this
case, they are often folded into a single entity. The result is
something of a "Model/Viewer" breakdown, where one class knows how to
"do work" and the other knows how to "talk to the user."

An Example
==========

It is a little difficult to follow from an abstract description of the
MVC pattern to it's realization in any particular situation. To get
something of a feel for how this pattern works (and why it might be
useful), let us return to our motivating example.
