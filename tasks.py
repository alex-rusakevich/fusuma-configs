import glob
import os

from invoke import run, task


@task
def install(context):
    options = sorted(os.path.basename(i) for i in glob.glob("./configs/*.yml"))

    print("Please, choose your config (press Ctrl-C to exit):\n")

    for i, option in enumerate(options):
        print(f"{i+1}) {option}")

    chosen_opt = options[int(input("\nEnter config's number: ")) - 1]

    print()

    run("mkdir -p ~/.config/fusuma/")

    if os.path.exists(os.path.expanduser("~/.config/fusuma/config.yml")):
        print(
            "'~/.config/fusuma/config.yml' already exists, backing it up as '~/.config/fusuma/config.yml.bak'..."
        )
        run("mv -f ~/.config/fusuma/config.yml ~/.config/fusuma/config.yml.bak")

    run(f"cp -f '{os.path.join('configs', chosen_opt)}' ~/.config/fusuma/config.yml")
    print("The config has been installed successfully! Restart fusuma, please")


@task
def remove(context):
    should_continue = (
        input(
            "Do you really want to remove fusuma config? \
All the changes in fusuma/config.yml will be lost! [y/n] "
        )
        .strip()
        .lower()
        == "y"
    )

    if not should_continue:
        print("Bye!")
        return

    run("rm ~/.config/fusuma/config.yml")
    print("The config has been removed successfully! Restart fusuma, please")
