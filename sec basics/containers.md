Container Widgets
=================

The container widgets are widgets designed to contain other widgets, and
add some useful capability to them.

(In many cases, they can be considered an example of the 'decorator'
design pattern; see Appendix 1.)

The Basic Widget and Layout Widgets
===================================

Some of the widgets that we have already discussed are or can be viewed
as container widgets. One of the major ways that we build layouts is by
placing child widgets inside a `BasicWidget`; in this scenario, the
`BasicWidget` is serving as a container widget. Similarly, in some kits,
'layouts' are widgets: we might have a `HorizontalBox` or `Grid` as a
widget, for example, and any children that we added to these widgets
would be laid out in a horizontal row, or on a grid. In this case, the
layout widgets are also 'container widgets'.

The Border Widget
=================

Beyond the above, the simplest container widget (offered by some kits)
is the 'border'. The 'border widget', like the `BasicWidget`, is
designed to have children added to it; it lays them out just like a
`BasicWidget`. The major difference is that the border widget will draw
a 'border' around its contents.

Many kits do not include border widgets; in many modern kits, the
`BasicWidget` will have sophisticated styling capabilities, which will
include the ability to draw a border around itself; this precludes the
need for an separate border widget.

The Group Box
=============

The 'group box' is an extension of the idea behind a border widget. The
group box is designed to contain child widgets, like a BasicWidget or
border widget; it frequently draws (or can draw) a border around its
children. It has the additional ability to draw a label above the group;
this allows you to group and label a set of controls.

The group box is the first of the container widgets to have a unique
event or property: its label. It will typically display its label near
the children it contains; it may also display a border.

The StackPanel
==============

The StackPanel is a container widget that is designed to handle a
dynamically changing set of children -- that is, it is designed to allow
the user to add widgets to it (and remove widgets from it) while the
program is running. The StackPanel will display its children in either a
row or a column, depending on how it is configured.

The Scroller
============

The major common container widget is the 'scroller'; if we have some
widget that has very strict sizing rules (such as an image or text
document), the scroller allows us to embed that widget in a GUI that
might not be able to satisfy that child's sizing requirements. The
scroller adds the ability to be 'scrolled' to a child widget; that is,
it adds scroll-bars to the lower- and right-edges of a child widget. The
scroller will report a very low minimum size to its parent widget; if
the parent widget allocates the scroller less than the minimum (or
preferred) size of the child widget, the scroller will shrink, will
enable the scroll bars, and will show only part of the child widget.

In many kits, the Scroller can only have a single child; this is not as
significant a restriction as it may seem, however, as a single
`BasicWidget` is a single widget from the perspective of the Scroller
that it is placed in, but it can contain multiple child widgets.

The TabBox
==========

The TabBox is designed to allow multiple widgets to use a single, finite
allocation of screen space. The TabBox can contain many child widgets,
but it will only display one of them, and it will give the one widget
that is displaying (almost) all of its screen space; the other child
widgets (the ones that are not selected) will not be displayed. There
will also be a page list presented across the top of the widget, which
will give the user the ability to select a child widget. The user views
the TabBox as containing 'pages', but each page is in fact a child
widget.

In most cases, the system will keep track of the current page, and will
switch the current shown page in response to a tab selection without our
having to do anything. The major bit of state data that we will need to
track is the list of pages, and the association between the 'pages'
(which are the widgets that we are adding) and their 'titles'.

The current page will typically be exposed as a property by the toolkit
- this might be by the page title or by the numeric page number,
depending on how the kit keeps track of pages. Likewise, many kits will
provide us with functions to switch the current page.

Most kits will provide us with events to track when the tab changes, but
in 'most' cases we will not need to interact with this machinery, as the
system will switch from page to page in response to the user clicking a
tab-selector without our having to do anything. The major exception to
this rule would be if we wanted to prevent the user from switching tabs
in certain circumstances - such as if each page represented a set of
configurations that needed to be proceeded through in order, and we
wished to prevent the user from prematurely jumping ahead.

The major event that we are likely to connect to - which is not provided
by all kits - is the `tab_close_requested` event. The process of
removing tabs from TabBoxes varies heavily from kit to kit, but some
kits merely generate a "close requested" event when the user tries to
close a tab; it is then up to us to explicitly remove the specific
requested page from the TabBox.

There will be two major work-flows for using tab-boxes. In the first
case, we will know what elements will be in the tab box before-hand;
this will be the case if, for example, we are using the TabBox to
contain a multi-page configuration widget. In this case, we will work
with the TabBox much like we have been working with the parent widgets
that we have used as canvases up to know: we will use our graphical
tools to add pages, set layouts on the pages and drag child widgets onto
the pages.

The more interesting case, however, is when we do not know the number or
configuration of the tabs before-hand: this is the case if, for example,
we were working on a document editor, and we were using the tabs to
contain open documents. In this case, most kits will have an `add_page`
function, which will (typically) take at least a widget (which is the
page to add) and a title for the page. This requires us to have
constructed a widget that will represent each page; this is perhaps our
first look at interacting with one widget that we have constructed from
within another widget that we have constructed.

PageStacks
----------

Some kits will also provide us with page stacks. A page stack is much
like the TabBox, in that it contains several children, but will only
display one at a time. However, it does not have the tab selector on
top; rather, its entire area is given over to displaying the active
child widget. The major use for these containers is if we want to
implement our own page selector, rather than using the tab bar provided
by the system.

The EventBox
============

Some kits include a widget that contains a single child, and add new
event capabilities to that child; this is the EventBox. EventBoxes can
be used to (in effect) add event-handling capabilities (like receiving
click events) to widgets that do not normally have them (like labels or
images).

EventBoxes will generally be included in kits whose event systems are
not sufficiently flexible to allow widgets to easily choose what events
they wish to generate or receive. Many kits will provide widgets with
several common events - such as mouse-enter, mouse-leave, mouse-down,
mouse-up and mouse-click; these kits can then choose to handle these
events or not. In kits with such flexible event systems, there will be
little need for an EventBox.

Animated Widgets
================

With the rise of accelerated graphics, a host of new widgets have
appeared, which take advantage of the improved rendering performance
available. Many of these widgets are containers; they frequently provide
animation or overlay properties to existing widgets, allowing us to, for
example, reveal and show widgets, or to overlay one widget on top of
another.

There is not yet a standard lexicon of such widgets, and so we will not
handle them extensively here.
