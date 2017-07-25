First Steps: Displays, Controls and Layouts
===========================================

Having looked at the basic concepts of event-driven programming, looked at a number of possible toolkits and considered how to start a "blank file" project, let us now turn to the building-blocks that we will use to construct graphical interfaces.

Widgets
=======

Let us consider some of the common basic widgets that we will be working with.

Typically, we will construct complex interfaces by combining simple building blocks, like buttons and labels.
Most GUI libraries will provide us with a selection of basic elements: we will call these components "widgets".
Loosely, a widget is any component of our application that can draw itself on the screen.

The BasicWidget
---------------

GUI toolkits will frequently include a basic Widget class: we will call this the `BasicWidget`.
`BasicWidget`s are the building blocks for their specific toolkits; they define the capabilities of a widget in that kit, and include most of the functionality necessary to create a other widgets (which will typically done by creating classes that extend the `BasicWidget`).

The other widgets present in the toolkit - buttons, images, text boxes and so on - will inherit from the `BasicWidget` class.
The benefits of doing this are twofold.
First, and perhaps most obvious, is that, by producing a generic widget class that other classes can inherit from, it is easy to create new widgets.
The second benefit, more subtle but perhaps also more significant, is that it provides us with a common interface that we may use throughout the toolkit.
The classes that comprise the toolkit need not know what kind of widget that they are working with; as long as they can work with `BasicWidgets`, they will be able to work a Button, a TextArea, or some other widget that we have created ourselves.

Widget Trees
------------

`BasicWidget`s frequently have the ability to contain other `BasicWidget`s. This allows us to put `BasicWidget`s into other `BasicWidget`s - or more usefully, other *classes that inherit from* `BasicWidget` into other classes that inherit from `BasicWidget`/

We can use this capability to create GUIs by creating composits of widgets containing widgets.
We refer to this arrangement as a *widget tree*.
If one widget *A* contains another widget *B*, we say that *A* is the parent of *B*, and that *B* is the child of *A*.

For example, in a given toolkit, besides the `BasicWidget` class, there might be a `Button` class and a `TextField` class.
We could create a simple GUI (that might be the start of a file downloader, for example) by creating a `BasicWidget` object, a `Button` object and a `TextField` object, and adding the `Button` and `TextField` objects to the `BasicWidget` object as children.

Notice that this composite object would still appear to be a single `BasicWidget` class to its parent.
We could create a class that automated this process - a class that inherited from `BasicWidget` and, in its constructor, creates a `Button` and `TextField` object and adds them to itself as children.
This suggests one of the major uses for `BasicWidget`s, and one of the major strategies for building GUIs: creating classes that inherit from a toolkits `BasicWidget` class and populate themselves with child widgets.

Types of Widgets
----------------

There are several general types of widgets; for now, let us specifically consider three: *Displays*, *Controls* and *Containers*.
A *Display* is a widget that displays some value to the user; the simplest example of this class is perhaps the Label widget, which simply places some fixed text somewhere in the GUI.
A *Control* is a class that receives input from the user; a Button is perhaps the simplest control, giving the user the ability to trigger some specified action.
A *Container* is a widget that is designed to contain other widgets as children; a Scroller is a simple container that adds scroll-bars to its child widget.
These categories are not mutually exclusive; a volume slider, for example, is both a display and a control.

Layouts
-------

Adding elements to a GUI is only the very start of building an interface. At the least, we would typically like to place these elements at specific locations on the screen, and to give them appropriate sizes (we likely would not want a text-entry field to be several times the size of a button next to it, for example). This might seem like a simple task; for any given GUI size, it would be. However, modern GUIs are typically designed to be *resized* - users will want to grab the edge of the windows that our graphical applications reside in and then scale them to whatever size they see fit. Creating a flexible, fault-resistant sizing algorithm that can accommodate any arbitrary window geometry would be an involved problem.

Fortunately, this tedious work has already been done for us. Most toolkits will provide us with some facility for creating *layouts*; layouts are software components that manage the size and position of our widgets for us. This allows us to create GUIs that the user can resize however they like, while requiring us to do little more than add the widgets that we would like, possibly specify a layout type and then configure that layout.

