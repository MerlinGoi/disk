#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Box.H>
#include <string>

Fl_Input *nameInput;
Fl_Box *messageBox;

void onSubmit(Fl_Widget*, void*) {
    std::string name = nameInput->value();
    messageBox->label(("Welcome, " + name + "!").c_str());
}

int main(int argc, char **argv) {
    Fl_Window *window = new Fl_Window(300, 200, "Name Entry");

    nameInput = new Fl_Input(100, 40, 150, 30, "Name:");
    Fl_Button *submitBtn = new Fl_Button(100, 80, 100, 30, "Submit");
    messageBox = new Fl_Box(50, 130, 200, 30, "");

    submitBtn->callback(onSubmit);

    window->end();
    window->show(argc, argv);
    return Fl::run();
}