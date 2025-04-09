# main.py

import math


def define_env(env):
    @env.macro
    def reading_stats(content):
        words = len(content.split()) - 137  # adjust for titles, figures
        minutes = max(1, math.ceil(words / 200))
        return {"words": f"{words:,} words", "time": f"{minutes} min read"}
