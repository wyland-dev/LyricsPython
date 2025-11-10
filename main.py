import sys
from rich import print
from time import sleep
import time

tree =f'''    
    [chartreuse4]*
   [yellow1]*[/yellow1]*[deep_pink1]*[/deep_pink1]
  *[bright_blue]*[/bright_blue]*[red3]*[/red3]*
 [deep_pink1]*[/deep_pink1]**[yellow1]*[/yellow1]***
**[red3]*[/red3]**[bright_blue]*[/bright_blue]*[yellow1]*[/yellow1]*[/chartreuse4]
   [orange4]|||[/orange4]
'''

lines = [
        ('Once bitten and twice shy-y-y-y', 0.09),
        ("I keep my distance,", 0.09),
        ('but you still catch my eye', 0.09),
        ('Tell me, baby, do you recognise me?', 0.08),
        ("Well, it's been a year,", 0.08),
        ("it doesn't surprise me", 0.08),
        ('"Happy Christmas,"', 0.05),
        ("I wrapped it up and sent it", 0.08),
        ('With a note saying,', 0.09),
        ('"I love you,"', 0.09),
        ('I meant it', 0.09),
        ("Now I know what a fool I've been", 0.1),
        ("But if you kissed me now", 0.08),
        ("I know you'd fool me again", 0.08)
    ]

delays = [1.1, 0, 0.7, 1.1, 0, 1.1, 0.4, 0, 0, 0.4, 0.6, 0, 0.4]

def printtext():
    try:
        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                if line ==  '"Happy Christmas,"':
                    print(f'[italic][gold3]{char}[/italic][/gold3]', end='')
                    sys.stdout.flush()
                    sleep(char_delay)
                elif line == '"I love you,"':
                    print(f'[italic][red3]{char}[/italic][/red3]', end='')
                    sys.stdout.flush()
                    sleep(char_delay)
                else:
                    print(f'[bold][dark_sea_green4]{char}[/bold][/dark_sea_green4]', end='')
                    sys.stdout.flush()
                    sleep(char_delay)
            print()
            sleep(delays[i])
    except:
        print(tree)

printtext()