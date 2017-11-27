import neovim

@neovim.plugin
class BioNvim(object):
    def __init__(self, nvim):
        self.nvim = nvim

    def echo(self, msg):
        self.nvim.command("echo '{}'".format(msg))

    @neovim.command("CountFasta")
    def count_fasta_entries(self):
        buf = self.nvim.buffer[:]
        num = buf.count(">")
        self.echo(num)
