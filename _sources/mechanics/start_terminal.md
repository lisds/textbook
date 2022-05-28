# Starting a terminal application on your computer

We use the (ahem) term *terminal* to mean an application that allows you to
run applications by typing commands.

Here's a screen-shot of a Mac terminal window:

![](../images/terminal_app.png)

There is a similar terminal window for (ahem) Windows.

The terminal has a *prompt* - in the Mac terminal above it is `[mb312@shanghai
~]$`, but yours will be different.  The cursor sits at the end of the prompt.
If you type in this window, the characters will appear at the prompt.  When
you type some text, and press Enter, the terminal will interpret what you
typed as commands to be sent to the computer.  Usually the commands will be
names of programs (applications) to run, along with any parameters that the
program needs.

## Opening the terminal - Windows

Go to the start menu.  Select the menu option "Anaconda (64-bit)".

![](../images/anaconda_menu_top.png)

Then select the option "Anaconda command prompt".

![](../images/anaconda_menu_prompt.png)

You should see a window like this:

![](../images/anaconda_terminal.png)

To test, type the command `dir` and press Enter.  You should see a listing of files in the directory that the terminal started in, rather like this:

![](../images/cmd_dir.png)

where the files on your computer will be the different from the first few files
that you see in this listing.

## Opening the terminal - Mac

Mac has a terminal application called Terminal.app.

You'll find it in the Utilities sub-folder of your Applications folder, but the easiest way to start it is via Spotlight.

Start spotlight by either:

*   Clicking on the magnifying glass icon at the right of your menu bar at the
    top of your screen

    ![](../images/spotlight_on_menu.png)

    or (the better option):
*   Press the command key (the key with the ⌘ symbol) and then (at the same
    time) the spacebar.

In either case, a mini-window like this will come up:

![](../images/spotlight_mini_window.png)

Type `terminal` in this window.  The first option that comes up is almost invariably the Terminal application:

![](../images/spotlight_terminal.png)

Select this by pressing Enter, and you should see the Terminal application window, as above.

If you see a window where there doesn't seem to be a prompt, that has several
lines starting with something like `[I 11:39:53.621 NotebookApp]`, then you have got to the Terminal window that Jupyter is using; you need a new window.  Choose "New Window" from the "Shell" menu in the menu bar to start a new window.  That window should be fresh, and look like the window at the top of the page.

## Opening the terminal - Linux

If you are on the class laptops, go to the desktop, and double-click on the "LXTerminal" icon.  This will open the terminal.

If you are not on the class laptops, and you don't know how to open a terminal, do a web search for "open terminal ubuntu" where "ubuntu" is your Linux distribution.  You should get some good hits.