You might wonder if layouts are widgets. In some toolkits they are, and in some toolkits they are not. In GTK, for example, the ability to manage layouts is provided by the Box and Grid container widgets; the Box is a container that lays its children out in a row, while the Grid is a container that arranges its children in the cells of a grid (much like an HTML table). However, in most other kits, layouts are not widgets - they are not visually displayed, they are not elements of the widget tree, and they do not inherit from `BasicWidgets`. They are instead *properties* of widgets; for example, the `BasicWidget` class might have a `setLayout` function, and we might have our choice of layout classes to choose from.

Many kits will include more than one type of layout. For example, Java Swing includes the `GridBagLayout`, `FlowLayout` and `SpringLayout`, among others.

In general, the different widgets in a GUI should be sized differently. This might be because of the properties of the widgets themselves - for example, some might be able to stretch horizontally or vertically, while others cannot. Similarly, we might want some widgets to behave differently than others; if we have two widgets that can grow horizontally and vertically, we might want one element to maintain its minimum size, while the other widget receives all the excess space available in the layout.

Events
------

In addition to adding child widgets and setting a layout, we would also like to arrange for our GUIs to respond to user inputs. Each widget will be designed to respond to certain *events*; we will then attach *callback functions* to these events (callback functions are also sometimes called *event handlers*). When the specified event is detected, the callback that we set is triggered; in this case, we would say that the specific event has been triggered on the widget.

For example, Button widgets primarily respond to being *clicked*, and so they typically have a *click event*. If we have a button, when we specify a callback for it, we say that we have *attached* a callback to the *click event* of that button, or that we have *registered* that callback with the button. When the user clicks the button and our callback is triggered, we would say that the click event has been *triggered* or *raised*.

Callback mechanisms can very heavily from programming language to programming language, and from GUI toolkit from GUI toolkit; this makes it difficult for us to discuss them in depth now. Significantly, callbacks are likely to use facilities in many programming languages that the average undergraduate Computer Science student will not have seen before.

Properties
----------

