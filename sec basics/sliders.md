Sliders and Progress Bars
=========================

Two other common widgets are presented here, the 'slider' and the
'progress-bar'. These widgets serve distinct purposes; they are
presented together here because they have similar properties.

The Progress Bar
================

The most basic of the two 'percentage widgets' is the progress bar. The
progress bar is a vertical bar that is filled to some partial degree; it
is typically used to display the percentage of progress through some
ongoing task. (We will revisit background tasks later.)

The progress-bar has three important properties, perhaps the most
obvious of which is the current value that it displays. We can change
the progress on some task by changing the value displayed in the
progress bar. The 'minimum value' and 'maximum valye' properties are
also important; they allow us to use increments for our task that are
convenient for our purposes, without having to do math in our code to
convert our current status to a percentage.

indeterminate mode
------------------

We do not always know how long our applications will take to perform
some task. If we are writing a program to find the shortest path between
two given URLs on the web, for example, we might not know what that
shortest path is, or how much more work we will have to do to find that
path. In situations like this, we still wish to communicate to the user
that our application is still running.

For this reason, many toolkits allow sliders to be placed in an
'indeterminate' mode. In this mode, the slider does not display some
given percent; rather, it will run some animation, such as pulsing or
filling and unfilling. This is useful because our slider is updated
during the event/render loop; if the event/render loop is hung by
something, the animation in our slider bar will stop running.

The Slider
==========

The slider is a control rather then a display - or in addition to being
a display. The slider renders as a long bar with an indicator for the
current value; it allows the user to grab the indicator and move it back
and forth along the bar.

Like the progress-bar, the slider exposes its minimum, maximum and
current value as properties; we could potentially use the slider as a
progress display using these, and this is sometimes done in media
players. (Obviously, we should not use the slider bar purely as a
display; the user will expect to be able to grab and move the slider to
control the displayed value.) However, the slider also gives us an
interesting event; the `value_changed` event; When the user grabs the
slider and moves it, the `value_changed` event will be triggered.

As with the combo box, the slider will usually offer the user
sophisticated interactions, like the ability to cancel a change; the bar
will typically issue the `value_changed` event only when it is
appropriate (not, for example, any time the slider is clicked).
Similarly, the slider will keep track of the user's interactions without
our having to do any special event wiring.

Unlike the combo box (and the other button-like widgets), we often will
want to connect to the `value_changed` event. If we are working on a
media player, we would want do jump to a different location in the track
being played when the user moves the slider.
