from discord.ext import commands
import discord
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
import matplotlib
matplotlib.use('AGG')
import io

class Graphing():

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=['plot'])
    async def graph(self, ctx, expr, lower_limit, upper_limit):
        """ Plots the given expression between upper and lower limit """
        expr_list = expr.split(';')
        expr_list = [parse_expr(e) for e in expr_list]

        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        buf = None

        # set the axis limits to avoid weird plots
        if lower_limit <= 0:
            axis_limit_lower = 0
        else:
            axis_limit_lower = lower_limit
        try:
            p = plot(*expr_list, (sympy.var('x'), lower_limit, upper_limit), axis_center = (axis_limit_lower, 0), show=False)
            buf = io.BytesIO()
            p.save(buf)
            buf.seek(0)
            await self.bot.send_file(ctx.message.channel, buf, filename='graph.png')
        except Exception as e:
            # log this instead...
            print(f'!! Exception occured during plotting: {e}')
            await self.bot.say(f'Invalid expression: {expr}')
        finally:
            if buf:
                buf.close()

def setup(bot):
    bot.add_cog(Graphing(bot))
