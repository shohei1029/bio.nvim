import neovim

@neovim.plugin
class BioNvim(object):
    def __init__(self, nvim):
        self.nvim = nvim

    def echo(self, msg):
        self.nvim.command("echo '{}'".format(msg))

    @neovim.command("SNtest")
    def echo_test(self):
        self.echo("heyhey")
        print("printheyhey")

    @neovim.command("CountFasta")
    def count_fasta_entries(self):
        buf = self.nvim.current.buffer[:]
#        num = buf.count(">")
#        self.echo(num)
        self.echo(type(buf))
