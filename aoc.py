#! /home/hiyer/.asdf/shims/python

import click
import requests
import os


def get_cookie():
    env_var = "AOC_SESSION"
    cookie = os.environ.get(env_var)
    if not cookie:
        click.secho(f"Session cookie not found. Please set ${env_var} environment variable", fg="red")
        raise click.Abort()
    return cookie


@click.command()
@click.option("-d", "--day", required=True, type=int)
@click.option("-y", "--year", required=False, default=2023, type=int)
def download(day, year):
    """ Download the input file for a given day """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    try:
        cookies = {'session': get_cookie()}
        click.secho(f"Downloading input file {url}", fg="green")
        r = requests.get(url, cookies=cookies, allow_redirects=True)
        r.raise_for_status()
        directory = f"y{year}/day{day}"
        click.secho(f"Creating directory {directory}", fg="green")
        os.makedirs(directory, exist_ok=True)
        open(f"{directory}/input.txt", "wb").write(r.content)
        click.secho(f"Wrote file {directory}/input.txt", fg="green")
    except click.Abort as e:
        click.secho(e, fg="red")
        raise SystemExit(1)
    except requests.exceptions.HTTPError as e:
        response_code = e.response.status_code
        if response_code in [400, 401, 403]:
            click.secho(f"Error {response_code}. Please check your session cookie (it may have expired)", fg="red")
        else:
            click.secho(e, fg="red")
        raise SystemExit(1)


@click.command()
@click.option("-d", "--day", required=True, type=int)
@click.option("-y", "--year", required=False, default=2023, type=int)
@click.option("-l", "--level", required=True, type=int)
@click.option("-a", "--answer", required=True, type=int)
def submit(day, year, level, answer):
    """ Submit a solution for a given day and level """

    from bs4 import BeautifulSoup as bs

    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    try:
        cookies = {'session': get_cookie()}
        form_data = {'level': level, 'answer': answer}
        r = requests.post(url, cookies=cookies, data=form_data)
        r.raise_for_status()
        soup = bs(r.content, "html.parser")
        message = ' '.join(soup.main.article.stripped_strings)
        if "not the right answer" in message or "too recently" in message:
            click.secho(message, fg="red")
        else:
            click.secho(message, fg="yellow")
    except requests.exceptions.HTTPError as e:
        response_code = e.response.status_code
        if response_code in [400, 401, 403]:
            click.secho(f"Error {response_code}. Please check your session cookie (it may have expired)", fg="red")
        else:
            click.secho(e, fg="red")

@click.command()
@click.option("-d", "--day", required=True, type=int)
@click.option("-y", "--year", required=False, default=2023, type=int)
@click.option("-l", "--level", required=False, type=int)
def get_question(day, year, level):
    """ Get the question description for a day """

    from bs4 import BeautifulSoup as bs

    url = f"https://adventofcode.com/{year}/day/{day}"
    try:
        cookies = {'session': get_cookie()}
        r = requests.get(url, cookies=cookies)
        r.raise_for_status()
        soup = bs(r.content, "html.parser")
        articles = soup.find_all("article", {"class": "day-desc"})
        if level and len(articles) >= (level - 1):
            click.secho('\n'.join(articles[level - 1].stripped_strings), fg="green")
        else:
            for idx, article in enumerate(articles):
                click.secho(f"Level {idx+1}", fg="yellow")
                click.secho('\n'.join(article.stripped_strings), fg="green")
    except requests.exceptions.HTTPError as e:
        response_code = e.response.status_code
        if response_code in [400, 401, 403]:
            click.secho(f"Error {response_code}. Please check your session cookie (it may have expired)", fg="red")
        else:
            click.secho(e, fg="red")




@click.group()
def cli():
    """ CLI for downloading AOC inputs and submitting the solutions.
        Needs the 'session' cookie from your browser session at adventofcode.com """
    pass


cli.add_command(download)
cli.add_command(submit)
cli.add_command(get_question)

if __name__ == '__main__':
    cli()
