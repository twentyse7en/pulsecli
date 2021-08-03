import click
import requests
from bs4 import BeautifulSoup

from rich.align import Align
from rich.console import Console, render_group
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.table import Table

BASE_URL = "https://pulse.zerodha.com/"
console = Console()


def _get_page():
    with console.status("[green]Fetching the page", spinner="point"):
        resp = requests.get(BASE_URL)
        resp.raise_for_status()
        return resp.text


def _extract_data(article):
    # some article doesn't have description
    desc_element = article.select(".desc")
    if desc_element == []:
        desc = ""
    else:
        desc = desc_element[0].text

    extracted_article = {
            'title': article.find('a').text,
            'url': article.find('a')['href'],
            'desc': desc,
            'time_elapsed': article.select(".date")[0].text,
            'source': article.select(".feed")[0].text,
            }
    return extracted_article


def display_list(articles, minimal):
    LAYOUT_WIDTH = 80

    @render_group()
    def render_article(article):
        yield Rule(style="bright_yellow")
        yield ""

        meta_data = article["time_elapsed"]+article["source"]
        title_table = Table.grid(padding=(0, 1))
        title_table.expand = True
        title = Text(article["title"], overflow="fold", style="yellow bold")
        title_table.add_row(title, Text(meta_data, style="blue dim"))
        title_table.columns[1].no_wrap = True
        title_table.columns[1].justify = "right"
        yield title_table
        yield ""

        description = article["desc"]
        if description != "" and not minimal:
            yield Text(description.strip(), style="green")

        if not minimal:
            url = article["url"]
            yield(Text(url, style="dim italic"))
        yield ""

    def column(renderable):
        return Align.center(renderable, width=LAYOUT_WIDTH, pad=False)

    for article in articles:
        console.print(column(render_article(article)))
    console.print(column(Rule(style="bright_yellow")))


def display_grid(articles, minimal):
    max_desc_len = 90
    panels = []
    for article in articles:
        title = Text(article["title"], style="bold yellow")
        time_elapsed = Text(article["time_elapsed"], style="magenta")
        source = Text(article["source"], style="blue")
        desc = Text(article["desc"], style="green")
        desc.truncate(max_desc_len, overflow="ellipsis")
        article_summary = Text.assemble(
                    title,
                    "\n",
                    time_elapsed,
                    " ",
                    source
                )
        if not minimal:
            article_summary = Text.assemble(article_summary, "\n", desc)
        panels.append(Panel(article_summary, expand=True))
    console.print((Columns(panels, width=30, expand=True)))


def _scrape_articles(limit):
    soup = BeautifulSoup(_get_page(), features="lxml")
    news = soup.find(id="news")
    articles = news.find_all("li")

    extracted_articles = []
    for article in articles[:limit]:
        data = _extract_data(article)
        extracted_articles.append(data)
    return extracted_articles


def _get_news(limit, style, minimal):
    extracted_articles = _scrape_articles(limit)
    with console.pager(styles=True):
        if style == "grid":
            display_grid(extracted_articles, minimal)
        else:
            display_list(extracted_articles, minimal)


@click.command()
@click.option(
        "--limit",
        "-l",
        default=30,
        type=int,
        help="limit the number of news. Default: 30"
)
@click.option(
        "--style",
        "-s",
        default="list",
        type=click.Choice(["list", "grid"], case_sensitive=False),
        help="Output style (list, grid), default is list"
)
@click.option(
        "--minimal",
        "-m",
        is_flag=True,
        help="Display news without description and url"
        )
def cli(limit, style, minimal):
    try:
        _get_news(limit, style, minimal)
    except requests.HTTPError:
        print("Unable to connect to pulse.")
    except requests.ConnectionError:
        print("Unable to connect. Check your connection")


if __name__ == '__main__':
    cli()
