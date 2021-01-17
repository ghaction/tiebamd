from argparse import ArgumentParser

from .crawl import TiebaCrawler
from requests import Session


def cli():
    p = ArgumentParser("tiebaMD")
    p.add_argument("post", help="帖子的链接或ID")
    p.add_argument("--repliers", action="store_true", help="是否包含回帖")
    p.add_argument("--http-proxy", help="指定 HTTP 代理，例如 http://127.0.0.1:8080")

    args = p.parse_args()
    start(args)


def start(args):
    session = Session()
    post = args.post
    has_reply = args.repliers
    proxy = args.http_proxy

    pid = post.split("/")[-1].split("?")[0] if not post.isdigit() else post
    tc = TiebaCrawler(session, pid, not has_reply)
    tc.set_proxy(proxy)
    tc.start()