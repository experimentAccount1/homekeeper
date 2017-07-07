import click
import homekeeper
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)


@click.command(short_help='removes broken symlinks only')
@click.pass_context
def cleanup(ctx):
    h = ctx.obj['homekeeper']
    h.cleanup_symlinks = True
    h.overwrite = False
    h.cleanup()


@click.command(short_help='set dotfiles directory to current directory')
@click.pass_context
def init(ctx):
    h = ctx.obj['homekeeper']
    h.cleanup_symlinks = False
    h.overwrite = False
    h.cleanup()


@click.command(short_help='symlinks dotfiles to your home directory')
@click.pass_context
def keep(ctx):
    h = ctx.obj['homekeeper']
    h.keep()


@click.command(short_help='restores dotfiles and replacing symlinks')
@click.pass_context
def unkeep(ctx):
    h = ctx.obj['homekeeper']
    h.unkeep()


@click.group()
@click.option('--cleanup/--no-cleanup', default=True, is_flag=True,
              help='removes broken symlinks')
@click.option('--overwrite/--no-overwrite', default=True, is_flag=True,
              help='overwrite existing files or symlinks')
@click.option('--config-path', default=None, help='path to config file')
@click.pass_context
def main(ctx, cleanup, config_path, overwrite):
    h = homekeeper.Homekeeper(config_path=config_path)
    h.cleanup_symlinks = cleanup
    h.overwrite = overwrite
    ctx.obj = dict()
    ctx.obj['config_path'] = config_path
    ctx.obj['homekeeper'] = h


main.add_command(cleanup)
main.add_command(init)
main.add_command(keep)
main.add_command(unkeep)
