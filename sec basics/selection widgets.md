Useful Controls: Selection Widgets
==================================

We will now consider a family of useful controls, the 'selection widgets'. Many of these widgets inherit from the `Button` widget, and so will inherit also the `Button`'s properties and events.

A Selection Widget is a widget that allows a user to select from among several specific options. They are useful when you can determine the full range of the options that a user is likely to want to select - for example, if a user is only going to want to enable or disable something, or if they only have a small, fixed number of options that make sense.

In the next section, we will consider widgets that allow for more free-form selections.

The CheckBox Widget
-------------------

A simple extension to the `Button`, the CheckBox is a clickable control that has multiple states - at least a *checked* and *unchecked* state, and possibly more. It toggles between these states when clicked, and typically exposes its current state as a property. We use check boxes to allow users to make yes/no decisions in our interfaces.

CheckBoxes usually inherit from Buttons, and so usually have an `on_click` event that we can connect to; this signal will be emitted whenever the button has been clicked, regardless if the user checked or unchecked it. Frequently, CheckBoxes will also add `on_checked` or `on_unchecked` signals, which we can connect to if we only care about when a button is specifically checked or unchecked.

In most cases, we will not connect to the signals on a CheckBox directly. They will track whether they are checked or unchecked on their own, without us having to do anything, and this is usually all we want them for. Commonly, we will be interested in getting their state - whether they are checked or unchecked - when the form that contains the button is submitted. In this sense, the most interesting feature of the CheckBox is their `State` property, not their events.

the major exception to the above is if we wish to *enable* or *disable* some section of the form that contains the button, based on whether or not the button is toggled. In this case, we would likely connect to the `clicked` signal, and enable or disable the form section in question based on the `status` property of the CheckBox; we will return to *enabling* or *disabling* widgets later.

Some kits support *tri-state* check-boxes; these are check-boxes that have three states, checked, unchecked and partial. These are mainly used in *tree views*, to represent branches of three where some items are selected and some items are de-selected. We will revisit *tree views* later; their use can be very involved.

Enabling Widgets
----------------

In many toolkits, a widget can be either 'enabled' or 'disabled'. When a widget is 'enabled', it will draw itself, and it can generate and receive events; this is the normal state. When a widget is 'disabled', it will not generate or receive events; it also will not redraw itself. Disabled widgets are typically rendered differently, so that users will no that the specified component cannot be interacted with.

The RadioButton Widget
----------------------

An extension of the CheckBox, an individual RadioButton also has two states, checked and unchecked. Like the CheckBox, the RadioButton will toggle and un-toggle itself in response to user action on its own; because of this, we usually will not connect to the events on a radio button directly. The major difference between the CheckBox and RadioButton is that RadioButtons are designed to be used in groups, and that they will ensure that only one RadioButton in the group is selected at any given time.

RadioButtons are primarily useful when we can determine the number of options before-hand, and when the number of options are *small*. This is because each option takes up space in our layout; it is more difficult (though not impossible) to make a layout that can scale to handle arbitrary and possibly large numbers of radio buttons. If the number of options is large, or if we do not know how many options there will be before hand, we should use a ComboBox instead; the ComboBox is covered below.

In some kits, it will be possible for none of the buttons to be selected, and this might be the case when the program starts; other kits will ensure that one button is *always* selected, and therefore will have one default button selected when the application starts. In the former case, developers should be aware that it might be the case that no RadioButton is selected, and design their applications to detect and handle this case. In the latter case, developers should be aware that users may not have actually made a deliberate selection even if a RadioButton is selected; this would be the case if you wished to keep track of whether a user had changed the settings in a form or not.

### Button Groups

