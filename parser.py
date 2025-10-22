#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# parser.py - BibTeX -> Hugo Blox Markdown

import os
import re
from pathlib import Path
import bibtexparser
import yaml

# ================= 配置 =================
BIB_FILE = "references.bib"           # BibTeX 文件路径
OUTPUT_DIR = "content/publication"    # Hugo publications 存放目录
PDF_DIR = "static/files/papers"       # PDF 文件目录（可选）
# ========================================

def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符"""
    return re.sub(r'[^0-9A-Za-z._-]', '_', name)

def format_authors(entry: dict) -> list:
    """保持作者列表，返回 YAML 列表形式"""
    authors = []
    raw = entry.get("author", "")
    if not raw:
        return authors
    parts = raw.replace("\n", " ").split(" and ")
    for p in parts:
        name = p.strip().replace("{", "").replace("}", "")
        if name:
            authors.append(name)
    return authors

def extract_doi_raw(doi_field: str) -> str:
    """提取 DOI 原始值，不带 http(s)://"""
    if not doi_field:
        return ""
    m = re.search(r'(10\.\d{4,9}/\S+)', doi_field)
    if m:
        return m.group(1).rstrip('.,;')
    return ""

def entry_to_frontmatter(entry: dict) -> dict:
    """BibTeX 条目 -> front matter dict"""
    title = entry.get("title", "").replace("{", "").replace("}", "").strip()
    year = entry.get("year", "").strip() if entry.get("year") else ""
    journal = entry.get("journal", "").replace("{", "").replace("}", "").strip()
    volume = entry.get("volume", "").strip()
    number = entry.get("number", "").strip()
    pages = entry.get("pages", "").strip()

    doi_raw = extract_doi_raw(entry.get("doi", ""))
    url_field = entry.get("url", "").strip()
    url = url_field if url_field else ""

    # PDF 文件检测
    pdf_path = ""
    bib_id = entry.get("ID", "")
    if bib_id:
        candidate = os.path.join(PDF_DIR, f"{sanitize_filename(bib_id)}.pdf")
        if os.path.exists(candidate):
            pdf_path = candidate
        else:
            candidate2 = os.path.join(PDF_DIR, f"{sanitize_filename(title)}.pdf")
            if os.path.exists(candidate2):
                pdf_path = candidate2

    date = f"{year}-01-01" if year else ""

    front = {}
    if title:
        front["title"] = title
    authors = format_authors(entry)
    if authors:
        front["authors"] = authors
    if journal:
        front["publication"] = journal
    if volume:
        front["volume"] = volume
    if number:
        front["issue"] = number
    if pages:
        front["pages"] = pages
    if date:
        front["date"] = date
    if doi_raw:
        front["doi"] = doi_raw
    if url and not doi_raw:
        front["url"] = url
    if pdf_path:
        front["pdf"] = pdf_path

    return front

def write_md(out_dir: Path, front: dict):
    """写入 index.md"""
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "index.md"
    yaml_text = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    content = f"---\n{yaml_text}---\n"
    md_path.write_text(content, encoding="utf-8")
    return md_path

def main():
    if not os.path.exists(BIB_FILE):
        print(f"Error: BibTeX file '{BIB_FILE}' not found.")
        return

    with open(BIB_FILE, "r", encoding="utf-8") as f:
        bib_database = bibtexparser.load(f)

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    for entry in bib_database.entries:
        bib_id = entry.get("ID", "")
        fname = sanitize_filename(bib_id if bib_id else entry.get("title", "untitled"))
        out_dir = Path(OUTPUT_DIR) / fname
        front = entry_to_frontmatter(entry)
        md_file = write_md(out_dir, front)
        print(f"Generated: {md_file}")

if __name__ == "__main__":
    main()

