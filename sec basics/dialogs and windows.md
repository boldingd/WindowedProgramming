Up to now, we have been discussing the widgets that we will compose to
create our interfaces; the background of this discussion has been the
process of creating GUIs by placing some of the component widgets into
basic widgets (or some other analogous structure). But our applications
cannot consist of a single screen; in this chapter, we will have our
first discussion of having multiple active windows

Dialogs and Windows
===================

Almost every toolkit will give us the ability to create multiple windows
and dialogs at a time. This might seem unusual at first; how does the
system keep track of which windows belong to which applications?

Many operating systems will treat windows as 'system resources' that a
given process can 'own', much like files or memory. In the same way that
an application can request multiple files, the application can request
multiple windows; much like file objects abstract the OS's low-level
file access system, our tool-kit will likely provide us with some high
level class that represents the window resource that the OS gives us.
For convenience, our tool-kits may also provide us with a class that
both manages a window and inherits from `BasicWidget`.

Notice that the event loop as we have developed it can flexibly adapt to
a single application having multiple windows.

What Ends the Application
=========================

Having multiple windows requires us to think about what ends our
application - and how we end our application.

To answer the last question first, we can end our application by telling
the event loop to stop; if the event loop was the last thing in our main
file, then, after program flow leaves the event loop, our main function
will return and our application will end. Many kits will provide us with
a function to tell the event loop to terminate for precisely this
purpose.

To answer the first question, perhaps the most obvious way is to attach
a callback to some event, and to call the end-event-loop function in
that callback. The most obvious time to do so would be when some
privileged window is closed; if our application provides us with an
at\_window\_close event, we can register a callback to this event (on
some particular main window, or possibly for multiple windows) and call
the end-event-loop callback in that function.

Since this is a fairly wrote task, many kits provide us with a
convenience function that automates this process. Windows in java swing,
for example, have the "set\_default\_close\_operation" function, and the
value can be set to "exit\_on\_close"; this allows us to mark one (or
more) windows, and, when those windows are closed, the application will
exit.

Some other kits -- notably WPF -- keep track of how many windows are
open, and exit the event loop when no windows are left. This allows the
kit to have a reasonable policy for managing when our application
terminates, without us having to manage the process at all.

Modality
========

Sometimes, we want to block the user's access to other parts of an
application while a particular screen is being displayed; this might be
the case if, for example, if the user is interacting with a settings
dialog that will affect the primary screen. Most kits provide us with
the ability to mark certain windows as 'modal' with respect to other
windows; if a child window is modal with respect to a given parent
window, then the user will not be able to interact with the parent
window while the child window is being displayed. As the reader may have
guessed, most 'dialog windows' are modal.

Dialogs
=======

Dialogs are special windows; they are used to display alerts to the user
(such as an alert box reporting an application failure), or to ask the
user to make a decision (such as a dialog asking the user if they wish
to save a document or not) or for more detailed interactions (such as a
file selection or color selection dialog). In principle, dialogs are
nothing more than modal windows that display appropriate contents. We
could create them by creating top-level windows, packing those windows
with children, marking them as modal with respect to the application's
main window, and then marking them as visible. We typically will not
build dialogs by hand, however, for two major reason. The first is that
building a dialog by hand is a tedious process, and one that can be
easily automated. The second, more important reason is 'platform
integration'; users have expectations about how familiar dialogs will
behave, based on how the other dialogs on their platforms behave. If we
create our dialogs by hand, we will have to reproduce every behavior of
the platform's default dialog - every keyboard shortcut, ever feature.
If we do not, the user's interaction with our application will be
disrupted when they discover that they cannot trigger our dialog's
'cancel' action by hitting escape, for example - because we would have
had to replicate that behavior in specific code, and perhaps we did not
think to, or did not have time.

Because of the first reason, almost every kit in existence will provide
you with a selection of dialogs, and convenience-functions to display
them. For the second reason, you should use these default dialogs
wherever possible.

Needless to say, this assumes that our kit includes a version of the
dialog that we want. For common dialogs -- like error dialogs, print
dialogs or font dialogs -- this is very likely to be the case. However,
if we need an unusual dialog, we will need to build it ourselves.

Show Functions
==============

Many kits will include a `show` function that will display the given
dialog; for some kits, this will be a member function of a dialog
object, while for others it will be a static class function. In most
cases, these functions will suspend the operation of your code at the
point that they are called, while the dialog is run; they will then
resume at the same point in your callback, and will return the results
of the user's action (for example, by having a `ShowFileDialog` function
return the file path the user picked as a string).

While this is simple in concept, and makes our code simple, the student
should be aware that this is in fact a complex operation internally.
These functions have to start a second main loop to manage the
application while the show function has blocked the original main loop.
