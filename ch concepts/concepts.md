Basic Concepts
==============

Things Will Be Different
------------------------

Things are a little different when working with event-driven systems.

The first programs you wrote were probably simple single-file programs. They had a beginning, ran through several steps, and reached an end. Your programs may have grown to encompass more functions, files and modules, but they probably still had some concept of a "current instruction," and there was probably some flow through the program that you could, in principle, follow.

This is of course still true of event-driven programs "under the hood," but this is not how you, the programmer, will view them. You will not (necessarily) be starting at a given entry point (like a main routine) and then tracking your program flow as it moves through various stages of execution.

In event-driven programming, you are instead given an *environment*. You will add *entities* into this environment, and you will define how those entities respond to *events* that come from the environment. You will set this construct up and then "let it go," and its exact behavior will depend on the specific events that your system receives from the environment.

Events and Callbacks
--------------------

Let us begin by first examining the concept of a *callback*. A *callback* is a function that a programmer provides to some external library, so that the library can trigger that function at some other time; abstractly, they are a way to specify to the library in question what we want *done* at some future point, thereby specifying how the library will *behave* or *respond*.

The exact details of how we do this and what our callbacks will look like will vary from language to language, from GUI library to GUI library and from problem area to problem area. Registering a key-press-handling callback in a 3D game written in C++ will look *very* different from setting a callback to process a message-received event in a Java programming listening to an internet socket or an on-mouse-click event handler written in JavaScript on a web-site.

An Example: Processing Numbers
------------------------------

To give us something concrete to work with, let us turn to an example. Consider a Python program that we will use to analyze an arbitrary series of numbers:

``` Python
def PrintIfEven(number):
  if number % 2 == 0:
    print(str(number))

def AbortIfFortyseven(number):
  if number == 47:
    gp_SignalAbort()

gp_RegisterCallback(PrintIfEven)
gp_RegisterCallback(AbortIfFortyseven)

gp_Run()
```

The above program assumes that 'some' library is providing the `gp_*` functions that we are using. Omitting the code for that library is not accidental; in the context of GUI development, you usually will be working with some existing event-generating library, and you usually will not be concerning yourself with that library's internals.

Also note that much of the work done in this program occurs "out of our sight". It might not even be completely obvious what the program is going to do when run, since we don't know under what conditions our callbacks will actually be used -- that is, we don't know when `gp_Run` is going to run our callbacks. This is also a feature of event-driven programming; we have to have some expectation of what kinds of events we're going to receive from the environment (and what we can do with the environment in response) in order to write our program, but we don't know precisely what is going to happen.

Looking into what's happening here, we first define two functions, each with a single argument. These functions both evaluate their arguments, and do something "interesting" depending on what values they've received. In the first, if the `number` given as an argument is even, the function then prints that number. In the second, if the `number` is exactly 47, the function calls the `gp_SignalAbort` library routine; we'll come back to this function in a little bit.

We then come to the `gp_RegisterCallback` function, which takes a single argument, which it expects to be a function. `gp_RegisterCallback` registers our number-processing functions with the (implicit) number-generating GP library; it tells the GP library to call the given functions every time a new number is generated. We call `gp_RegisterCallback` twice, once with each of the callbacks that we defined.

Depending on what languages you are familiar with, it may seem odd to pass a function name as an argument to another function. Python supports *functional programming* -- that is, in Python it is possible to treat functions variables. They can be handled just like any other variable; they can be assigned, returned from functions, passed into functions and so on. This facility exists in some languages and not in others; for example, it exists in some sense in C, where function pointers replicate *some* of this functionality, but it does not exist as such in Java. I make note of this to point out an important fact of event-driven programming, and later graphical programming: the right way to do a given thing will depend heavily on the features supported by your *language* or event-generating *library*. While the abstract *idea* might be the same from language to language or GUI tool-kit to tool-kit, the *exact* way that you define, handle or trigger your callbacks will be different in different languages. For example, in Python you might define your callbacks as functions directly, while in Java you might define an object that overrides the some `HandleEvent` method defined in an `EventHandler` interface.

Returning to our example, we finally call `gp_Run()`. Presumably, the `gp_Run()` function will generate an arbitrary sequence of numbers, and call every function registered with `gp_RegisterCallback` with each generated number as an argument. The GP library maintains some 'state', including an `Abort` flag. The GP library will periodically check if that flag has been set to `True`; if it has, the `gp_Run` function will return, thus ending the generation and evaluation of numbers.

