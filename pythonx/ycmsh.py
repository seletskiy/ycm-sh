import vim
import os.path
import tempfile

def inject():
    new_config = ""

    payload_path = vim.eval('expand("<sfile>:p:h:h")') + "/payload.py"
    config_path = vim.eval('get(g:, "ycm_global_ycm_extra_conf", "")')

    if config_path and os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            new_config = config_file.read() + "\n"

    new_config += "### generated by ycm-sh ####\n"

    with open(payload_path, "r") as payload_file:
        new_config += payload_file.read()

    (_, new_config_path) = tempfile.mkstemp("_ycm-sh")
    with open(new_config_path, "w") as new_config_file:
        new_config_file.write(new_config)

    vim.command("let g:ycm_global_ycm_extra_conf = '" + new_config_path + "'")
