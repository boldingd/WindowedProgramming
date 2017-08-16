Long-Running Jobs
=================

Most of our callbacks have been focused on manipulating the state of the
interface; partly as a result of this, most of our callbacks have also
been very short. There is another reason that our callbacks are very
short: a very long callback would delay the event-loop, and prevent the
interface from updating. This might leave the student to wonder, how is
their program to do any actual work?

Say that you are writing a program to download resources from the Web.
Downloading large files can take time; certainly this cannot be placed
directly in a callback, as we would not want to pause the event loop
until the download is completed. We can also note that, for example, web
browsers certainly do not act like that; the interface continues to
update as the download proceeds. (If it did not, download progress bars
would not work.)

In this chapter, we will discuss how to handle such *long-running* or
*background* jobs.

Idle Events
===========

Idle Events are an old scheme for handling long-running jobs. Many
tool-kits provide an *idle event*. And idle event is triggered at some
predictable point in the event loop -- such as at the end, after all
other events have been processed. In order to handle a long-running job,
a callback is attached to the idle event; every time the idle event
occurs and the callback is triggered, the idle callback will perform a
small step in the long-running job. (This requires that the progress of
the long-running job is being tracked somewhere, so that the
user-interface can update any progress display that exists, and so the
idle callback knows what step it is going to do next.)

It is important here that it is possible to split up the long-running
job into a sequence of very small steps; the idle callback, like any
other callback, is being run at a specific point in the event loop. If
the idle callback takes too much time to return, it will cause the event
loop to be delayed. It can sometimes be very difficult to split a
long-term operation into small chunks; this can become an especially big
problem when we do not *know* how long a chunk will take. Some file and
network operations, for example, will usually be *fast*, but can
sometimes take very long times to complete; this can mean that our
idle-events can sometimes surprise us by take a very long time to
complete.

It can be very complex to set up all of this machinery, and there can be
quite a lot of subtlety involved. Thankfully, more modern techniques
exist, largely enabled by modern multi-threading operating systems and
hardware.

Multi-Threading
===============

With the rise of multi-threading operating systems (and programming
languages), it has become feasible to split our long-running jobs off
into their own threads. This prevents us from having to place our
long-running jobs in the event loop, which also conveniently removes any
need to split our job up into small operations.

It also introduces a complexity, however; there must be some mechanism
for communicating between the main UI and the job in the event loop --
even if for no other reason than to detect when the job has completed.
While this might seem simple, this communication must be coordinated
with the event loop. If we change the state of a widget from the "work"
thread, it is possible that we might change that widget's state at any
point in the event loop -- for example, while it is being redrawn, or
while the layout is being computed. This can result in the widget
drawing itself incorrectly, for example.

A common solution is to use a synchronized object to communicate between
the widgets in the UI and the status of the work thread. We will likely
still have to use an idle event, but this time, all it will be doing is
checking the state stored in the synchronized object, and updating the
state of the UI appropriately. Of course, as in any multi-threading
scenario, we will still have to carefully manage the locking of the
synchronized object; an error could result in the idle-event callback
waiting for the synchronized object forever, for example, which would
freeze our event loop.

BackgroundWorker classes
------------------------

Such multithreading schemes can be difficult to set up -- but, at the
same time, many such systems ultimately work the same way when
completed. Because of this, many kits provide us with a BackgroundWorker
class. BackgroundWorkers set up much of this machinery on their own;
they also frequently provide us with events that the BackgroundWorkers
will generate (and the BackgroundWorkers will make sure that these
events are generated at an appropriate time with respect to the event
loop). This can make our job very simple: create a BackgroundWorker,
provide it with a method that holds the logic for our long-running job,
and wire its events up appropriately; we then simply start the
BackgroundWorker.

BackgroundWorkers can provide many sophisticated capabilities: most
support some facility for reporting 'progress', typically by generating
an event. Notably, some BackgroundWorkers -- such as the one provided in
Java Swing -- are single-use. This requires the creation of a new
BackgroundWorker every time a job is to be run.