Different kits group RadioButtons together in different ways. Some kits have explicit ButtonGroup classes, while others do not. Even among kits with ButtGroup classes, the ButtonGroup might be a widget (in the sense that it is an element of the widget tree), or it might not (in that it will not be in the widget tree, will not be drawn, will not be an element of the RadioButton's parent widget and will not "take possession" of the RadioButton from the parent widget).

Many modern kits will create an *implicit* button group that contains all the RadioButtons that are children of a specific widget; that is, they will group together all the RadioButtons in a given widget. This allows our RadioButtons to function with minimal set-up; we need only add them to our GUI, and they will be grouped automatically.

The implicit approach can make it difficult to create a GUI with two or more *independant* button groups. In order to do this, we can simply create a blank BasicWidget to contain each group of RadioButtons; each of these BasicWidgets will then create a separate implicit button group for the RadioButtons that they contain.

Some kits use a hybrid approach; they group RadioButtons by containing widget by default, but they also provide us with a ButtonGroup class for fine control.

The ComboBox
------------

The ComboBox is similar to a Button, except that, when clicked, it will display a drop-down list of entries; the user can then select from among these entries. The ComboBox is useful for displaying a list of entities from which we want the user to make a single selection. It has the additional advantage over the RadioButton that it is very 'compact', and that its layout is predictable; it is therefore useful for the situation where our list of choices is either very large or unpredictable - that is, we cannot know what it will be before-hand.

ComboBoxes have two interesting properties, the list of 'possible' selections and the 'currently'-selected item. They provide us with a single interesting event, the `on_select` event, which is emitted when a selection is made from the pull-down menu. This event is somewhat different from the `Button`'s `on_click` event. `on_click` is emitted whenever the user clicks the Button, which is essentially their only way of interacting with the Button; `ComboBoxes` typically support 'cancelling' the interaction, perhaps by hitting the Escape key after clicking the button; this might result in an `on_click` event being issued without a corresponding `on_select` event.

Since we usually care about when the user makes a 'selection' and what they have selected and not whether or not the `ComboBox` was clicked, we will usually connect to the `on_select` event and not the `on_click` event, or the other events that the `ComboBox` might emit. In point of fact, since we often do not care about the selection displayed in the `ComboBox` until we wish to use it, we often will not connect to a signal on the ComboBox at all, but rather will fetch the current selection from the `ComboBox`'s `current_selection` property at some later point (for example after the user has clicked an "OK" `Button` and some processing is being performed).

Frequently, `ComboBoxes` will also have two other useful properties, 'editability' and 'read-only status'.

### Object Models

`ComboBoxes` can be very flexible, powerful widgets; they can often display much more than simple text labels. Many toolkits support sophisticated 'object models' that allow developers to have significant influence over how the combo-box behaves. Problematically for our purposes, these mechanisms are very distinct from platform to platform, and they are often also very complex. Therefore, exploring the entry-model facilities available on the reader's chosen platform is left as a (highly recommended!) exercise for the reader.

Having said this, it is worth noting that because these facilities 'exist' does not mean that they should always be used. In the majority of cases, developers will mainly want to present application users with a drop-down list of textual item names. Most kits make it possible to achieve this end without tangling with the platform's complex entity-modelling systems; when this facility is sufficient, users should likely not bother with building custom content models.

The SpinBox
-----------

SpinBoxes are not as common as the above widgets; they are not supported in Windows Presentation Foundation, for example. SpinBoxes are similar to ComboBoxes, except they are used to make a numerical selection; they will typically display a numerical value, and will have a "pull-down" indicator like a ComboBox; users will be able to increment or decrement the SpinBox by specific amounts.

There are several widgets that support numeric selections; SpinBoxes are useful when the space available for the widget in the GUI is limited, and in particular when only a specific range of numerical selections are possible (as SpinBoxes typically have a set precision, and typically increment or decrement by fixed amounts).

SpinBoxes have several interesting properties. Perhaps the most obvious is their current value; we are also interested in their 'default' value, their 'minimum' and 'maximum' values, and their 'increment' and 'decrement' steps. The combination of these values will determine the range of possible values that the SpinBox could have. Be aware that these, on some platforms, care must be taken to ensure that these settings 'agree'. For example, the 'increment' and 'decrement' should probably be the same value, providing a single step-size, and the minimum and maximum should be a multiple of that step size. The default value should also be chosen so that it is a multiple of step-size.

Examples
========

For concrete examples, see either [Selection Widgets in Python](getting started python.md) or [Selection Widgets with JavaFX](selections jfx.md)
