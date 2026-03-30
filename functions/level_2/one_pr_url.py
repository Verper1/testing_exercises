def is_github_pull_request_url(url: str) -> bool:
    """Проверка url строки на то, что она является PR."""
    splitted_url = url.split("/")  # ['https:', '', 'github.com', 'Verper1', 'typing_challenges', 'pull', '3']
    return len(splitted_url) == 7 and splitted_url[2] == "github.com" and splitted_url[5] == "pull"