Note that the behavior of the program when run will be determined by the callbacks that we have provided (as well as by how `gp_Run` *generates* numbers, a question that we will turn to momentarily). We determine what is done (or not done) with each number; presently, we print the even ones, but with different callbacks we might, for example, write every prime number to disk, or simply count how many numbers are generated before the program is terminated. Similarly, we determine under what conditions the program will halt; if none of our callbacks ever called `gp_SignalAbort`, then presumably our example would never terminate.

Events
------

In the previous example, we did not specify under what conditions `gp_Run` will generate numbers. We might suppose that it simply generates numbers continuously and then feeds them into our callbacks, so long as `gp_SignalAbort` has not been called; this is in fact the implementation of `gp_Run` that the author used to error-check the example.

But this is far from the only way that `gp_Run` could be implemented. Suppose that it instead were to monitor the keyboard; every time a key on the keyboard is pressed, `gp_Run` could pass the character-code for that key into the callbacks that had been registered.

This would radically change the way that we would expect our program to behave. If we assumed that our callbacks would simply receive a stream of arbitrary numbers, then, when our code is run, we might expect to see a stream of arbitrary (even) numbers generated on the console. At some point, when the number 47 is generated, we would expect the stream to stop.

But if a number is generated and processed if and only if a key is pressed, we would expect completely different behaviour. For one thing, we would only expect to see output generated when we press a key; our callbacks would not be called unless a key is pressed. In this alternate set-up, our program is not simply processing a stream of numbers; it is instead responding to changes that are happening in our program's environment -- that environment being the keyboard.

This is the key concept of event-driven programming: instead of running through some specified procedure until the job we wish to perform is done, our program instead watches the environment for changes, and then responds to those changes when they occur. We call these changes *events*, and we determine how we respond to those events by specifying the callbacks that we wish to be invoked when a given event occurs.

It is worth noting that our original Python example provides a single event, the generation of a number. If we wanted to specify different behaviours for different *types* of numbers (even, odd, prime or so one) we need to determine what type of number was generated in our callbacks. In most realistic applications, this is not the case; there will generally be many possible events that an entity in the environment could generate, each with their own distinct list of registered callbacks. For example, in a Java SWING GUI, an image might have one set of callbacks registered for when the user *left*-clicks the image (which we would call a left-click event), and another set of callbacks for when the user *right*-clicks the image (which we would call a right-click event).

Generating Events
=================

Having looked at the process of creating callbacks, let us take a moment to consider how the system generated and dispatches events. Though this will generally not be our responsibility when working with GUI libraries, it is worthwhile to understand in the abstract how this process operates.

Event Loops
-----------

In the abstract, we will frequently set up entities in the environment, add callbacks for the events that might be generated and then ask the system to begin to process events; we can see this last step in the previous Python example when `gp_Run` function is called. This function represents what is often termed an *event loop*; an event loop is a function that monitors the state of a given environment (and the entities that it contains) and dispatches events that correspond to any changes that occur.

In slightly more concrete terms, event loops are typically infinite loops. They will maintain a copy of the environment's last state; until some predetermined stopping condition occurs, they will compare the current state of the environment to the last state that was seen. If a change has occurred, this will be viewed as an event; if any handlers were registered for this event, those handlers will be invoked. They will then update their state record with the state that was just encountered, and return to the head of the loop.

The result, from our point of view, is what we have seen; we set up a list of callbacks and specify the events that we wish to trigger those callbacks, and then invoke the event loop; the event loop then monitors the environment and triggers our callbacks as necessary.

A Java Example
--------------

As a concrete example, let us consider a Java class that watches the state of the mouse. If the mouse moves, it will create a MouseMotionEvent that describes that motion and invoke any registered event handlers; if no motion occurs, no action will be taken. The event-loop will not terminate unless a callback requests that it do so: in this specific case, callbacks may do this by simply returning `false`. The code for this class is given below:

``` java
import java.util.Vector;

import java.awt.MouseInfo;
import java.awt.PointerInfo;
import java.awt.Point;


public class MouseWatcher {

    private Vector<MouseMotionEventHandler> EventHandlers;

    public MouseWatcher() {
        EventHandlers = new Vector<MouseMotionEventHandler>();
    }

    public void RegisterMouseMotionEventHandler(MouseMotionEventHandler handler) {
        EventHandlers.add(handler);
    }

    public void WatchMouse() {
        boolean AbortFlag = false;

        int lastX, lastY;

        Point p = MouseInfo.getPointerInfo().getLocation();
        lastX = p.x;
        lastY = p.y;

        while (AbortFlag == false) {
            p = MouseInfo.getPointerInfo().getLocation();
            int delX = p.x - lastX;
            lastX = p.x;

            int delY = p.y - lastY;
            lastY = p.y;

            if (delX != 0 || delY != 0) {
                MouseMotionEvent e = new MouseMotionEvent();
                e.HorizontalMotion = delX;
                e.VerticalMotion = delY;

                for (MouseMotionEventHandler handler: EventHandlers) {
                    boolean handlerResult = handler.HandleMouseMotionEvent(e);

                    if (handlerResult == false) {
                        AbortFlag = true;
                    }
                }
            }
        }

        return;
    }

}
```

