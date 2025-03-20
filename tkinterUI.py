import tkinter as tk

# Define the VisualInterface ancestor class
class VisualInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.buttons = []  # List to store button objects
        self.actions = []  # Array to store the values of user actions (button clicks)
        self.total = 0.00  # Initialize the total to 0.00
        self.total_label = None  # To display the total on the UI
        self.root.configure(bg='black')  # Set the background color to black
        self.message_label = None  # Label to show messages

        # Center the window on the screen and make it non-resizable
        self.center_window(500, 300)
        self.root.resizable(False, False)  # Prevent resizing

    def center_window(self, width, height):
        """
        Centers the Tkinter window on the screen.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)

        # Set the window geometry
        self.root.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def addInputMethod(self, button_properties):
        """
        Method to add a button to the interface based on provided properties.
        button_properties is a dictionary containing button label, color, position, etc.
        """
        # Unpack properties
        label = button_properties.get("label", "Button")
        color = button_properties.get("color", "lightblue")
        x_pos = button_properties.get("x", 0)
        y_pos = button_properties.get("y", 0)
        
        # Create the button and place it on the window
        button = tk.Button(self.root, text=label, bg=color, command=lambda: self.button_action(label))
        
        # Place the button
        button.place(x=x_pos, y=y_pos)
        
        self.buttons.append(button)

    def button_action(self, label):
        """
        Action when a button is clicked. This will add the value associated with the button
        to the total and update the total display.
        """
        if label == "Add 1 cent":
            value = 0.01
        elif label == "Add 2 cent":
            value = 0.02
        elif label == "Add 5 cent":
            value = 0.05
        elif label == "Add 10 cent":
            value = 0.10
        elif label == "Add 20 cent":
             value = 0.20
        elif label == "Add 50 cent":
            value = 0.50
        elif label == "Add 1 Euro":
            value = 1.00
        elif label == "Add 2 Euro":
            value = 2.00
        elif label == "Add 5 Euro":
            value = 5.00
        elif label == "Add 10 Euro":
            value = 10.00
        elif label == "Add 20 Euro":
            value = 20.00
        elif label == "Add 50 Euro":
            value = 50.00
        elif label == "Add 100 Euro":
            value = 100.00
        else:
            return  # No valid label
        
        # Add the value to the actions array
        self.actions.append(value)
        
        # Calculate the total sum of all actions
        self.total = sum(self.actions)
        
        # Check if the sum exceeds 100 Euro
        if self.total > 100:
            self.show_message(f"Your sum of €{self.total:.2f} is more than 100 Euro. The operation is declined.")
            self.reset_total_after_delay()
        else:
            # Update the total label with the new total
            self.update_total_label()

    def update_total_label(self):
        """
        Updates the label showing the total amount.
        """
        if self.total_label is None:
            # Create the total label if it doesn't exist
            self.total_label = tk.Label(self.root, text=f"Total: €{self.total:.2f}", font=("Arial", 14), fg="white", bg="black")
            self.total_label.place(x=10, y=10)
        else:
            # Update the existing total label with the new total
            self.total_label.config(text=f"Total: €{self.total:.2f}")

    def show_message(self, message):
        """
        Shows a message to the user in a label on the window.
        """
        if self.message_label:
            self.message_label.config(text=message)
        else:
            self.message_label = tk.Label(self.root, text=message, font=("Arial", 14), fg="red", bg="black")
            self.message_label.place(x=10, y=150)

    def reset_total_after_delay(self):
        """
        Resets the total to 0 after 5 seconds and removes the total label.
        """
        # After 5 seconds, reset the total and remove the total label
        self.root.after(5000, self.reset_total)

    def reset_total(self):
        """
        Reset the total to zero and remove the total label.
        """
        self.total = 0.00
        self.actions.clear()  # Clear the actions array
        # Remove the total label
        if self.total_label:
            self.total_label.destroy()
            self.total_label = None
        # Reset the message label
        if self.message_label:
            self.message_label.config(text="")
        
        # Update the UI to reflect the reset
        self.update_total_label()

    def execute_conversion(self):
        """
        When the 'Execute' button is clicked, this function calculates the combination of Euro
        denominations that make up the current total and displays the result.
        """
        # Denominations available in the currency system
        denominations = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
        remaining_amount = self.total
        change = []

        for denom in denominations:
            count = int(remaining_amount // denom)  # Get how many times the denomination fits into the remaining amount
            if count > 0:
                change.append(f"{count} x {denom} Euro")
            remaining_amount -= count * denom

        # If we have a result, display it; otherwise, show an error
        if change:
            result_message = f"You have: " + ", ".join(change)
            self.show_message(result_message)
        else:
            self.show_message("No denominations found.")

# Define the ConsoleInterface ancestor class
class ConsoleInterface:
    def __init__(self):
        self.console_output = ""
    
    def show_console_message(self, message):
        """
        Method to simulate showing messages in the console interface.
        Here, we'll print to the actual console.
        """
        self.console_output += message + "\n"
        print(self.console_output)

# Define the UI class that inherits both VisualInterface and ConsoleInterface
class UI(VisualInterface, ConsoleInterface):
    def __init__(self, root):
        VisualInterface.__init__(self, root)  # Initialize VisualInterface
        ConsoleInterface.__init__(self)  # Initialize ConsoleInterface
        
    def show(self):
        """
        Method to display the UI (buttons) on the window.
        """
        # Define button properties (labels, colors, positions, padding)
        button_properties = [
            {"label": "Add 1 cent", "color": "lightgreen", "x": 10, "y": 50},
            {"label": "Add 2 cent", "color": "lightgreen", "x": 10, "y": 80},
            {"label": "Add 5 cent", "color": "lightgreen", "x": 10, "y": 110},
            {"label": "Add 10 cent", "color": "lightgreen", "x": 10, "y": 140},
            {"label": "Add 20 cent", "color": "lightgreen", "x": 90, "y": 50},
            {"label": "Add 50 cent", "color": "lightgreen", "x": 90, "y": 80},
            {"label": "Add 1 Euro", "color": "lightgreen", "x": 90, "y": 110},
            {"label": "Add 2 Euro", "color": "lightgreen", "x": 90, "y": 140},
            {"label": "Add 5 Euro", "color": "lightblue", "x": 10, "y": 170},
            {"label": "Add 10 Euro", "color": "lightblue", "x": 90, "y": 170},
            {"label": "Add 20 Euro", "color": "lightblue", "x": 170, "y": 170},
            {"label": "Add 50 Euro", "color": "lightblue", "x": 250, "y": 170},
            {"label": "Add 100 Euro", "color": "lightblue", "x":330, "y": 170},
            {"label": "Execute", "color": "lightyellow", "x": 200, "y": 200},
        ]
        
        # Add buttons using the 'addInputMethod'
        for button_prop in button_properties:
            self.addInputMethod(button_prop)
        
        # Display a console message for confirmation
        self.show_console_message("UI loaded with buttons!")

        # Bind the "Execute" button
        execute_button = self.buttons[-1]  # The last button is the "Execute" button
        execute_button.config(command=self.execute_conversion)

# Main function to run the app
def main():
    # Create the main window
    root = tk.Tk()
    root.geometry("500x300")  # Set window size
    root.resizable(False, False)  # Prevent resizing

    # Create the UI instance
    ui = UI(root)

    # Display the UI (buttons)
    ui.show()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