Finally, many widgets also have *properties*. Properties, as the name implies, are aspects of given widgets that we can adjust to alter the behavior or display of an individual widget. (One might consider the events that a widget possesses to be special properties, and some 'kits do treat them this way.)  A check-box widget might have a *checked* property, which will tell us whether it is currently *checked* or *unchecked*.

Recall that any given widget will typically inherit from a `BasicWidget` base class; some might inherit from several intermediate classes along the way. A Button widget might inherit from a `Clickable` class, which might itself inherit from a `FixedSizeWidget` class. Each one of these classes might potentially include properties that their descendant classes might inherit. Because of this, some properties will be common to all widgets, while others will be specific to a certain widget class.

Some Basic Widgets
==================

We will now continue on to consider several of the common widgets, beginning with several basic displays and controls. When a new widget is introduced, we will discuss its use, its event and its properties.

The Label
---------

Perhaps the simplest display widget - and perhaps the simplest useful widget baring the BasicWidget - is the Label. Labels are simple widgets that display some given text wherever they are placed in the GUI; they are primarily useful for (as their name implies) labeling some other component of the interface, which they are placed near. The label has no interesting events and only a single interesting property, the text-string that it contains.

The Button
----------

Labels are not particularly interesting on their own; the user cannot interact with them (other than perhaps to select and copy their text), and in most cases we will not be modifying them after they are created and placed in our GUI. Of more interest is the Button; much as the Label is our simplest display widget, the Button is perhaps the simplest control widget. Like the Label, Buttons will generally have a single interesting property, the text string that they display; however, unlike Labels, Buttons provide us with an interesting event - the `on_click` event; when the user clicks the Button, the Button will emit the `on_click` event. More technically, the system will detect that the mouse button was depressed and released in the area on the screen that the Button occupies, and will call every event handler registered to the Button's `on_click` event; we usually do not concern ourselves with these details, and simply say that "the Button emits the `on_click` signal."

We will typically use Buttons to allow the user to request that we perform some action - obvious examples are the ubiquitous "OK" and "Cancel" buttons that can be found throughout most programs of any complexity, which allow the user to tell the program when they are ready to have the system perform some task or wish for the system to not perform some task. It is worth noting that we usually do not place the code that performs a given task in the callback that we will connect to a Button; rather, the actual callback in the Button will change some internal state in our interface and then arrange to have the task begun later, likely in another thread.

Layouts
=======

Having touched on two widgets of interest, a minimal control and a minimal display, the motivated reader will be tempted to begin building basic interfaces. However, we will need some other tools to build a usable interface. Simply placing widgets into an entity tree is not enough information for the system to build our interface; it will tell the system what controls are present, but it will not tell the system how those controls should be displayed - in particular, the system won't know *where* on screen to place the controls, or, if they can be different sizes, how *large* they should be. To provide this information, we turn to *layouts*.

The Layout-Relevant Properties of Widgets
-----------------------------------------

Widgets will typically provide 'minimum', 'maximum' and 'preferred' sizes; these sizes can depend on what the widget's intended purpose is, and what its current contents are. For example, a Button's minimum, maximum and preferred size might all be the same, and they might be determined entirely by the text content of the button (and perhaps the current 'style sheet' in use in the application); meanwhile, an empty BasicWidget might not have any maximum size, but its minimum and preferred sizes might be determined by the widgets it contains. These properties can vary both 'vertically' and 'horizontally' - a widget might have a specified maximum 'height' that it can occupy, but it might be capable of being any 'length'.

Widgets may also have different "willingness" to grow vertically or horizontally. For example, it might be the case that we have two widgets laid out in a row, and neither of them might specify a maximum length: in this case, how should we allocate the vertical space of the widget? While some toolkits might use some combination of the different sizes and some implicit rules, other toolkits provide us with 'weights'. Weights represent how much "slack space" should be given to the components in the case that a layout has more space available than all widget's minimum or preferred sizes. In some toolkits, weights are (implicit or explicit) properties of the 'widgets' while in others they are properties of the 'layouts'; the distinction is not terribly important, as they tend to perform the same role.

The Layout Cycle
----------------

When a given widget wishes to compute its layout, it might do so in several steps.

-   *Gather Properties*
    -   *Gather child properties*
    -   *Compute our properties*
-   *Compute Layout*
    -   *Compute child layouts*
    -   *Compute our layout*

Recall that any widget might contain several child widgets. For a given widget to know its own minimum and maximum sizes, it will need to know the minimum and maximum sizes of its children; those children may themselves have children whose sizes will need to be computed, and so on. Likewise, once a widget knows what the minimum and maximum sizes of its children are, it will compute its layout, determining the positioning and extents of its children. Once those children know their extents, they can compute their own internal layouts, and so on. In this way, the layout process is 'recursive'.

Types of Layouts
----------------

There are several common types of layouts.

### Row Layouts

Perhaps the simplest layout is the 'row' or 'column' layout, which lays its child widgets out in a single row or column. These layouts might give each child equal space, or they might size their children more flexibly. Row layouts are not particularly flexible; they (or widgets that use them) are frequently composed to create more sophisticated layouts. It is often ultimately more convenient to use a single 'table' layout.

### Grid Layouts

Grid layouts work like HTML tables; they lay their children out across the cells of a table. Cells (and rows and columns) can have different sizing properties, and widgets can span rows and columns; this allows us to create sophisticated and flexible layouts, but it also requires us to carefully set the parameters of each widget in each cell - and getting exactly the result that we want can require us to be somewhat clever in doing so.  Even worse, small changes to our layout can require quite a lot of rebuilding and re-tuning.

A major layout property in grid layouts is whether a cell can *expand* or *grow*, either vertically or horizontally. Some kits allow us to attach weights to cells, determining not just *whether* a cell can grow, but *how much* of any new space the layout receives will go to a given cell; while this is sometimes useful, we usually either want a cell to grow freely, or to not grow at all, and so we usually will set our weights to be either 0 or 1.

### Relative Layouts

Rather than lay our components out in geometric rows, columns or grids, relative layouts allow us to build layouts by *anchoring* control points on our widgets to control points on other widgets (or control points on the containing widget, like corners or edges). Working with relative layouts can be a very different process then working with row or table layouts: they use entirely different sets of properties to determine their layouts. For that, however, table layouts and relative layouts can achieve much the same results; the major advantage of relative layouts is *not* that they are more powerful or that they are easier to work with in a broad sense, but rather that they are easier to work with inside graphical GUI-builder tools specifically.

In a relative layout, some components will generally be anchored to one edge of the parent widget; however, it is possible for a component to be anchored entirely to other widgets. In relative layouts, if a widget is anchored on both its left and right edges (or top and bottom edges), this will essentially make it *grow* and *shrink* in that direction.

Very beneficially, relative layouts are very easy to *change*; they allow us to move individual components around without having to re-build substantial parts of the layout ourselves.

Examples
========

For concrete examples, see either [Getting Started in Python](getting started python) or [Getting Started with JavaFX](getting started jfx.md)