This example uses the following definitions for the `MouseMotionEvent` class:

``` java
public class MouseMotionEvent {
    public int HorizontalMotion;
    public int VerticalMotion;
}
```

and the `MouseMotionEventHandler` interface:

``` java
public interface MouseMotionEventHandler {

    public boolean HandleMouseMotionEvent(MouseMotionEvent event);

}
```

Of primary interest is the WatchMouse function, which in this case is our event loop. We store the last observed mouse position in `lastX` and `lastY`. Then, until we detect that a callback has requested that we terminate, we get the current position of the mouse, and compute the difference between the current position and the last position. If a change has occurred, we construct a `MouseMotionEvent` and invoke every registered `MouseMotionEventHandler` with that event as an argument; if any of those handlers return `false`, we set the `AbortFlag`. We then update our record of the last mouse position with what we just fetched.

Consider how this might be used: potential client code is presented below.

``` java
public class MouseListeners {
    public static void main(String args[]) {

        MouseWatcher watcher = new MouseWatcher();

        watcher.RegisterMouseMotionEventHandler(new MouseMotionEventHandler() {
            public boolean HandleMouseMotionEvent(MouseMotionEvent event) {
                int distance_square = event.HorizontalMotion * event.HorizontalMotion;
                distance_square += event.VerticalMotion * event.VerticalMotion;
                double distance = Math.sqrt((double) distance_square);

                System.out.println("Distance moved:  " + String.valueOf(distance));

                if (distance > 20.0) {
                    System.out.println("Requesting abort!");
                    return false;
                }

                return true;
            }
        });

        watcher.WatchMouse();

        return;
    }

}
```

In this example, we declare an anonymous class that implements the `MouseMotionEventHandler` interface. The `HandleMouseMotionEvent` function that we have provided here computes the distance that the mouse has moved; if the mouse has moved more than 20 unites (which, though unspecified, we may reasonably assume are pixels), the handler requests that event processing terminates. The distance moved is printed in either case. When run, this generates output similar to the following:

    Distance moved:  1.4142135623730951
    Distance moved:  1.4142135623730951
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.0
    Distance moved:  1.4142135623730951
    Distance moved:  2.8284271247461903
    Distance moved:  2.23606797749979
    Distance moved:  3.0
    Distance moved:  2.23606797749979
    Distance moved:  4.47213595499958
    Distance moved:  12.041594578792296
    Distance moved:  11.180339887498949
    Distance moved:  25.0
    Requesting abort!

There is a subtlety here; notice that the output that we see depends on how quickly our event-handlers run. If our handlers run quickly, we will likely see vary small changes reported; if the mouse is moved at a constant rate, quicker callbacks means a shorter span of time will pass between checks by the event-loop. However, if one of our callbacks took a very long time to run, then this would mean that it will be a very long time before the event-loop checks the state of the mouse again. This might mean that a very large change in position is reported; it might also mean that some mouse motion is missed entirely. If for example the mouse was moved some distance to the right and then moved *back* some distance to the left during the span of time in which the long callback was running, then the mouse motion will be reported as less than it actually was, since we only know the last position we saw the mouse and the current position where we see the mouse.

This suggests what is actually a very general principle; your callbacks should be *fast*. What exactly "fast" means we shall not precisely define; as a bound, for GUI programming, any callback whose execution time a human could perceive is a callback that is far too slow. The faster your callbacks are, the more responsive your program will be; the slower your callbacks are, the more your interfaces will stutter.

The student may wonder how exactly one is to handle a long-running process, such as fetching a resource from the internet. The short answer is that we do this outside of a callback; we mark the interface such that the user knows that a long-running job is being performed, we start the job perhaps on another thread, and we return to event-processing on the main thread. Part of our event-processing may be to check the status of the long-running job, so that we can update the interface with that jobs current state. Having said this, handling long-running jobs is a more involved topic that we shall return to later.
