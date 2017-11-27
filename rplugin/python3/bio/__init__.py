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

    @neovim.command("CountFasta")
    def count_fasta_entries(self):
        buf = self.nvim.current.buffer[:]
#        num = buf.count(">")
#        self.echo(num)
        cnt = 0
        for line in buf:
            if line[0] == '>':
                cnt += 1
        self.echo(cnt)

    @neovim.command("FastaSingleLine", sync=False)
    def fasta_single_line(self):
        self.nvim.command("g/^>/s/\n/\r\r/g")
        self.nvim.command("%s/\n\(^[^>]\+\)/\1/g")
