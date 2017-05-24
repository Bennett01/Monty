from discord.ext import commands
import discord, sympy, io, matplotlib
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
matplotlib.use('AGG')

class Graphing():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['plot'])
    async def graph(self, ctx, expression, lower_limit='-10', upper_limit='10'):
        """
        Plots an expression between lower and upper limit.
        
        <expression> can be a semicolon separated list of expressions,
        example expr1;expr2;expr3...
        """
        if isinstance(lower_limit, str):
            try:
                lower_limit = float(lower_limit)
            except ValueError:
                return await self.bot.say(f'Invalid lower limit: {lower_limit}')
        if isinstance(upper_limit, str):
            try:
                upper_limit = float(upper_limit)
            except ValueError:
                return await self.bot.say(f'Invalid upper limit: {upper_limit}')

        expr_list = expression.split(';')
        expr_list = [parse_expr(e) for e in expr_list]

        var = expr_list[0].free_symbols.pop()
        limits = (var, lower_limit, upper_limit)

        buf = None
        try:
            p = plot(*expr_list, limits, axis_center = 'auto', show=False)
        except Exception as e:
            # log this instead...
            print(f'!! Exception occured during plotting: {e}')
            await self.bot.say(f'Could not plot: {expr_list}')
        else:
            buf = io.BytesIO()
            p.save(buf)
            buf.seek(0)
            await self.bot.send_file(ctx.message.channel, buf, filename='graph.png')
        finally:
            if buf:
                buf.close()

def setup(bot):
    bot.add_cog(Graphing(bot))
