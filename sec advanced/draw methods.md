Overriding Draw Methods
=======================

Previously, we considered a model of the event loop that included a
'draw' step. During this step in the event loop, any widget whose state
has been changed since the last cycle of the event-loop will redraw
itself. The reader may well wonder what this process actually looks
like.

Looking back on our widget gallery, the reader may well think of some
interesting widget that they have seen in use that has not been covered.
If the student can identify such a widget, it is likely that that widget
is not a commonly-used one: the student might, for example, consider a
widget that displays a graph of data. It is very unlikely that such a
specialized widget would be included in most kits; furthermore, there is
no obvious way to create such a widget by combining any of the common
widgets that we have discussed. Presumably, at least in some kits, there
is provision for building completely unique widgets by use of low-level
drawing facilities.

In this chapter, we will look at how widgets draw themselves, and
discuss providing out own Render methods to implement custom widgets.

A Word of Caution
-----------------

This is a non-trivial process. There is a significant amount of work
involved in implementing even simple drawing logic -- and an enormous
amount of work required to implement that logic 'correctly'. These
systems are far more detailed than those that we have been using before,
and will require us to manage and account for a great many details in
order to produce just the result that we want.

The Draw Method
===============

Object-oriented techniques are used throughout graphical programming,
and drawing logic is no exception. In many kits, there is a Paint method
included on the BasicWidget; when it is time to redraw a widget, the
system calls the Paint method on that widget. Paint methods are meant to
be overridden, and most widgets (other than those composed of other
widgets) perform their drawing by overriding the Paint method. When we
wish to implement our own completely novel widget, we can do so by
overriding the Paint method and providing our own rendering logic.

State Objects
-------------

The user with some understanding of graphics might imagine that we will
be given a grid of pixels by the system, and that they will
programatically set each pixel to some desirable value. While this would
work, it is not practical: if nothing else, it likely will require every
programmer to re-implement the same types of methods, like drawing lines
or placing images to the screen. Additionally, and more subtly, it makes
the assumption that the system can conveniently give us a grid of pixels
to work with; this assumption does not reasonably describe how modern
graphics cards function. Finally, it would effectively preclude many
modern graphical techniques; imagine if every GUI developer had to
re-implement SVG support on top of raw pixel buffers.

Instead, the vast majority of modern graphical kits will provide us with
classes to represent the state of a canvas, and classes or methods that
allow us to manipulate that canvas. When we implement a paint method, we
will be given (or get from the system) an instance of such a class, and
we will use the methods on it, perhaps with the help of support classes,
to draw geometric figures, fill them, display images or render text.

It is important to understand that, in some modern kits, even though we
appear to, for example, call a DrawCircle() function, and then have a
circle appear on the screen where our widget is, that the system does
not in fact actually render the circle into whatever graphics buffer
backs our window when the function was called. Many modern systems might
cache the drawing commands, for example, and issue them in a batch; they
might render our commands to a set of SVG instructions and cache those
instructions; or they might save the buffer that our instructions
produce, and update it only when strictly necessary.

Common Options
==============

Many modern kits will provide us with several basic graphical primitives
that the system supports. Many canvases will support rendering the
following:

-   Lines
-   Curves
-   Circles
-   Rectangles
-   Images
-   Text

Additionally, we can frequently set the 'border' of the figure being
drawn, and we will be given the ability to specify a 'fill' that colors
the interior.

Drawing
=======

In practice, we will typically have some idea about the size of the
patch of screen that the system has allocated to our widget
specifically; we will refer to this as its 'allocation'. If we know the
width and height of our allocation in pixels, we will then position
several of the above primitives to create the layout that we want.

(Canvases will typically use a 2D Cartesian coordinate system, with each
unit corresponding to a pixel on screen. A common - but by no means
universal - choice for the origin (the \[0, 0\] pixel) is the top left.)

Layouts
=======

The alert reader may notice that we have assumed that the system has
determined our allocation and given it to us before we actually start to
render the widget. This suggests that there should be some machinery in
place to determine the size of our widget, and that that machinery
should operate without having to actually render our widget.

This is in fact typically the case. In addition to the Paint function,
many kits also include 'sizing' functions - functions that return for
example the minimum, maximum or preferred size of a widget, given its
current configuration. We have not had to interact with these functions
before, as they are usually used by the layout manager to lay out
components without us having to do anything.

However, if we are providing a custom graphical display, we will
frequently also have to provide (accurate) implementations of the
appropriate layout functions, so that the layout-manager will be able to
size and place our widget.

Property Dependency
===================

We have mentioned that the 'size' that we compute might be dependent on
the 'properties' that are set on our window. If we are implementing a
text control, the size of the text might change if, for example, the
font is changed; if we are implementing a page-selection widget, the
size will change if the number of pages is changed; and so on.
Generally, most users will want to be able to configure the properties
of our widgets at run-time; more significantly, many kits (and
particularly many designers) might 'require' our widgets to be run-time
reconfigurable. Typically in object-oriented programming, we will not
expose properties as primitive variable; we will rather have defined
'getters and setters' for our properties.

In the setter for a layout-affecting property, we will 'invalidate' or
'damage' our display. Then, the system will re-compute the layout of any
widget that contains our custom widget (and we should return a new
sizing computed from the changed properties). Then, we will be given
some specific allocation (possibly different from our sizing request)
and we will render ourselves.

Events
======

When drawing our own widgets, we will typically have to create our own
events to accompany them. We will not have the benefit of using existing
widgets as components, and therefore we will not be able to receive
high-level, abstract events (like Clicked or EnterPressed). Here, too,
we turn to machinery provided to us by the BasicWidget class: it will
frequently include "low level" events - like key-pressed, mouse-down or
mouse-up. We will attach to these primitive events, and generate the
high-level events that we define as appropriate.

Here again, recall that, in order to re-render your widget so that
changes can be displayed, you will have to mark the widget as 'damaged';
you should not actually re-draw the widget during the event handler.
This implies that you will need to add the machinery to your class to
track the 'state' of your widget.

For example, suppose we have a widget that displays several icons, and
we want to draw the one that the mouse is over differently. We would
connect to the MouseMoved event; when the mouse moves, we will get its
new coordinates, and see if they are within the area of one of our
icons. If it is, we will have to record the number of that icon in a
class variable - say "this.mouseOverIconNumber" - and mark the widget as
'damaged'. When the widget is redrawn, we will consult the
"mouseOverIcon" variable, and draw the indicated icon differently.

Printing
========

As a final note, many kits implement 'printing' as a special case of
widget drawing. At some point in the printing process, the system will
provide a window-like object representing a 'page' - as in, a physical
page of paper. The programmer will then use the same set of mechanisms,
rendering into a buffer. However, at some point the user might mark a
page as 'complete', at which point, rather than rendering to the screen,
the buffer that the user has built up will be printed to an actual page.
