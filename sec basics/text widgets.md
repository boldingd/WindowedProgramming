Useful Controls: Text Widgets
=============================

We have just covered the common 'selection widgets' - widgets that allow
users to make a selection from among a fixed number of options that we
have provided. The 'text widgets' - which will be the subject of this
chapter - are more free-form; they allow the user to enter potentially
arbitrary strings of text.

Text widgets have two major uses. Perhaps most simply, we may use them
as 'displays' - as our program runs, we will update the text in a text
widget with progress messages from our program. This allows us a basic
form of dynamic communication with the user; it is rarely the preferred
approach for communicating with the user, but is very useful as a cheap,
stopgap output system during application development. The other use for
text widgets is to allow the user to enter text, from file names to
messages.

Some systems provide very sophisticated text-formatting facilities;
these are beyond the scope of discussion for this document. Still,
readers should be aware that their platform's text-entry widgets might
be 'very' sophisticated, and should check their platform's documentation
for more information.

The TextLine Widget
-------------------

There are two major text entry widgets; the multi-line entry and the
single-line entry. We will first concern ourselves with the single-line
text entry. Usually, the single-line entry will be very simple; it's
primary purpose is to allow the user to entry a single value, such as a
URL, a file path or a parameter string. (As such, they are commonly
coupled with some kind of file-chooser dialog; we will discus dialogs,
including the file-chooser dialog, later.)

Because the TextLine widget only allows the user to enter a single line
of text, it affords us the opportunity to treat it as a special event if
the user presses the "return" key. Unfortunately, toolkits very
significantly as to how they achieve this; some kits' TextEntries will
offer us an `enter_pressed` event, while others will trigger the form's
'default action' automatically, without ever raising an event that we
handle in our code.

Of note is that the TextLine is the first widget that we have seen that
can grow. The previous Button widgets had fixed preferred sizes, that
were functions of their contents (for example, that were determined from
their text labels in the case of a simple button). TestLines, on the
other hand, can potentially grow and shrink, at least horizontally.

The TextBox Widget
------------------

The TextBox allows the user to enter multiple rows of text. The
TextBoxes provided by most kits are very sophisticated; their full
capabilites are arguably beyond the scope of this text. For our
purposes, we will ignore most of the events that they might offer us,
and focus mainly on their `text` property, which will allow us to
retrieve the text in them (if the user is entering text) or add to the
text in them (if we are using the TextBox as a display).

The TextBox is the first widget that we have seen that can grow both
horizontally 'and vertically'; it is also the first widget that we have
seen that is 'scrollable'. All of the previous controls have some
minimum size that is a function of their contents; a Button, for
example, must be given at least enough space on the screen to display
its label. We can easily imagine a scenario where we enter more text in
a TextBox than can be displayed on screen. Rather than require the text
box to resize, the TextBox (in most kits) can display 'scroll bars' when
its contents grow too large to display in the area available to it in
the layout. (In most kits, this capability is enabled by default, and
will be triggered automatically without our intervention.)

Frequently, we can select whether the text box should 'always' display
scroll bars, 'never' display scroll bars, or display them
'automatically' when the text in the TextBox becomes too large to fit
on-screen. This last setting is 'usually' the "right answer," and so is
usually the default.

Marking Text Boxes as Editable
------------------------------

TextBoxes have one other property of particular interest, whether or not
they are 'editable'. The `editable` property will determine whether or
not the user is able to type text in the `TextBox` If we are using the
`TextBox` as a display, we should usually mark the text box as not
editable; this way, the user cannot, for example, accidentally delete
our log messages. In most kits, even if the `TextBox` is not editable,
it will still be possible for the user to select the text in the text
box; this is useful so that they can copy our log messages, for example.

Note that the 'editability' of a `TextBox` is a separate concern from
whether or not it is `Enabled`. If a `TextBox` is disabled, neither the
developer nor the programmer will be able to interact with it,
regardless of its editability setting. We will revisit the subject of
'disabling' widgets later.
