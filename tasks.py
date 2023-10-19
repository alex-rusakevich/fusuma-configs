import glob
import os

from invoke import run, task


@task
def install(context):
    options = tuple(glob.glob("./configs/*.yml"))

    print("Please, choose your config:\n")

    for i, option in enumerate(options):
        print(f"{i+1}) {os.path.basename(option)}")

    chosen_opt = options[int(input("\nEnter config's number: ")) - 1]

    run("mkdir -p ~/.config/fusuma/")
    run(
        f"cp '{os.path.join('configs', os.path.basename(chosen_opt))}' ~/.config/fusuma/config.yml"
    )
