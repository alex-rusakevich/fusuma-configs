import glob
import os

from invoke import run, task


@task
def install(context):
    options = tuple(os.path.basename(i) for i in glob.glob("./configs/*.yml"))

    print("Please, choose your config:\n")

    for i, option in enumerate(options):
        print(f"{i+1}) {option}")

    chosen_opt = options[int(input("\nEnter config's number: ")) - 1]

    print()

    run("mkdir -p ~/.config/fusuma/")

    if os.path.exists(os.path.expanduser("~/.config/fusuma/config.yml")):
        print(
            "'~/.config/fusuma/config.yml' already exists, backing it up as '~/.config/fusuma/config.yml.bak'..."
        )
        run("cp ~/.config/fusuma/config.yml ~/.config/fusuma/config.yml.bak")

    run(f"cp '{os.path.join('configs', chosen_opt)}' ~/.config/fusuma/config.yml")

    print("The config has been installed successfully!")
