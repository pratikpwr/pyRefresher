class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.is_connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.is_connected = False
        print("Disconnected")


# class inheritance

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} remaining pages.)"

    def print(self, pages):
        if not self.is_connected:
            print("Printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


pgs = int(input("Enter no of pages sto print: "))
printer = Printer('Printer', "WIFI", 200)
printer.print(pgs)

print(printer)
printer.disconnect()
