Getting Started with JavaFX
===========================

Let's build a simple layout using JavaFX.

The Application class is the starting-point for all JavaFX applications, so we'll start by importing it and difining one.

``` java
import javafx.application.Application;

public class BasicApplication extends Application {
    @Override
    public void start(Stage primaryStage) {

    }
}
```

We don't need to provide a main method; if we run this class, the JVM will automatically launch the application.
It will do this by calling the `start` method on our application -- there are several other methods that we can override, but just `start` will do for now.

The Start method will be given one `Stage` as an argument; `Stage`s are loosely analogous to *windows*; they are the contexts in which our widgets are drawn.
What we need to do, in our implementation of the `start` method, is build our interface.

JavaFX represents interfaces as collections of *nodes* in a *scene-graph*, which in turn belongs to a `Scene` object.
We'll build our interface by defining some top-level node, and then adding child nodes to it; we will then construct a new `scene` and give it our top-level widget as an argument; in turn, we'll then give that `Scene` to the default stage.

A GridPane will make a pretty good top-level node -- it's designed to contain and layout children, after all!

``` java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.text.*;

import javafx.stage.Stage;

public class BasicWindow extends Application {
    @Override
    public void start(Stage primaryStage) {
        GridPane root = new GridPane();

        Label l = new Label("A Label");
        root.add(l, 0, 0);

        Button b = new Button("A Button");
        root.add(b, 1, 0);
        
        primaryStage.setTitle("Starting Out");
        
        primaryStage.setScene(new Scene(root, 400, 400));
        primaryStage.show();
    }
}
```

Here we've also built a `Label` and a `Button` widget, and added them to our `GridPane`.
(The `add` method takes the node to be added, the column and the row as parameters, in that order.
There are other overrides that take more parameters, like row- and column-spans.)

This works, but it would be very impractical to try to build an entire large, complex interface in this one method.
We would very much like to break our interface into seperate components, and package them into classes.

The GridPane makes a fairly good super-class for an interface component; we can break the GridPanel and its children into a separate class...

``` java
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.text.*;

import javafx.stage.Stage;

class BasicWidget extends GridPane {
    public BasicWidget() {
        Label l = new Label("A Label");
        add(l, 0, 0);

        Button b = new Button("A Button");
        add(b, 1, 0);
    }
}
```

...which we can then construct when we start our application...

``` java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class BasicWindow extends Application {
    @Override
    public void start(Stage primaryStage) {
        BasicWidget bw = new BasicWidget();

        primaryStage.setTitle("ded");

        primaryStage.setScene(new Scene(bw, 400, 400));
        primaryStage.show();
    }
}
```

Finally, a button that doesn't do anything isn't particularly interesting.
Let's make our button print a message when it's clicked.

Unfortunately, this process is a little complicated.
We represent our callback as an object that implements the EventHandler interface; EventHandler defines one method, `void handle(T event)`; we'll fill in the implementation of that method with our callback.
(`EventHandler` is a *template class*, and the `T` in that signature is the template parameter -- which in this case is the type of event that we're handling.
If you aren't familiar with templates and generics, see the [java tutorials on generics](https://docs.oracle.com/javase/tutorial/extra/generics/index.html).)

We could create a new class that implements the EventHandler interface, create an instance of it, and give it to our button.
For a hypathetical `MyEventHandler` class, that might look like this:

    b.setOnAction(new MyEventHandler());

But if we had to do that for every button, our source directory might start to get overrun with trivial, ten-line event-handling classes.
Fortunately, Java allows us to define a new [anonymous class](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html) in-line; doing so looks like this:

``` java
b.setOnAction(new EventHandler<ActionEvent>() {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("button clicked!.");
    }
});
```

That's quite a statement!
We're creating a new object, of an anonymous class that implements `EventHandler`, and providing a definition of the `handle()` method in-line.
(Note that we provided `ActionEvent` as the template parameter; `ActionEvent` was then the type of event that was the first parameter of the `handle` method.)

This is still a little cumbersome; more recently, Java also gained the ability to define a [lambda expression](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html).
Using a lambda expression, our callback looks like this:

``` java 
b.setOnAction(
    event -> System.out.println("Button clicked.");
);
```

Very concise!
