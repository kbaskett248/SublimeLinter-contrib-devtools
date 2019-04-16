import os.path
from SublimeLinter.lint import Linter

MAGIC_PATH = "C:\\Program Files (x86)\\PTCT-AP\\SoloFocus\\DevTools.Universe\\DevTools\\System\\Magic_Console.exe"
LINTER_PATH = "C:\\Program Files (x86)\\PTCT-AP\\SoloFocus\\DevTools.Universe\\DevTools\\PgmObject\\Hha\\HhaZtDev.Lint.P.mps"

class DevToolsLinter(Linter):
    regex = r'(?P<filename>.+?); (?P<line>\d+); \(((?P<warning>[DW])|(?P<error>E))\) (?P<message>.+)'
    multiline = False
    defaults = {
        'selector': 'source.focus'
    }
    tempfile_suffix = "-"

    def cmd(self):
        return '"%s" "%s" /f ${file} /wholefile' % (MAGIC_PATH, LINTER_PATH)

    def split_match(self, match):
        """Extracts data from each error result returned from the command.

        Data is extracted using the regex. A tuple of data is returned.

        Arguments:
            match (re.Match): An re.Match object obtained by using the object's
                regex attribute and an error line

        Returns:
            tuple: match - the match object
                   line - the line on which the error occurred
                   col - the column on which the error occurred
                   error - Truthy value if the line indicates an error. Falsey
                        value otherwise.
                   warning - Truthy value if the line indicates a warning.
                        Falsey value otherwise.
                   message - Message text for the error or warning
                   near - Text value that the error is near. This text is
                        underlined when displayed.

        """
        match, line, col, error, warning, message, near = super().split_match(match)

        if error:
            error = " "
        elif warning:
            warning = " "
        else:
            error = " "

        return match, line, col, error, warning, message, near
