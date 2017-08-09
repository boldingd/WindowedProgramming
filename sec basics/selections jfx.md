Selection Widgets with JavaFX
=============================

Now let's look at selection widgets using JavaFX.
We'll create a class to contain our inerface, much like last time; we'll then create our interface inside the constructor for that class.
The code below, unless otherwise noted, will go inside this constructor:

``` java
class CheckWidget extends GridPane {

    public CheckWidget() {
        // code to build our interface will go in here
    }
}
```

We will also omit the import statements that we add, until the final code listing.

## The Checkbox

We can create a check-box simply enough:

``` java
        CheckBox cb = new CheckBox("Checky the CheckBox");
        add(cb, 0, 0);
```

JavaFX `CheckBoxes` actually support three states: checked, unchecked and *undefined*.
Though the undefined state can be useful, most of the time, we want the check-box to be in either the checked or unchecked state.
We can disable the *undefined* state like this:

``` java
        cb.setAllowIndeterminate(false);
```

We can also determine if we want the check-box to be selected or not like this:

``` java
        cb.setSelected(false);
```

We can of course also use `getSelected()` to determine if our check-box is checked or not.

## Binding to Properties

Like many modern tool-kits, JavaFX supports the idea of *binding* to the *properties* of a widget; this is a little ugly to do in explicit code, but is very useful when we build our interfaces using a *declarative language*, like FXML (which we will cover later).

We can add a `ChangeListener` to an `ObservableProperty`, like the `CheckBox`'s `selected` property; to save some slightly convoluted anonymous class construction, we'll skip directly to the use of a *lambda express*:

``` java
        cb.selectedProperty().addListener(
            (observable, oldval, newval) -> {
                if (newval) {
                    System.out.println("checked");
                } else {
                    System.out.println("unchecked");
                }
            }
        );
```

Most things that are exposed as properties are also accessable using normal getter and setter methods -- we can, for example, also use `cb.isSelected()` and `cb.setSelected(boolean)`.

## Radio Buttons

JavaFX uses `ToggleGroup`s to manage radio buttons.
We can create two `ToggleGroup`s, and assign two `RadioButton`s to each, like so:

``` java
        ToggleGroup tg1 = new ToggleGroup();
        ToggleGroup tg2 = new ToggleGroup();

        RadioButton rb_g1_1 = new RadioButton("Option 1");
        rb_g1_1.setToggleGroup(tg1);
        add(rb_g1_1, 1, 1);

        RadioButton rb_g1_2 = new RadioButton("Option 2");
        rb_g1_2.setToggleGroup(tg1);
        add(rb_g1_2, 1, 2);

        RadioButton rb_g2_1 = new RadioButton("Option A");
        rb_g2_1.setToggleGroup(tg2);
        add(rb_g2_1, 2, 1);

        RadioButton rb_g2_2 = new RadioButton("Option B");
        rb_g2_2.setToggleGroup(tg2);
        add(rb_g2_2, 2, 2);
```

Notice that we've laid out the second column of toggle buttons beside the first.

The `RadioButton` allows us to use `setOnAction` to assign an `ActionListener` to a `RadioButton` just like we did before with a normal `Button`, but that usually isn't ideal; what we usually actually want is to know which button in a group is selected, and we can get that information directly from the `selectedToggle` property of the `ToggleGroup`.
Again, using a lambda expression:

``` java
        tg.selectedToggleProperty().addListener(
            (observable, old_toggle, new_toggle) -> {
                if (new_toggle == rb_g1_1) {
                    System.out.println("Option 1");
                } else if (new_toggle == rb_g1_2) {
                    System.out.println("Option 2");
                }
            }
        );
```

## The ComboBox

The `ComboBox` has a *non-trivial* interface; it's a very flexible control, but also a very complex control.
It's a generic class; it allows us to give it a list of any type, and to tell it how to *render* each option.
While this allows us to create impressive displays, it's also complex.

We're going to focus on the simplest case, where it's given a list of strings to display.
That looks like this:

``` java
        ComboBox<String> combo = new ComboBox<String>();
        combo.getItems().addAll("Option A", "Option B", "Option C");
        add(combo, 0, 4);
```

As with other controls, we could access the current selection with the `getValue` method, but we can also add a listener to the `valueProperty`, like so:

``` java
        combo.valueProperty().addListener(
            (observable, old_value, new_value) -> {
                System.out.println(new_value);
            }
        );
```

Note that both `old_value` and `new_value` are `String`s, which was the template type we gave the ComboBox when we constructed it; of course, they'll be a different type if you give a different type as a template type.

